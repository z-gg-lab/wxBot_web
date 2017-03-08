# coding: utf-8
from wxbot import *

# 创建新线程
thread_web = myThread(1, "Thread-web", 1)
thread_listener = myThread(2, "Thread-listener", 2)


if __name__ == '__main__':
    thread_web.start()
    thread_listener.start()