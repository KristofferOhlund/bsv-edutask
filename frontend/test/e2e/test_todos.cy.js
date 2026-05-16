describe("Todo tests", () => {
    beforeEach(() => {
      // To create waiters for updates in DOM
      // https://docs.cypress.io/api/commands/wait
      cy.intercept('GET', '**/users/**').as('getUser');
      cy.intercept('GET', '**/tasks/**').as('getTaskTodos');
      cy.intercept('POST', '**/todos/**').as('createTodo');
      cy.intercept('DELETE', '**/todos/**').as('deleteTodo');

      cy.viewport(1200, 3000);
      cy.visit("http://localhost:3000/");
      cy.get("#email").type("kroh24@student.bth.se{enter}");
      cy.wait('@getUser');

      cy.contains(".container-element", "Test task").click();
      cy.wait('@getTaskTodos');
      // https://docs.cypress.io/api/commands/each#DOM-Elements

      removeTodos();
    })

    // .each() breaks, https://stackoverflow.com/a/69371000 is flaky, 
    function removeTodos() {
      cy.get('[placeholder="Add a new todo item"]').should('be.visible');
      cy.get('.todo-list').then(($todoList) => {
        if($todoList.find('.remover').length) {
          cy.get('.remover').first().click();
          // Wait for mongo calls
          cy.wait('@deleteTodo');
          cy.wait('@getTaskTodos');
          removeTodos();
        }
      })
    }

    it("Create named Todo item", () => {
      // Cont. Arrange
      cy.get('[placeholder="Add a new todo item"]').should('be.visible');
      
      // Act
      cy.get('[placeholder="Add a new todo item"]').click().type("Our first todo{enter}");
      // Wait for mongo. Create todo, Fetch todos.
      cy.wait('@createTodo');
      cy.wait('@getTaskTodos');
      
      // Assert
      cy.contains(".todo-item", "Our first todo").should("be.visible");

      // Clean-up
      cy.contains(".todo-item", "Our first todo").find(".remover").click();
      cy.wait('@deleteTodo');
      cy.wait('@getTaskTodos');
    })

    it("Button is disabled on empty input", () => {
      cy.get('.todo-list').find('input[type="submit"]').should('be.disabled');
      cy.get('.todo-list').find('input[type="submit"]').should('have.attr', 'disabled');
    })

    it("Button not disabled with text in input", () => {
      cy.get('[placeholder="Add a new todo item"]').click().type("Our first todo");
      cy.get('.todo-list').find('input[type="submit"]').should('not.be.disabled');
      cy.get('.todo-list').find('input[type="submit"]').should('not.have.attr', 'disabled');
    })

    it("Toggle Todo item", () => {
      // Arrange
      cy.get('[placeholder="Add a new todo item"]').should('be.visible');
      cy.get('[placeholder="Add a new todo item"]').click().type("A new todo_1{enter}")
      cy.wait('@createTodo');
      cy.wait('@getTaskTodos');

      // Act
      cy.contains(".todo-item", "A new todo_1").find(".checker").click();

      // Assert toggle on and off (double asserts OK?)
      cy.contains(".todo-item", "A new todo_1").find(".checker").should('have.class', 'checked');
      cy.contains(".todo-item", "A new todo_1").find(".checker").click();
      cy.contains(".todo-item", "A new todo_1").find(".checker").should('have.class', 'unchecked');
    })

    // Delete Todo
    it("Delete todo item", () => {
      cy.get('[placeholder="Add a new todo item"]').should('be.visible');
      cy.get('[placeholder="Add a new todo item"]').click().type("A new todo_2{enter}");

      cy.wait('@createTodo');
      cy.wait('@getTaskTodos');

      cy.contains(".todo-item", "A new todo_2").find(".remover").click();
      
      cy.wait('@deleteTodo');
      cy.wait('@getTaskTodos');
      cy.contains(".todo-item", "A new todo_2").should('not.exist');
    })
})
