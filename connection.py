from pymodm import connect
import os


def connection():
    connect('mongodb://' + os.environ['username'] + ":" + os.environ['password'] + "@" + os.environ['db_host'] + ':' + os.environ['db_port'] + '/tankStory')
