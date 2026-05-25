describe("Todo tests", () => {
  before(() => {
    // To create waiters for updates in DOM
    // https://docs.cypress.io/api/commands/wait
    cy.intercept("GET", "**/users/**").as("getUser");
    cy.intercept("GET", "**/tasks/**").as("getTaskTodos");
    cy.intercept("POST", "**/todos/**").as("createTodo");
    cy.intercept("DELETE", "**/todos/**").as("deleteTodo");

    cy.viewport(1200, 3000);
    cy.visit("http://localhost:3000/");
    cy.get("#email").type("kroh24@student.bth.se{enter}");
    cy.wait("@getUser");

    cy.contains(".container-element", "Test task").click();
    cy.wait("@getTaskTodos");
    // https://docs.cypress.io/api/commands/each#DOM-Elements
  });

  it("Create named Todo item", () => {
    // Cont. Arrange
    cy.get('[placeholder="Add a new todo item"]').should("be.visible");

    // Act
    cy.get('[placeholder="Add a new todo item"]')
      .click()
      .type("Our first todo{enter}");
    // Wait for mongo. Create todo, Fetch todos.
    cy.wait("@createTodo");
    cy.wait("@getTaskTodos");

    // Assert
    cy.contains(".todo-item", "Our first todo").should("be.visible");
  });

  after(() => {
    // Clean-up
    cy.contains(".todo-item", "Our first todo").find(".remover").click();
    cy.wait("@deleteTodo");
    cy.wait("@getTaskTodos");
  })
});


