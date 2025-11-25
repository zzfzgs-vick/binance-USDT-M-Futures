<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage -->

* U本位合约
* 交易接口
* REST API
* 调整开仓杠杆(TRADE)

本页总览

# 调整开仓杠杆 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#接口描述 "接口描述的直接链接")

调整用户在指定symbol合约的开仓杠杆。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#http请求 "HTTP请求的直接链接")

POST `/fapi/v1/leverage`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES | 交易对 |
| leverage | INT | YES | 目标杠杆倍数：1 到 125 整数 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#响应示例 "响应示例的直接链接")

```
{  
 	"leverage": 21,	// 杠杆倍数  
 	"maxNotionalValue": "1000000", // 当前杠杆倍数下允许的最大名义价值  
 	"symbol": "BTCUSDT"	// 交易对  
}
```

[上一页

更改持仓模式(TRADE)](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Position-Mode)[下一页

更改联合保证金模式(TRADE)](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Multi-Assets-Mode)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Initial-Leverage#响应示例)