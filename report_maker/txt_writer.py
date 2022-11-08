from datetime import datetime
import os
from sys import platform

from report_maker.report import get_full_report
from settings import CURRENT_DIR

TASKS_DIR_PATH = path = os.path.join(CURRENT_DIR, 'tasks')


def get_txt_time_format(string_time):
    full_date = string_time.split(' ')
    date = full_date[0].split('.')
    time = full_date[1].split(':')

    sep = '-'
    # Выбрасывает win error 87 если в названии файла есть символ ':'
    if platform == 'linux':
        sep = ':'

    return f'{date[2]}-{date[1]}-{date[0]}T{time[0]}{sep}{time[1]}'


def get_report_time(file_path):
    with open(f'{file_path}.txt', 'r', encoding='utf-8') as file:
        line = file.read().split('\n')[1]
        line = line[line.find('>') + 2:]

        return get_txt_time_format(line)


def check_is_report_exist(file_path, username):
    if os.path.exists(f'{file_path}.txt'):
        new_file_name = os.path.join(TASKS_DIR_PATH, f"old_{username}_{get_report_time(file_path)}.txt")

        try:
            os.rename(f'{file_path}.txt', new_file_name)
        except FileExistsError:
            os.remove(new_file_name)
            os.rename(f'{file_path}.txt', new_file_name)


# Отчет обязан в названии иметь час и минуту создания
# однако, при таком условии, невозможно будет создать
# два отчета в один определенный час и минуту.

# Для решения этой проблемы можно использовать более точную дату,
# или использовать uuid. Я просто пересоздаю файл
def create_or_update_report(user):
    user_report_path = os.path.join(TASKS_DIR_PATH, user.username)
    check_is_report_exist(user_report_path, user.username)
    with open(f'{user_report_path}.txt', 'w', encoding='utf-8') as file:
        file.write(get_full_report(user))


def run(users):
    ensure_dir_created()

    for user in users:
        now = datetime.now()
        user.report_time = f"{now.day}.{now.month}.{now.year} {now.hour}:{now.minute}"
        create_or_update_report(user)


def ensure_dir_created():
    os.makedirs(TASKS_DIR_PATH, exist_ok=True)
