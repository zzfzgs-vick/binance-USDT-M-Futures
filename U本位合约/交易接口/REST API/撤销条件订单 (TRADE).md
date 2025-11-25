<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order -->

* U本位合约
* 交易接口
* REST API
* 撤销条件订单 (TRADE)

本页总览

# 撤销条件订单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#接口描述 "接口描述的直接链接")

撤销条件订单

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#http请求 "HTTP请求的直接链接")

DELETE `/fapi/v1/algoOrder`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| algoid | LONG | NO | 系统订单号 |
| clientalgoid | STRING | NO | 用户自定义的订单号 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * `algoid` 与 `clientalgoid` 必须至少发送一个

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#响应示例 "响应示例的直接链接")

```
{  
   "algoId": 2146760,  
   "clientAlgoId": "6B2I9XVcJpCjqPAJ4YoFX7",  
   "code": "200",  
   "msg": "success"  
}
```

[上一页

下条件单 (TRADE)](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/New-Algo-Order)[下一页

撤销全部订单 (TRADE)](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Algo-Open-Orders)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Algo-Order#响应示例)