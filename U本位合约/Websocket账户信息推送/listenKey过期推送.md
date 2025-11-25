<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-User-Data-Stream-Expired -->

* U本位合约
* Websocket账户信息推送
* listenKey过期推送

本页总览

# listenKey过期推送

## 事件描述[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-User-Data-Stream-Expired#事件描述 "事件描述的直接链接")

当前连接使用的有效listenKey过期时，user data stream 将会推送此事件。

**注意:**

* 此事件与 websocket 连接中断没有必然联系
* 只有正在连接中的有效`listenKey`过期时才会收到此消息
* 收到此消息后 user data stream 将不再更新，直到用户使用新的有效的`listenKey`

## 事件类型[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-User-Data-Stream-Expired#事件类型 "事件类型的直接链接")

`listenKeyExpired`

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-User-Data-Stream-Expired#响应示例 "响应示例的直接链接")

```
{  
    "e": "listenKeyExpired",    // 事件类型  
    "E": "1736996475556",       // 事件时间  
    "listenKey":"WsCMN0a4KHUPTQuX6IUnqEZfB1inxmv1qR4kbf1LuEjur5VdbzqvyxqG9TSjVVxv"  
}
```

[上一页

Websocket API关闭listenKey(USER-STREAM)](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp)[下一页

Balance和Position更新推送](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Balance-and-Position-Update)

* [事件描述](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-User-Data-Stream-Expired#事件描述)
* [事件类型](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-User-Data-Stream-Expired#事件类型)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-User-Data-Stream-Expired#响应示例)