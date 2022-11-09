import json
import random


def create_non_valid_todo_json(id, user_id):
    val = '{ "id": ' + str(id) + ', "userId": ' + str(user_id) + \
          ', "completed": false }'
    return json.loads(val)


def create_non_valid_todos_json(count, user_id):
    todos = []
    for i in range(0, count):
        todos.append(create_non_valid_todo_json(random.randint(1, 50), user_id))
    return todos


def create_valid_todos_json(count, user_id):
    todos = []
    for i in range(0, count):
        todos.append(create_valid_todo_json(random.randint(1, 50), user_id))
    return todos


def create_valid_todo_json(id, user_id):
    val = '{ "id": ' + str(id) + ', "userId": ' + str(user_id) + \
          ', "title": "tiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiitle",' \
          ' "completed": false }'
    return json.loads(val)


def create_non_valid_user_json(id):
    val = '{ "id": ' + str(id) + \
          ', "name": "name", "email": "a@a.ru", "company": { "name": "cmp name" } }'
    return json.loads(val)


def create_non_valid_user_by_values_json(id):
    val = '{ "id": ' + str(id) + \
          ', "name": "", "email": "a@a.ru", "company": { "name": "cmp name" } }'
    return json.loads(val)


def create_non_valid_users_json(count):
    users = []
    for i in range(0, count):
        users.append(create_non_valid_user_json(random.randint(1, 50)))
    return users


def create_valid_user_json(id, name='name', username='usname'):
    val = '{ "id": ' + str(id) + \
          ', "name": "' + str(name) + '", ' \
          '"username": "' + str(username) + '", ' \
          '"email": "a@a.ru", ' \
          '"company": { "name": "cmp name" } }'
    return json.loads(val)


def create_valid_users_json(count):
    users = []
    for i in range(0, count):
        users.append(create_valid_user_json(random.randint(1, 50)))
    return users
