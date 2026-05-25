describe("Toggle Todo items", () => {
  beforeEach(() => {
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

  it("Toggle On", () => {
    // Arrange
    cy.get('[placeholder="Add a new todo item"]').should("be.visible");
    cy.get('[placeholder="Add a new todo item"]')
      .click()
      .type("A new todo_1{enter}");
    cy.wait("@createTodo");
    cy.wait("@getTaskTodos");

    // Act
    cy.contains(".todo-item", "A new todo_1").find(".checker").click();

    // Assert toggle on
    cy.contains(".todo-item", "A new todo_1")
      .find(".checker")
      .should("have.class", "checked");
  });

  it("Toggle Off", () => {
    // Arrange
    cy.get('[placeholder="Add a new todo item"]').should("be.visible");
    cy.get('[placeholder="Add a new todo item"]')
      .click()
      .type("A new todo_1{enter}");
    cy.wait("@createTodo");
    cy.wait("@getTaskTodos");

    // Act
    cy.contains(".todo-item", "A new todo_1").find(".checker").click();
    cy.contains(".todo-item", "A new todo_1").find(".checker").click();

    // Assert Toggle off
    cy.contains(".todo-item", "A new todo_1")
      .find(".checker")
      .should("have.class", "unchecked");
  });

  afterEach(() => {
    // Clean-up
    cy.contains(".todo-item", "A new todo_1").find(".remover").click();
    cy.wait("@deleteTodo");
    cy.wait("@getTaskTodos");
  });
});
