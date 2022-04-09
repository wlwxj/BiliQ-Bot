# -*- codeing = utf-8 -*-

import requests
import json

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }


def group_message():
    group_url = 'http://127.0.0.1:5700/send_group_msg'
    data = {
        'group_id': '732633112',
        'message': 'test1',
    }

    resp = requests.post(url=group_url, data=data, headers=headers).json()

    print(resp)


def channel_message():
    channel_url = 'http://127.0.0.1:5700/send_guild_channel_msg'
    channel_data = {
        'guild_id': '93473511649415396',
        'channel_id': '4913181',
        'message': 'test',

    }
    resp = requests.post(url=channel_url, data=channel_data, headers=headers).json()
    print(resp)


if __name__ == '__main__':
    # group_message()
    channel_message()
