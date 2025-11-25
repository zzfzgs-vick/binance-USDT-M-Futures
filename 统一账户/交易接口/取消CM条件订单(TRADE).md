<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Conditional-Order -->

* 统一账户
* 交易接口
* 取消CM条件订单(TRADE)

本页总览

# 取消CM条件订单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Conditional-Order#接口描述 "接口描述的直接链接")

取消CM条件订单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Conditional-Order#http请求 "HTTP请求的直接链接")

DELETE `/papi/v1/cm/conditional/order`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Conditional-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Conditional-Order#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| strategyId | LONG | NO |  |
| newClientStrategyId | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * `strategyId` 与 `newClientStrategyId` 之一必须发送

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Conditional-Order#响应示例 "响应示例的直接链接")

```
{  
    "newClientStrategyId": "myOrder1",  
    "strategyId":123445,  
    "strategyStatus":"CANCELED",  
    "strategyType": "TRAILING_STOP_MARKET",    
    "origQty": "11",  
    "price": "0",  
    "reduceOnly": false,  
    "side": "BUY",  
    "positionSide": "SHORT",  
    "stopPrice": "9300",                 
    "symbol": "BTCUSD",  
    "timeInForce": "GTC",  
    "activatePrice": "9020",             
    "priceRate": "0.3",                   
    "updateTime": 1566818724722,  
    "workingType":"CONTRACT_PRICE",  
    "priceProtect": false     
}
```

[上一页

撤销全部CM订单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Orders)[下一页

取消全部CM条件单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Conditional-Orders)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Conditional-Order#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Conditional-Order#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Conditional-Order#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Conditional-Order#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Conditional-Order#响应示例)