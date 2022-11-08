from api_worker.validator import get_sorted_and_validated_todos, get_sorted_and_validated_users
from api_worker.worker import get_users_vm_from_json
from tests.test_factory import create_valid_todos_json, create_valid_user_json, create_non_valid_todos_json


def test_vm_one_user():
    valid_todos = create_valid_todos_json(100, 1)
    valid_user = [create_valid_user_json(1)]

    user_vm = get_users_vm_from_json(users=get_sorted_and_validated_users(valid_user),
                                     todos=get_sorted_and_validated_todos(valid_todos))[0]

    assert user_vm is not None
    assert user_vm.todos_completed_count == 0
    assert user_vm.todos_uncompleted_count == 100


def test_vm_one_user_diff_todos():
    valid_todos = create_valid_todos_json(100, 1)
    non_valid_todos = create_non_valid_todos_json(100, 1)
    valid_user = [create_valid_user_json(1)]

    todos = get_sorted_and_validated_todos(valid_todos)+(get_sorted_and_validated_todos(non_valid_todos))
    user_vm = get_users_vm_from_json(users=get_sorted_and_validated_users(valid_user),
                                     todos=todos)[0]

    assert user_vm is not None
    assert user_vm.todos_completed_count == 0
    assert user_vm.todos_uncompleted_count == 100
