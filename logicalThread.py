# -*- coding: utf-8 -*-
# @Time : 2020/5/19 17:16
# @Author : Leilei Chui
# @Email : leilei.chui@gmail.com
# @File : logicalThread.py
# @Software: PyCharm
# -*- coding: utf-8 -*-

from PyQt5 import QtCore


class LogicalThread(QtCore.QThread):
    """
    逻辑处理线程
    """
    _signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(LogicalThread, self).__init__()
        self.task = None

    def set(self, task_func, callback_func):
        """
        设置线程任务
        :param task_func，线程任务函数
        :param callback_func: 回调函数
        :return: None
        """
        self.task = task_func
        self._signal.connect(callback_func)

    def run(self):
        self.task(self._signal)


# test
import time
import json


def task(signal: QtCore.pyqtSignal):
    """
    多线程任务函数
    :param signal: Qt信号
    :return: None
    """
    while True:
        time.sleep(1)
        signal.emit(json.dumps(time.time()))


def callback(params: str):
    """
    被逻辑线程回调的函数
    :param params: str, json
    :return: None
    """
    print(json.loads(params))


if __name__ == '__main__':
    thread = LogicalThread()
    thread.set(task_func=task, callback_func=callback)
    thread.run()
