# -*- codeing = utf-8 -*-
# @Time : 2022/4/10 20:18
# @Author : D1ve_Wh4le
# @File : main.py.py
# @Development Environment : PyCharm

from bilibili_api import get_live_status, get_newest_dynamic_type, dynamic_type_2
import requests
import os

if __name__ == '__main__':
    # room_id = input()
    # print(get_live_status(room_id))

    uid = '43584648'
    # print(get_newest_dynamic_type(uid))
    print(dynamic_type_2(str(uid)))

