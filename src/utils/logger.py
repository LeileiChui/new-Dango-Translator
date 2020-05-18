# -*- coding: utf-8 -*-
# @Time : 2020/5/19 3:19
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : logger.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import logging.handlers
import os

time_level = 'S'
time_interval = 10
number_of_logs = 5


class Logger(logging.Logger):
    def __init__(self, filename=None):
        super(Logger, self).__init__(self)
        if not os.path.exists('logs'):
            os.makedirs('logs')
        # 日志文件名
        if filename is None:
            filename = './logs/logger.log'
        self.filename = filename

        # 创建一个handler，用于写入日志文件
        fh = logging.handlers.TimedRotatingFileHandler(self.filename, time_level, time_interval, number_of_logs, 'utf8')
        fh.suffix = "%Y-%m-%d_%H-%M-%S.log"
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s] - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.addHandler(fh)
        self.addHandler(ch)


logger = Logger()
# test
import time

if __name__ == '__main__':
    while True:
        time.sleep(1)
        logger.info("测试")
