from api_worker.validator import get_sorted_and_validated_todos, \
    get_sorted_and_validated_users
from api_worker.worker import get_users_vm_from_json
from tests.test_factory import create_valid_todos_json, create_valid_user_json, \
    create_non_valid_todos_json


def test_vm_one_user():
    valid_todos = create_valid_todos_json(100, 1)
    valid_user = [create_valid_user_json(1, 'name', 'username')]

    user_vm = get_users_vm_from_json(
        users=get_sorted_and_validated_users(valid_user),
        todos=get_sorted_and_validated_todos(valid_todos))[0]

    assert user_vm is not None
    assert user_vm.todos_completed_count == 0
    assert user_vm.todos_uncompleted_count == 100


def test_vm_one_user_diff_todos():
    valid_todos = create_valid_todos_json(100, 1)
    non_valid_todos = create_non_valid_todos_json(100, 1)
    valid_user = [create_valid_user_json(1, 'name', 'username')]

    todos = get_sorted_and_validated_todos(valid_todos) + \
        (get_sorted_and_validated_todos(non_valid_todos))
    user_vm = get_users_vm_from_json(
        users=get_sorted_and_validated_users(valid_user), todos=todos)[0]

    assert user_vm is not None
    assert user_vm.todos_completed_count == 0
    assert user_vm.todos_uncompleted_count == 100


# Данный тест проверяет, будет ли запись отчета
# у пользователя, не имеющего ни одного отчета
def test_vm_one_user_without_relationship():
    # arrange
    user_relation_1 = create_valid_user_json(1, 'name1', 'usname1')
    user_non_relation = create_valid_user_json(2, 'name2', 'usname2')
    user_relation_2 = create_valid_user_json(3, 'name3', 'usname3')

    todos_for_user_1 = create_valid_todos_json(5, 1)
    todos_for_user_2 = create_valid_todos_json(10, 3)

    # act
    todos = get_sorted_and_validated_todos(todos_for_user_1) + \
        get_sorted_and_validated_todos(todos_for_user_2)

    users = get_sorted_and_validated_users([user_relation_1, user_non_relation, user_relation_2])

    users_vm = get_users_vm_from_json(
        users=users, todos=todos)

    # assert
    assert users_vm is not None
    assert len(users_vm) == 2


def test_vm_zero_users_raises_except():
    valid_todos = create_valid_todos_json(100, 1)

    todos = get_sorted_and_validated_todos(valid_todos)
    users = get_sorted_and_validated_users([{}])

    try:
        _ = get_users_vm_from_json(
            users=users, todos=todos)
        assert False
    except StopIteration:
        assert True
