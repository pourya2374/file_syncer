from utils import lock_instance, is_valid_interval, send_email, list_of_files, rsync
from configs import SERVER_NAME, SERVER_PATH, LOCAL_PATH


with lock_instance():
    is_valid_interval()

    rsync(
        '{}:{}'.format(SERVER_NAME, SERVER_PATH),
        LOCAL_PATH
    )

    file_names = list_of_files(LOCAL_PATH)
    send_email('poury.ms@gmail.com', 'Sync home with server', 'Downloaded list: \n\n{}'.format('\n'.join(file_names)))
