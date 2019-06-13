from contextlib import contextmanager
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

from zc.lockfile import LockError, LockFile
import pytz
import sh

from configs import START_HOUR, STOP_HOUR, DEBUG
from secrets import GMAIL_PASSWORD, GMAIL_USERNAME


my_sh = sh(_env={"PATH": "/usr/local/bin:/bin:/usr/bin"})


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


def send_email(to, subject, content):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = GMAIL_USERNAME
    msg['To'] = to

    part = MIMEText(content, 'plain')
    msg.attach(part)

    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.login(GMAIL_USERNAME, GMAIL_PASSWORD)
    s.sendmail(GMAIL_USERNAME, to, msg.as_string())
    s.quit()


def list_of_files(path: str) -> list:
    path_obj = Path(path)
    return [item.name for item in path_obj.iterdir() if item.is_file()]


def rsync(source_path: str, destination_path: str):
    my_sh.rsync("-rahtze", "ssh", "--progress", source_path, destination_path)


if __name__ == '__main__':
    # for testing purpose
    pass
