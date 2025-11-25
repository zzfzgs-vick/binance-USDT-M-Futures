<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream -->

* 统一账户
* Websocket账户信息推送
* 生成listenKey(USER-STREAM)

本页总览

# 生成listenKey(USER\_STREAM)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#接口描述 "接口描述的直接链接")

创建一个新的user data stream，返回值为一个listenKey，即websocket订阅的stream名称。如果该帐户具有有效的`listenKey`，则将返回该`listenKey`并将其有效期延长60分钟。

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#http请求 "HTTP请求的直接链接")

POST `/papi/v1/listenKey`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#请求参数 "请求参数的直接链接")

**None**

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#响应示例 "响应示例的直接链接")

```
{  
  "listenKey": "pqia91ma19a5s61cv6a81va65sdf19v8a65a1a5s61cv6a81va65sdf19v8a65a1"  
}
```

[上一页

账户信息流连接](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams)[下一页

延长listenKey有效期(USER-STREAM)](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Keepalive-User-Data-Stream)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Start-User-Data-Stream#响应示例)