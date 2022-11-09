import json
import requests

from api_worker.validator import get_sorted_and_validated_todos,\
    get_sorted_and_validated_users

from settings import TODOS_API_PATH, USERS_API_PATH

from view_models.user import User


def get_users_from_json():
    api_response = requests.get(USERS_API_PATH)
    users = json.loads(api_response.text)

    return get_sorted_and_validated_users(users)


def get_todos_from_json():
    api_response = requests.get(TODOS_API_PATH)
    todos = json.loads(api_response.text)

    return get_sorted_and_validated_todos(todos)


def get_user_vm(user, all_todos):
    return User(
        user['username'],
        user['companyName'],
        user['name'],
        user['email'],
        all_todos)


def get_first_or_next_user(users, todos, i=0):
    try:
        return next(usr for usr in users if usr['id'] == todos[i]['userId'])
    except StopIteration as e:
        print('Юзеров нет, программа останавливает свое выполнение')
        raise e


# Почему такой подход? Мне кажется, что пройтись 1 раз по всем
# задачам и искать юзера только при смене userId быстрее, чем
# подтягивать задачи отталкиваясь от юзера. В случае подтягивания
# с юзера, прийдется каждый раз обходить ВСЕ todos, а их в 20 раз больше.
# А данный метод будет обходить всех юзеров только при условии, что userId
# поменялся. Такой подход быстрее при условии отсортированного набора
# входных данных, и, если сервер гарантирует сортировку, то этот подход лучше,
# однако если данные различны, 1 способ окажется эффективнее
def get_users_vm_from_json(users, todos):
    users_vm = []
    all_todos = []

    # Может вылететь indexOutOfArray
    user = get_first_or_next_user(users, todos)

    for i in range(0, len(todos)):
        all_todos.append(todos[i])

        if i == len(todos) - 1:
            users_vm.append(get_user_vm(user, all_todos))
            break

        if todos[i]['userId'] != todos[i + 1]['userId']:
            users_vm.append(get_user_vm(user, all_todos))
            user = get_first_or_next_user(users, todos, i+1)
            all_todos = []

    return users_vm


def get_users_vm():
    users = get_users_from_json()
    todos = get_todos_from_json()

    return get_users_vm_from_json(users, todos)
