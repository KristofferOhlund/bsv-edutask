describe("Todo create", () => {
    beforeEach(() => {
        cy.visit("http://localhost:3000/");
        cy.get("#email").type("kroh24@student.bth.se{enter}");
    })
    
    it("Create Todo item", () => {
    // Select previous created Task
    cy.get('.container .container-element').first().click()
    cy.get('[placeholder="Add a new todo item"]').click().type("Our first todo{enter}")
    })

    it("Toggle Todo item", () => {
        cy.get(".container .container-element").first().click();
        cy.get('.unchecked').first().click()
    })
    // create Todo
})
