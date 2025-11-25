<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp -->

* U本位合约
* Websocket账户信息推送
* Websocket API关闭listenKey(USER-STREAM)

本页总览

# Websocket API关闭listenKey (USER\_STREAM)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#接口描述 "接口描述的直接链接")

关闭某账户数据流

## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#方式 "方式的直接链接")

`userDataStream.stop`

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#请求 "请求的直接链接")

```
{  
  "id": "819e1b1b-8c06-485b-a13e-131326c69599",  
  "method": "userDataStream.stop",  
  "params": {  
    "apiKey": "vmPUZE6mv9SD5VNHk9HlWFsOr9aLE2zvsw0MuIgwCIPy8atIco14y7Ju91duEh8A"  
  }  
}
```

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#请求参数 "请求参数的直接链接")

None

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#响应示例 "响应示例的直接链接")

```
{  
  "id": "819e1b1b-8c06-485b-a13e-131326c69599",  
  "status": 200,  
  "result": {},  
   "rateLimits": [  
    {  
      "rateLimitType": "REQUEST_WEIGHT",  
      "interval": "MINUTE",  
      "intervalNum": 1,  
      "limit": 2400,  
      "count": 2  
    }  
  ]  
}
```

[上一页

Websocket API延长listenKey有效期(USER-STREAM)](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp)[下一页

listenKey过期推送](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-User-Data-Stream-Expired)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#接口描述)
* [方式](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#方式)
* [请求](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream-Wsp#响应示例)