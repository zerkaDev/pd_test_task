import json
import requests

from ApiWorker.validator import get_sorted_and_validated_todos, get_sorted_and_validated_users

from settings import TODOS_API_PATH, USERS_API_PATH

from ViewModels.user import User


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


def get_users_vm_from_json(users, todos):
    users_vm = []
    all_todos = []

    user = next(usr for usr in users if usr['id'] == todos[0]['userId'])

    for i in range(0, len(todos)):
        all_todos.append(todos[i])

        if i == len(todos) - 1:
            users_vm.append(get_user_vm(user, all_todos))
            break

        if todos[i]['userId'] != todos[i + 1]['userId']:
            users_vm.append(get_user_vm(user, all_todos))
            user = next(item for item in users if item['id'] == todos[i + 1]['userId'])
            all_todos = []

    return users_vm


def get_users_vm():
    users = get_users_from_json()
    todos = get_todos_from_json()

    return get_users_vm_from_json(users, todos)
