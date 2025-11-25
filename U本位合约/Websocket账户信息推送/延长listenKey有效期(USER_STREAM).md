<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Keepalive-User-Data-Stream -->

* U本位合约
* Websocket账户信息推送
* 延长listenKey有效期(USER-STREAM)

本页总览

# 延长listenKey有效期(USER\_STREAM)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Keepalive-User-Data-Stream#接口描述 "接口描述的直接链接")

有效期延长至本次调用后60分钟

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Keepalive-User-Data-Stream#http请求 "HTTP请求的直接链接")

PUT `/fapi/v1/listenKey`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Keepalive-User-Data-Stream#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Keepalive-User-Data-Stream#请求参数 "请求参数的直接链接")

None

```
{  
    "listenKey": "3HBntNTepshgEdjIwSUIBgB9keLyOCg5qv3n6bYAtktG8ejcaW5HXz9Vx1JgIieg" // 被延长的listenkey  
}
```

[上一页

生成listenKey(USER-STREAM)](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream)[下一页

关闭listenKey(USER-STREAM)](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Keepalive-User-Data-Stream#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Keepalive-User-Data-Stream#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Keepalive-User-Data-Stream#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Keepalive-User-Data-Stream#请求参数)