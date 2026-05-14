describe("Todo tests", () => {
    beforeEach(() => {
        cy.visit("http://localhost:3000/");
        cy.get("#email").type("kroh24@student.bth.se{enter}");
        cy.viewport(2000, 2000);
        cy.get(".container-element:has(a)").first().click();
    })
    
    it("Create Todo item", () => {
      cy.get('[placeholder="Add a new todo item"]').click().type("Our first todo{enter}");
      cy.contains(".todo-item", "Our first todo").should("exist");
      cy.contains(".todo-item", "Our first todo").parent().find(".remover").first().click();
    })

    it("Toggle Todo item", () => {
      // Arrange
      cy.get('[placeholder="Add a new todo item"]').click().type("A new todo_1{enter}")
      const checker = cy
        .contains(".todo-item", "A new todo_1")
        .find(".checker");
      
      // Act
      checker.click();

      // Assert toggle on and off (double asserts OK? separate tests?)
      checker.should('have.class', 'checked');
      checker.click();
      checker.should('have.class', 'unchecked');
      // Clean-up
      checker.parent().find('.remover').click();
    })

    // Delete Todo
    it("Delete todo item", () => {
        cy.get('[placeholder="Add a new todo item"]')
          .click()
          .type("A new todo_1{enter}");
        cy.get(".todo-list").find("li").first().children(".remover").click();
        cy.get(".close-btn").click()
        cy.get(".container-element:has(a)").first().click();

        // Nu är GUI uppdaterat
        cy.get(".todo-list").should("have.length", 1);
    })
})
