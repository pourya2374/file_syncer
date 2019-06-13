from utils import lock_instance, is_valid_interval


with lock_instance():
    is_valid_interval()
