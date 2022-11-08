def check_title(todo_dict):
    if len(todo_dict['title']) > 46:
        todo_dict['title'] = todo_dict['title'][0:46] + '…'


def ensure_user_have_relation_and_required_variables(user):
    try:
        user_dict = {
            'id': user['id'],
            'name': user['name'],
            'username': user['username'],
            'email': user['email'],
            'companyName': user['company']['name'],
        }
    except KeyError:
        return None, False

    return user_dict, True


def ensure_todo_have_relation_and_required_variables(todo):
    try:
        todo_dict = {
            'userId': todo['userId'],
            'title': todo['title'],
            'completed': todo['completed'],
        }
    except KeyError:
        return None, False

    check_title(todo_dict)

    return todo_dict, True


def get_sorted_and_validated_todos(todos: list[dict]):
    sorted_todos = []

    for todo in todos:
        val_todo, is_created = ensure_todo_have_relation_and_required_variables(todo)
        if is_created:
            sorted_todos.append(val_todo)

    return sorted(sorted_todos, key=lambda d: d['userId'])


def get_sorted_and_validated_users(users: list[dict]):
    sorted_users = []

    for user in users:
        val_user, is_created = ensure_user_have_relation_and_required_variables(user)
        if is_created:
            sorted_users.append(val_user)

    return sorted(sorted_users, key=lambda d: d['id'])
