describe("Todo tests", () => {
    beforeEach(() => {
        cy.visit("http://localhost:3000/");
        cy.get("#email").type("kroh24@student.bth.se{enter}");
        cy.viewport(2000, 2000);
    })
    
    // it("Create Todo item", () => {
    // // Select previous created Task
    //   cy.get('.container .container-element').first().click()
    //   cy.get('[placeholder="Add a new todo item"]').click().type("Our first todo{enter}")
    // })

    it("Toggle Todo item", () => {
      // Arrange
      cy.contains('.title-overlay', 'Test task').click()
      cy.get('[placeholder="Add a new todo item"]').click().type("A new todo_1{enter}")
      // Act
      // cy.get(".container .container-element").first().click();
      const checker = cy.contains('.todo-item', "A new todo_1").find('.checker');
      checker.click();
      // Assert toggle on and off (double asserts OK? separate tests?)
      checker.should('have.class', 'checked');
      checker.click();
      checker.should('have.class', 'unchecked');
      // Clean-up
      checker.parent().find('.remover').click();
    })

    // Delete Todo
})
