<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders -->

* 统一账户
* 交易接口
* 查看当前全部UM挂单(USER-DATA)

本页总览

# 查看当前全部UM挂单(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#接口描述 "接口描述的直接链接")

查看当前全部UM挂单，请小心使用不带symbol参数的调用

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/openOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#请求权重 "请求权重的直接链接")

带symbol **1** - 不带 **40**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 不带`symbol`参数，会返回所有交易对的挂单

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#响应示例 "响应示例的直接链接")

```
[  
  {  
    "avgPrice": "0.00000",  
    "clientOrderId": "abc",  
    "cumQuote": "0",  
    "executedQty": "0",  
    "orderId": 1917641,  
    "origQty": "0.40",  
    "origType": "LIMIT",  
    "price": "0",  
    "reduceOnly": false,  
    "side": "BUY",  
    "positionSide": "SHORT",  
    "status": "NEW",  
    "symbol": "BTCUSDT",  
    "time": 1579276756075,              
    "timeInForce": "GTC",  
    "type": "LIMIT",  
    "updateTime": 1579276756075，  
    "selfTradePreventionMode": "NONE",   
    "goodTillDate": 0,  
    "priceMatch": "NONE"       
  }  
]
```

[上一页

查询当前UM挂单(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order)[下一页

查询UM所有条件订单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders#响应示例)