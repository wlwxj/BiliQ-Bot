# -*- codeing = utf-8 -*-
# @Time : 2022/4/10 20:18
# @Author : D1ve_Wh4le
# @File : main.py.py
# @Development Environment : PyCharm

from bilibili_api import get_live_status, get_newest_dynamic_type, dynamic_type_2, get_dynamic_id
from test import group_message, channel_message
import requests
import os

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'token': '114514',
    }


if __name__ == '__main__':
    # room_id = input()
    # print(get_live_status(room_id))

    uid = '1437582453'
    # print(get_newest_dynamic_type(uid))
    # print(dynamic_type_2(str(uid)))
    # print(get_dynamic_id(str(uid)))
    msg = uid+'发送了动态\n'+str(dynamic_type_2(str(uid))[0])+'[CQ:image,file='+str(dynamic_type_2(str(uid))[1])+',type=show]'

    print(channel_message(msg))
