<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config -->

* 统一账户
* 账户接口
* UM合约交易对配置(USER-DATA)

本页总览

# 交易对配置 (USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#接口描述 "接口描述的直接链接")

查询UM合约交易对上的基础配置

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/symbolConfig`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | NO | 交易对 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#响应示例 "响应示例的直接链接")

```
[  
  {  
  "symbol": "BTCUSDT",   
  "marginType": "CROSSED",  
  "isAutoAddMargin": "false",  
  "leverage": 21,  
  "maxNotionalValue": "1000000",  
  }  
]
```

[上一页

UM账户配置(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config)[下一页

获取UM账户信息V2(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Account-Detail-V2)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Symbol-Config#响应示例)