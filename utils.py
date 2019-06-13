from contextlib import contextmanager
from datetime import datetime

from zc.lockfile import LockError, LockFile
import pytz

from configs import START_HOUR, STOP_HOUR, DEBUG


@contextmanager
def lock_instance():
    try:
        lock = LockFile('file_syncer.lock')
    except LockError:
        print('Can not run multiple instance of this script. Try it later! :)')
        exit()
    yield
    lock.close()


def is_valid_interval():
    if DEBUG:
        return
    d = datetime.now()
    timezone = pytz.timezone("Asia/Tehran")
    d_aware = timezone.localize(d)
    if START_HOUR <= d_aware.hour < STOP_HOUR:
        return
    else:
        print("It's not good time to sync files! :)")
        exit()


if __name__ == '__main__':
    # for testing purpose
    pass
