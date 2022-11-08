from api_worker.worker import get_users_vm
import report_maker.txt_writer


def start():
    users = get_users_vm()
    report_maker.txt_writer.run(users)


if __name__ == '__main__':
    start()
