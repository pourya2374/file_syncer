import socket

DEBUG = socket.gethostname() != 'home'

START_HOUR = 2
STOP_HOUR = 7

SERVER_NAME = 'keylid1'
SERVER_PATH = '/tmp/movie/'

if DEBUG:
    LOCAL_PATH = '/home/pourya/Downloads/'
else:
    LOCAL_PATH = '/home/pourya/Downloads/movie/'
