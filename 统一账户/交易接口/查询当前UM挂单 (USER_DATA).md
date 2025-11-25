<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order -->

* 统一账户
* 交易接口
* 查询当前UM挂单(USER-DATA)

本页总览

# 查询当前UM挂单 (USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#接口描述 "接口描述的直接链接")

查询当前UM挂单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/openOrder`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| orderId | LONG | NO |  |
| origClientOrderId | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

注意:

> * `orderId` 或 `origClientOrderId` 必须至少发送一个
> * 查询的订单如果已经成交或取消，将返回报错 "Order does not exist"

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#响应示例 "响应示例的直接链接")

```
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
    "time": 1579276756075,              // order time  
    "timeInForce": "GTC",  
    "type": "LIMIT",               
    "updateTime": 1579276756075，  
    "selfTradePreventionMode": "NONE", //self trading preventation mode  
    "goodTillDate": 0,  
    "priceMatch": "NONE"          
}
```

[上一页

查询所有UM订单(包括历史订单) (USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Orders)[下一页

查看当前全部UM挂单(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Order#响应示例)