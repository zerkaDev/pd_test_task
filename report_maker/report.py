def get_full_report(user):
    report = f'# Отчёт для {user.company_name}.\n'
    report = ''.join([report, f'{user.fullname} <{user.email}> {user.report_time}\n'])
    report = ''.join([report, f'Всего задач: {user.todos_count}\n'])
    report = ''.join([report, '\n'])

    report = ''.join([report, f'## Актуальные задачи ({user.todos_uncompleted_count}):\n'])
    report = ''.join([report, get_tasks_report(user.uncompleted_todos)])

    report = ''.join([report, '\n'])
    report = ''.join([report, f'## Завершённые  задачи ({user.todos_completed_count}):\n'])
    report = ''.join([report, get_tasks_report(user.completed_todos)])

    return report


def get_tasks_report(tasks):
    report = ''

    for task in tasks:
        title = task['title']
        report = ''.join([report, f'- {title}\n'])

    return report
