<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders -->

* 统一账户
* 交易接口
* 查询CM所有条件订单(USER\_DATA)

本页总览

# 查询CM所有条件订单(包括历史订单)(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders#接口描述 "接口描述的直接链接")

查询CM所有条件订单（包括历史订单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders#http请求 "HTTP请求的直接链接")

GET `/papi/v1/cm/conditional/allOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders#请求权重 "请求权重的直接链接")

带symbol**1**; 不带**40**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| strategyId | LONG | NO |  |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| limit | INT | NO | Default 500; max 1000. |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

**注意:**

* 请注意，如果订单满足如下条件，不会被查询到：
  + 订单的最终状态为 `CANCELED` 或者 `EXPIRED`, 并且
  + 订单没有任何的成交记录, 并且
  + 订单生成时间 + 3 天 < 当前时间
* 查询时间范围最大不得超过 7 天(默认查询最近 7 天内的数据).

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders#响应示例 "响应示例的直接链接")

```
[  
  {  
    newClientStrategyId: "abc",  
    strategyId: 123445,  
    strategyStatus: "TRIGGERED",  
    strategyType: "TRAILING_STOP_MARKET",  
    origQty: "0.40",  
    price: "0",  
    reduceOnly: false,  
    side: "BUY",  
    positionSide: "SHORT",  
    stopPrice: "9300",  
    symbol: "BTCUSD",  
    orderId: 12123343534, //条件单触发后普通单id，当条件单被触发后才有  
    status: "NEW", //条件单触发后普通单状态, 当条件单被触发后才有  
    bookTime: 1566818724710, //条件单下单时间  
    updateTime: 1566818724722,  
    triggerTime: 1566818724750,  
    timeInForce: "GTC",  
    type: "MARKET", //条件单触发后普通订单类型  
    activatePrice: "9020",  
    priceRate: "0.3",  
  },  
]
```

[上一页

查询CM当前条件挂单(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Current-CM-Open-Conditional-Order)[下一页

查询CM条件单历史(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Conditional-Order-History)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-All-CM-Conditional-Orders#响应示例)