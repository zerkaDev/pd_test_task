from api_worker.validator import get_sorted_and_validated_users, get_sorted_and_validated_todos
from tests.test_factory import create_valid_users_json, create_non_valid_users_json, create_valid_todos_json, \
    create_non_valid_todos_json


def test_validate_valid_users_success():
    users = create_valid_users_json(5)
    users_after_validate = get_sorted_and_validated_users(users)

    assert len(users) == len(users_after_validate)


def test_validate_nonvalid_users_succes():
    non_valid_users = create_non_valid_users_json(5)
    users_after_validate = get_sorted_and_validated_users(non_valid_users)

    assert len(users_after_validate) == 0


def test_validate_valid_todo_success():
    valid_todos = create_valid_todos_json(5, 1)
    todos_after_validate = get_sorted_and_validated_todos(valid_todos)

    assert len(valid_todos) == len(todos_after_validate)


def test_validate_non_valid_todo_success():
    non_valid_todos = create_non_valid_todos_json(5, 1)
    todos_after_validate = get_sorted_and_validated_todos(non_valid_todos)

    assert len(todos_after_validate) == 0



