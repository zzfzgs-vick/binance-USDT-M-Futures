<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Conditional-Order-History -->

* 统一账户
* 交易接口
* 查询UM条件单历史(USER-DATA)

本页总览

# 查询UM条件单历史(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Conditional-Order-History#接口描述 "接口描述的直接链接")

查询UM条件单历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Conditional-Order-History#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/conditional/orderHistory`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Conditional-Order-History#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Conditional-Order-History#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| strategyId | LONG | NO |  |
| newClientStrategyId | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

**注意:**

* `strategyId` 与 `newClientStrategyId` 中的一个为必填参数.
* `NEW` 状态的条件订单不会返回
* 请注意，如果订单满足如下条件，不会被查询到：
  + 订单的最终状态为 `CANCELED` 或者 `EXPIRED`, 并且
  + 订单没有任何的成交记录, 并且
  + 订单生成时间 + 3天 < 当前时间

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Conditional-Order-History#响应示例 "响应示例的直接链接")

```
{  
    "newClientStrategyId": "abc",   
    "strategyId":123445,  
    "strategyStatus":"TRIGGERED",  
    "strategyType": "TRAILING_STOP_MARKET",    
    "origQty": "0.40",  
    "price": "0",  
    "reduceOnly": false,  
    "side": "BUY",  
    "positionSide": "SHORT",  
    "stopPrice": "9300",                 
    "symbol": "BTCUSDT",   
    "orderId":12132343435,   //条件单触发后普通单id，当条件单被触发后才有  
    "status": "NEW",     //条件单触发后普通单状态, 当条件单被触发后才有      
    "bookTime": 1566818724710,    //条件单下单时间              
    "updateTime": 1566818724722,  
    "triggerTime": 1566818724750,    
    "timeInForce": "GTC",  
    "type": "MARKET",   //条件单触发后普通订单类型  
    "activatePrice": "9020",             
    "priceRate": "0.3",      
    "workingType":"CONTRACT_PRICE",  
    "priceProtect": false,  
    "selfTradePreventionMode": "NONE", //self trading preventation mode  
    "goodTillDate": 0                 
}
```

[上一页

查询UM当前条件挂单(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order)[下一页

查询CM订单(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Order)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Conditional-Order-History#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Conditional-Order-History#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Conditional-Order-History#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Conditional-Order-History#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Conditional-Order-History#响应示例)