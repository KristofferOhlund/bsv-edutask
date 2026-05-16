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

      // removeTodos();
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
          // Recursive call
          // if(cy.get('.todo-list').find('.remover').length) {
          //   removeTodos();
          // }
          removeTodos();
        }
      })
    }

  //   // AI version
  //   function removeTodos() {
  //   cy.get('.todo-list').then(($todoList) => {
  //     const count = $todoList.find('.remover').length;
      
  //     if (count === 0) return;

  //     // Loop exactly as many times as removers exist right now
  //     Cypress._.times(count, () => {
  //       cy.get('.remover').first().click();
  //       cy.wait('@deleteTodo');
  //       cy.wait('@getTaskTodos');
  //     });
  //   });
  // }

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

    // it("Fail to create unnamed Todo item", () => {
    //   cy.get('[placeholder="Add a new todo item"]').should('be.visible');
      
    //   // cy.get('.todo-list').find('input[type="submit"]').should('be.disabled'); SEPARATE TEST
    //   cy.get('.todo-list').find('input[type="submit"]').click();
    //   // Assert
    //   cy.get('@createTodo.all').should('have.length', 0)
    //   cy.get(".todo-list").should("exist");
    //   cy.get(".todo-item").should("not.exist");

    // })

    it("Button is disabled on empty input", () => {
      // cy.get('.todo-list').find('input[type="submit"]').then(($btn) => {
      //   console.log($btn[0])
      // })
      // It does not have that attribute when inspected...
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
      // Clean-up
      // cy.contains(".todo-item", "A new todo_1").find('.remover').click();
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
