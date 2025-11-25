<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order -->

* 统一账户
* 交易接口
* 查询UM当前条件挂单(USER-DATA)

本页总览

# 查询UM当前条件挂单(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#接口描述 "接口描述的直接链接")

查询UM当前条件挂单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/conditional/openOrder`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| strategyId | LONG | NO |  |
| newClientStrategyId | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

注意:

> * `strategyId` 与 `newClientStrategyId` 中的一个为必填参数.
> * 如果查询的条件单已经为`CANCELED`， `TRIGGERED`或`EXPIRED`，会报错"Order does not exist"

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#响应示例 "响应示例的直接链接")

```
{              
    "newClientStrategyId": "abc",   
    "strategyId":123445,  
    "strategyStatus":"NEW",  
    "strategyType": "TRAILING_STOP_MARKET",                                  
    "origQty": "0.40",                        
    "price": "0",  
    "reduceOnly": false,  
    "side": "BUY",  
    "positionSide": "SHORT",  
    "stopPrice": "9300",                 
    "symbol": "BTCUSDT",  
    "bookTime": 1566818724710,       //条件单下单时间          
    "updateTime": 1566818724722,  
    "timeInForce": "GTC",  
    "activatePrice": "9020",             
    "priceRate": "0.3",  
    "selfTradePreventionMode": "NONE",  
    "goodTillDate": 0,  
    "priceMatch": "NONE"                       
}
```

[上一页

查看UM当前全部条件挂单(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-Current-UM-Open-Conditional-Orders)[下一页

查询UM条件单历史(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Conditional-Order-History)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-UM-Open-Conditional-Order#响应示例)