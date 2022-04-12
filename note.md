#相关参数,资料
##1. 哔哩哔哩动态API

####url:
>e.g.:https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?visitor_uid=85580050&host_uid=43584648&offset_dynamic_id=632663891261784065&need_top=1&platform=web

>https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?

- 请求方法:get

 | 参数                | 值         |
|-------------------|-----------|
| visitor_uid       | 85580050  |
| host_uid          | 628288620 |
 | offset_dynamic_id | 0         |
 | need_top          | 1         |
 | platform          | web       |

| 参数                | 值             |
|-------------------|---------------|
 | visitor_uid       | 访问者uid        |
 | host_uid          | 访问对象uid       |
 | offset_dynamic_id | 上次最后一条动态的动态id |
 | need_top          | 1             |
 | platform          | web           |

----
##2. 哔哩哔哩直播状态API
####url:
>http://api.live.bilibili.com/room/v1/Room/room_init?id=22816111

>http://api.live.bilibili.com/room/v1/Room/room_init?
- 请求方法:get

| 参数  | 值      |
|-----|--------|
| id  | 查询对象id |

返回数据(JSON)

| 键         | 值                                                                                                                                                                                                                                                                                               |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| "code"    | 0,                                                                                                                                                                                                                                                                                              |
| "msg"     | "ok",                                                                                                                                                                                                                                                                                           |
| "message" | "ok",                                                                                                                                                                                                                                                                                           |
| "data"    | {"room_id": 22816111,"short_id": 0,"uid": 1437582453,"need_p2p": 0,"is_hidden": false,"is_locked": false,"is_portrait": false,"live_status": 2,"hidden_till": 0,"lock_till": 0,"encrypted": false,"pwd_verified": false,"live_time": -62170012800,"room_shield": 1,"is_sp": 0,"special_type": 0 |

其中的data字段

| 键              | 值            |
|----------------|--------------|
| "room_id"      | 22816111     |
| "short_id"     | 0            |
| "uid"          | 1437582453   |
| "need_p2p"     | 0            |
| "is_hidden"    | false        |
| "is_locked"    | false        |
| "is_portrait"  | false        |
| "live_status"  | 2            |
| "hidden_till"  | 0            |
| "lock_till"    | 0            |
| "encrypted"    | false        |
| "pwd_verified" | false        |
| "live_time"    | -62170012800 |
| "room_shield"  | 1 (直播间状态 )   |
| "is_sp"        | 0            |
| "special_type" | 0            |
----
>http://127.0.0.1:5700/send_guild_channel_msg?&guild_id=93473511649415396&channel_id=4913181&message=channel_msg

##动态类型

| id  | 类型    |
|-----|-------|
| 8   | 投稿视频  |
| 2   | 图片+文字 |
| 4   | 纯文字   |