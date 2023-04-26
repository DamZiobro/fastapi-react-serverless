import pytest
from fastapi.testclient import TestClient

from api.main import (
    app,
    create_todo_repository,
)
from api.models import (
    TodoDTO,
    TodoModel,
)
from api.repos import (
    InMemoryTodoRepository,
    TodoInterface,
)


@pytest.fixture
def todo_repository() -> TodoInterface:
    repo = InMemoryTodoRepository()
    repo.todos = []  # clear persistance between each test
    return repo


@pytest.fixture
def client(todo_repository: TodoInterface, monkeypatch) -> TestClient:
    app.dependency_overrides[create_todo_repository] = lambda: todo_repository
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


def test_create_todo_repository():
    todo_repository = create_todo_repository()
    assert isinstance(todo_repository, InMemoryTodoRepository)


# Test create_todo_handler
def test_create_todo_handler_returns_201(
    client: TestClient, todo_repository: TodoInterface, monkeypatch
):
    # Test case: create a new Todo successfully
    new_todo = TodoDTO(task="test task", description="test description")
    created_todo = TodoModel(id=1, task="test task", description="test description")
    monkeypatch.setattr(todo_repository, "create_todo", lambda todo: created_todo)

    response = client.post("/todos/", json=new_todo.dict())
    assert response.status_code == 201
    assert response.json() == created_todo.dict()


def test_create_todo_handler_validates_missing_input_fields(
    client: TestClient, todo_repository: TodoInterface, monkeypatch
):
    # Test case: create a new Todo with missing required fields
    response = client.post("/todos/", json={"description": "test task"})
    assert response.status_code == 422


def test_create_todo_handler_validates_incorrect_type_of_input_field(
    client: TestClient, todo_repository: TodoInterface, monkeypatch
):
    # Test case: create a new Todo with invalid input type
    invalid_todo = {"description": 123}
    monkeypatch.setattr(todo_repository, "create_todo", lambda todo: invalid_todo)

    response = client.post("/todos/", json=invalid_todo)
    assert response.status_code == 422


# Test update_todo_handler
def test_update_todo_handler(
    client: TestClient, todo_repository: TodoInterface, monkeypatch
):
    # Test case: update an existing Todo successfully
    existing_todo = TodoModel(id=1, task="test task", description="test description")
    updated_todo = TodoModel(
        id=1, task="updated task", description="updated description"
    )
    monkeypatch.setattr(
        todo_repository, "update_todo_by_id", lambda id, todo: updated_todo
    )

    response = client.put(f"/todos/{existing_todo.id}", json=updated_todo.dict())
    assert response.status_code == 200
    assert response.json() == updated_todo.dict()


def test_update_todo_handler_returns_404_for_non_existing_todos(
    client: TestClient, todo_repository: TodoInterface, monkeypatch
):
    # Test case: update a non-existing Todo
    updated_todo = TodoModel(
        id=1, task="updated task", description="updated description"
    )
    non_existing_todo_id = 2
    monkeypatch.setattr(todo_repository, "update_todo_by_id", lambda id, todo: None)

    response = client.put(f"/todos/{non_existing_todo_id}", json=updated_todo.dict())
    assert response.status_code == 404


def test_read_todo_handler(client, todo_repository, monkeypatch):
    # Arrange
    todo = TodoModel(id=1, task="Test task", description="Test description")
    monkeypatch.setattr(todo_repository, "read_todo_by_id", lambda todo_id: todo)

    # Act
    response = client.get("/todos/1")

    # Assert
    assert response.status_code == 200
    assert response.json() == todo.dict()


def test_read_todo_handler_not_found(client, todo_repository, monkeypatch):
    # Arrange
    monkeypatch.setattr(todo_repository, "read_todo_by_id", lambda todo_id: None)

    # Act
    response = client.get("/todos/1")

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}


def test_delete_todo_handler(client, todo_repository, monkeypatch):
    # Arrange
    monkeypatch.setattr(todo_repository, "delete_todo_by_id", lambda todo_id: True)

    # Act
    response = client.delete("/todos/1")

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted successfully"}


def test_delete_todo_handler_not_found(client, todo_repository, monkeypatch):
    # Arrange
    monkeypatch.setattr(todo_repository, "delete_todo_by_id", lambda todo_id: False)

    # Act
    response = client.delete("/todos/1")

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo 1 not found"}


def test_read_todos(
    client: TestClient, todo_repository: InMemoryTodoRepository, monkeypatch
):
    # Define test data
    test_todo_1 = TodoModel(id=1, task="Task 1", description="Description 1")
    test_todo_2 = TodoModel(id=2, task="Task 2", description="Description 2")

    # Mock the read_todos method to return test data
    monkeypatch.setattr(
        todo_repository, "read_todos", lambda: [test_todo_1, test_todo_2]
    )

    # Call the API endpoint
    response = client.get("/todos/")

    # Assert the response
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["task"] == test_todo_1.task
    assert response.json()[1]["description"] == test_todo_2.description
