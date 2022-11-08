from ApiWorker.worker import get_users_vm
import ReportMaker.txt_writer


def start():
    users = get_users_vm()
    ReportMaker.txt_writer.run(users)


if __name__ == '__main__':
    start()
