<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp -->

* U本位合约
* Websocket账户信息推送
* Websocket API生成listenKey(USER-STREAM)

本页总览

# Websocket API生成listenKey (USER\_STREAM)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#接口描述 "接口描述的直接链接")

创建一个新的user data stream，返回值为一个listenKey，即websocket订阅的stream名称。如果该帐户具有有效的`listenKey`，则将返回该`listenKey`并将其有效期延长60分钟。

## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#方式 "方式的直接链接")

`userDataStream.start`

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#请求 "请求的直接链接")

```
{  
  "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",  
  "method": "userDataStream.start",  
  "params": {  
    "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"  
  }  
}
```

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| apiKey | STRING | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#响应示例 "响应示例的直接链接")

```
{  
  "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",  
  "status": 200,  
  "result": {  
    "listenKey": "xs0mRXdAKlIPDRFrlPcw0qI41Eh3ixNntmymGyhrhgqo7L6FuLaWArTD7RLP"  
  },  
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

关闭listenKey(USER-STREAM)](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Close-User-Data-Stream)[下一页

Websocket API延长listenKey有效期(USER-STREAM)](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Keepalive-User-Data-Stream-Wsp)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#接口描述)
* [方式](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#方式)
* [请求](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Start-User-Data-Stream-Wsp#响应示例)