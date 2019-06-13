from contextlib import contextmanager

from zc.lockfile import LockError, LockFile


@contextmanager
def lock_instance():
    try:
        lock = LockFile('file_syncer.lock')
    except LockError:
        print('Can not run multiple instance of this script. Try it later! :)')
        exit()
    yield
    lock.close()


if __name__ == '__main__':
    # for testing purpose
    pass
