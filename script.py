import logging
import sys

from api_worker.worker import get_users_vm
import report_maker.txt_writer

log = logging.getLogger()
log.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)


def start():
    log.debug("Script starts")

    users = get_users_vm()

    log.debug(f"{len(users)} users and "
              f"{sum(len(todo) for todo in (user.todos for user in users))} todos was added")

    log.debug("Writing...")

    report_maker.txt_writer.run(users)


if __name__ == '__main__':
    start()
