def check_title(todo_dict):
    if todo_dict['title'] == "":
        return False

    if len(todo_dict['title']) > 46:
        todo_dict['title'] = todo_dict['title'][0:46] + '…'

    return True


def check_user(user_dict):
    if user_dict['name'] == "" or \
            user_dict['username'] == "" or \
            user_dict['email'] == "" or \
            user_dict['companyName'] == "":
        return False
    return True


def ensure_user_have_required_variables(user):
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

    if not check_user(user_dict):
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

    if not check_title(todo_dict):
        return None, False

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
        val_user, is_created = ensure_user_have_required_variables(user)
        if is_created:
            sorted_users.append(val_user)

    return sorted(sorted_users, key=lambda d: d['id'])
