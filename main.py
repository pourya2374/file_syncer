from utils import lock_instance

from time import sleep


with lock_instance():
    while True:
        print('hello')
        sleep(1)
