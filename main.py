from utils import lock_instance, is_valid_interval, send_email


with lock_instance():
    is_valid_interval()
    send_email('poury.ms@gmail.com', 'test email', 'test content\ntest content')
