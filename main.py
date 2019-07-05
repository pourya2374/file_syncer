from utils import lock_instance, is_valid_interval, send_email, list_files_with_size, rsync, is_changed
from configs import SERVER_NAME, SERVER_PATH, LOCAL_PATH


with lock_instance():
    is_valid_interval()

    rsync(
        '{}:{}'.format(SERVER_NAME, SERVER_PATH),
        LOCAL_PATH
    )

    files = list_files_with_size(LOCAL_PATH)
    msg = ''
    for file in files:
        msg += '\n{}. {} -> {}'.format(*file)

    if is_changed(msg):
        send_email(
            'poury.ms@gmail.com',
            'Sync home with server',
            'Downloaded list: \n{}'.format(msg)
        )
    else:
        print('there is no change!')
