# coding:utf-8
import sys
import os


# 生成资源文件目录访问路径
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


if __name__ == '__main__':
    # 访问res文件夹下a.txt的内容
    filename = resource_path("config\config.json")
    print(filename)
    with open(filename, encoding='utf8') as f:
        lines = f.readlines()
        print(lines)
        f.close()
    input()

"""
pyinstaller 打包资源文件教程
https://www.cnblogs.com/darcymei/p/9397173.html

"""