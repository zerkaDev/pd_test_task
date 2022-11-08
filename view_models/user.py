# Можно было бы использовать dataclass
class User:
    # Время устанавливаем только во время генерации отчета,
    # не при инициализации.
    def __init__(self,
                 username,
                 company_name,
                 fullname,
                 email,
                 todos):
        self.username = username
        self.company_name = company_name
        self.fullname = fullname
        self.email = email
        self.report_time = None
        self.todos = todos

    @property
    def todos_count(self):
        return len(self.todos)

    @property
    def completed_todos(self):
        return [todo for todo in self.todos if todo['completed'] is True]

    @property
    def uncompleted_todos(self):
        return [todo for todo in self.todos if todo['completed'] is False]

    @property
    def todos_completed_count(self):
        return len(self.completed_todos)

    @property
    def todos_uncompleted_count(self):
        return len(self.uncompleted_todos)
