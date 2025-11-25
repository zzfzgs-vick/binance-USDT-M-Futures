<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Order -->

* 统一账户
* 交易接口
* 撤销CM订单(TRADE)

本页总览

# 撤销CM订单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Order#接口描述 "接口描述的直接链接")

撤销CM订单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Order#http请求 "HTTP请求的直接链接")

DELETE `/papi/v1/cm/order`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Order#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| orderId | LONG | NO |  |
| origClientOrderId | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * `orderId` 或 `origClientOrderId` 必须至少发送一个

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Order#响应示例 "响应示例的直接链接")

```
{  
    "avgPrice": "0.0",  
    "clientOrderId": "myOrder1",  
    "cumQty": "0",  
    "cumBase": "0",  
    "executedQty": "0",  
    "orderId": 283194212,  
    "origQty": "2",  
    "price": "0",  
    "reduceOnly": false,  
    "side": "BUY",  
    "positionSide": "SHORT",    
    "status": "CANCELED",            
    "symbol": "BTCUSD_200925",  
    "pair": "BTCUSD",  
    "timeInForce": "GTC",  
    "type": "LIMIT",  
    "updateTime": 1571110484038,  
}
```

[上一页

取消全部UM条件单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders)[下一页

撤销全部CM订单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Orders)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Order#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Order#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Order#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Order#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Order#响应示例)