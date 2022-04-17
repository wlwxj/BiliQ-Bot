# -*- codeing = utf-8 -*-
# @Time : 2022/4/11 19:28
# @Author : D1ve_Wh4le
# @File : bilibili_api.py
# @Development Environment : PyCharm

from cgitb import text
import requests
import json
import re

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
dynamic_url = 'https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?'


def get_live_status(room_id):
    # 获取直播间状态
    live_url = 'https://api.live.bilibili.com/room/v1/Room/room_init?'
    live_param = {
        'id': room_id,
    }

    live_resp = requests.get(url=live_url, params=live_param, headers=headers).json()

    status = live_resp['data']['room_shield']

    # print(str(status))
    return int(status)


def get_newest_dynamic_type(uid):
    dynamic_param = {
        'visitor_uid':  '',
        'host_uid': uid,
        'offset_dynamic_id': '0',
        'need_top': '1',
        'platform': 'web',
    }

    dynamic_resp = requests.get(url=dynamic_url, params=dynamic_param, headers=headers).json()

    dynamic_type = dynamic_resp['data']['cards'][0]['desc']['type']
    return int(dynamic_type)


def dynamic_type_2(uid):
    ret = []
    dynamic_param = {
        'visitor_uid': '',
        'host_uid': uid,
        'offset_dynamic_id': '0',
        'need_top': '1',
        'platform': 'web',
    }

    dynamic_resp = requests.get(url=dynamic_url, params=dynamic_param, headers=headers).json()
    latest_dynamic = dynamic_resp['data']['cards'][0]['card']
    # print(latest_dynamic)

    text_obj = re.compile(r'"description":"(.*?)",', re.S)
    image_obj_png = re.compile(r'https:\\/\\/i0\.hdslb\.com\\/bfs\\/album\\/(.*?)\.png', re.S)
    image_obj_jpg = re.compile(r'https:\\/\\/i0\.hdslb\.com\\/bfs\\/album\\/(.*?)\.jpg', re.S)

    text = text_obj.findall(str(latest_dynamic))
    src = image_obj_png.findall(str(latest_dynamic))
    while src:
        image_url = 'https://i0.hdslb.com/bfs/album/' + src[0] + '.png'
        break
    else:
        src = image_obj_jpg.findall(str(latest_dynamic))
        image_url = 'https://i0.hdslb.com/bfs/album/' + src[0] + '.jpg'

    # print(text)
    # print(src)

    ret.append(text[0])
    ret.append(image_url)

    return ret


def dynamic_type_4(uid):
    dynamic_param = {
        'visitor_uid': '',
        'host_uid': uid,
        'offset_dynamic_id': '0',
        'need_top': '1',
        'platform': 'web',
    }
    dynamic_resp = requests.get(url=dynamic_url, params=dynamic_param, headers=headers).json()
    latest_dynamic = dynamic_resp['data']['cards'][0]['card']

    obj = re.compile(r'"content": "(.*?)", ', re.S)
    text = obj.findall(latest_dynamic)
    return text


def get_dynamic_id(uid):
    dynamic_param = {
        'visitor_uid': '',
        'host_uid': uid,
        'offset_dynamic_id': '0',
        'need_top': '1',
        'platform': 'web',
    }

    dynamic_resp = requests.get(url=dynamic_url, params=dynamic_param, headers=headers).json()
    # print(dynamic_resp)
    dynamic_id = dynamic_resp['data']['cards'][0]['desc']['dynamic_id']

    return dynamic_id


if __name__ == '__main__':
    print('no main!!')
