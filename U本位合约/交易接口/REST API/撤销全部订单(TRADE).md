<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders -->

* U本位合约
* 交易接口
* REST API
* 撤销全部订单(TRADE)

本页总览

# 撤销全部订单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders#接口描述 "接口描述的直接链接")

撤销全部订单 (TRADE)

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders#http请求 "HTTP请求的直接链接")

DELETE `/fapi/v1/allOpenOrders`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES | 交易对 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders#响应示例 "响应示例的直接链接")

```
{  
	"code": 200,   
	"msg": "The operation of cancel all open order is done."  
}
```

[上一页

批量撤销订单(TRADE)](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-Multiple-Orders)[下一页

倒计时撤销所有订单(TRADE)](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Auto-Cancel-All-Open-Orders)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Cancel-All-Open-Orders#响应示例)