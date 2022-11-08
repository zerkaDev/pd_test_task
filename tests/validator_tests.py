from api_worker.validator import get_sorted_and_validated_users, get_sorted_and_validated_todos, \
    ensure_todo_have_relation_and_required_variables
from tests.test_factory import create_valid_users_json, create_non_valid_users_json, create_valid_todos_json, \
    create_non_valid_todos_json, create_non_valid_user_by_values_json


def test_validate_valid_users_success():
    users = create_valid_users_json(5)
    users_after_validate = get_sorted_and_validated_users(
        users)

    assert len(users) == len(users_after_validate)


def test_validate_non_valid_users_success():
    non_valid_users = create_non_valid_users_json(5)
    users_after_validate = get_sorted_and_validated_users(
        non_valid_users)

    assert len(users_after_validate) == 0


def test_validate_valid_todo_success():
    valid_todos = create_valid_todos_json(5, 1)
    todos_after_validate = get_sorted_and_validated_todos(
        valid_todos)

    assert len(valid_todos) == len(todos_after_validate)


def test_validate_non_valid_todo_success():
    non_valid_todos = create_non_valid_todos_json(5, 1)
    todos_after_validate = get_sorted_and_validated_todos(
        non_valid_todos)

    assert len(todos_after_validate) == 0


def test_validate_non_valid_by_values_todo_success():
    non_valid_todo = create_non_valid_user_by_values_json(5)
    todo, is_created = ensure_todo_have_relation_and_required_variables(
        non_valid_todo)

    assert todo is None
    assert is_created is False
