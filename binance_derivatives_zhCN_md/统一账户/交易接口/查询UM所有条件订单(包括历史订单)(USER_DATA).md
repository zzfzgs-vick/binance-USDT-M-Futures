<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders -->

* 统一账户
* 交易接口
* 查询UM所有条件订单(TRADE)

本页总览

# 查询UM所有条件订单(包括历史订单)(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#接口描述 "接口描述的直接链接")

查询UM所有条件订单(包括历史订单)

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/conditional/allOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#请求权重 "请求权重的直接链接")

带symbol **1** ; 不带**40**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| strategyId | LONG | NO |  |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| limit | INT | NO | Default 500; max 1000. |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 请注意，如果订单满足如下条件，不会被查询到：
>   + 订单的最终状态为 `CANCELED` 或者 `EXPIRED`, 并且
>   + 订单没有任何的成交记录, 并且
>   + 订单生成时间 + 3 天 < 当前时间
> * 查询时间范围最大不得超过 7 天(默认查询最近 7 天内的数据).

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#响应示例 "响应示例的直接链接")

```
[  
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
    "orderId":12132343435,  //条件单触发后普通单id，当条件单被触发后才有     
    "status": "NEW",      //条件单触发后普通单状态, 当条件单被触发后才有         
    "bookTime": 1566818724710,      //条件单下单时间          
    "updateTime": 1566818724722,  
    "triggerTime": 1566818724750,    
    "timeInForce": "GTC",  
    "type": "MARKET",    //条件单触发后普通订单类型  
    "activatePrice": "9020",              
    "priceRate": "0.3",  
    "selfTradePreventionMode": "NONE", //self trading preventation mode  
    "goodTillDate": 0,  
    "priceMatch": "NONE"     
  }  
]
```

[上一页

查看当前全部UM挂单(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Orders)[下一页

查看UM当前全部条件挂单(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-UM-Conditional-Orders#响应示例)