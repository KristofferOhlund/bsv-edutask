describe("Todo tests", () => {
    beforeEach(() => {
      // To create waiters for updates in DOM
      cy.intercept('GET', '**/tasks/**').as('getTaskTodos');
      cy.intercept('POST', '**/todos/**').as('createTodo');
      cy.intercept('DELETE', '**/todos/**').as('deleteTodo');

      cy.visit("http://localhost:3000/");
      cy.get("#email").type("kroh24@student.bth.se{enter}");
      cy.viewport(1200, 3000);
      cy.contains(".container-element", "Test task").click();
    })

    it("Create Todo item", () => {
      cy.get('[placeholder="Add a new todo item"]').should('be.visible');
      cy.get('[placeholder="Add a new todo item"]').click().type("Our first todo{enter}");
      // Wait for mongo. Create todo, Fetch todos.
      cy.wait('@createTodo');
      cy.wait('@getTaskTodos');
      
      cy.contains(".todo-item", "Our first todo").should("exist");
      cy.contains(".todo-item", "Our first todo").find(".remover").click();

      // Wait for mongo. Delete todo, Fetch todos (empty! hopefully).
      cy.wait('@deleteTodo');
      cy.wait('@getTaskTodos');
      
      cy.contains(".todo-item", "Our first todo").should("not.exist");
    })

    it("Button is disabled on empty input", () => {
      cy.get('.todo-list').find('input[type="submit"]').then(($btn) => {
        console.log($btn[0])
      })
      // It does not have that attribute when inspected...
      cy.get('.todo-list').find('input[type="submit"]').should('have.attr', 'disabled');
      cy.get('.todo-list').find('input[type="submit"]').should('be.disabled');
    })

    it("Button not disabled with text in input", () => {
      cy.get('[placeholder="Add a new todo item"]').click().type("Our first todo");
      cy.contains('input[type="submit"]', 'Add').should('not.have.attr', 'disabled');
      cy.contains('input[type="submit"]', 'Add').should('not.be.disabled');
    })

    it("Toggle Todo item", () => {
      // Arrange
      cy.get('[placeholder="Add a new todo item"]').click().type("A new todo_1{enter}")
      // // https://docs.cypress.io/app/core-concepts/variables-and-aliases
      // // You cannot assign or work with the return values of any Cypress command.
      // // Commands are enqueued and run asynchronously.
      // const checker = cy
      //   .contains(".todo-item", "A new todo_1")
      //   .find(".checker");
      
      // Act
      // checker.click();
      cy.contains(".todo-item", "A new todo_1").find(".checker").click();

      // Assert toggle on and off (double asserts OK? separate tests?)
      // checker.should('have.class', 'checked');
      // checker.click();
      // checker.should('have.class', 'unchecked');
      cy.contains(".todo-item", "A new todo_1").find(".checker").should('have.class', 'checked');
      cy.contains(".todo-item", "A new todo_1").find(".checker").click();
      cy.contains(".todo-item", "A new todo_1").find(".checker").should('have.class', 'unchecked');
      // Clean-up
      cy.contains(".todo-item", "A new todo_1").find('.remover').click();
    })

    // Delete Todo
    it("Delete todo item", () => {
      cy.get('[placeholder="Add a new todo item"]').click().type("A new todo_2{enter}");
      cy.wait('@createTodo');
      cy.wait('@getTaskTodos');

      cy.contains(".todo-item", "A new todo_2").find(".remover").click();
      
      cy.wait('@deleteTodo');
      cy.wait('@getTaskTodos');
      cy.contains(".todo-item", "A new todo_2").should('not.exist');
    })
})
