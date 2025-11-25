<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-UM-Order -->

* 统一账户
* 交易接口
* 修改UM订单(TRADE)

本页总览

# 修改UM订单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-UM-Order#接口描述 "接口描述的直接链接")

修改UM订单功能，当前只支持限价（LIMIT）订单修改，修改后会在撮合队列里重新排序

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-UM-Order#http请求 "HTTP请求的直接链接")

PUT `/papi/v1/um/order`

## 请求权重(Order)[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-UM-Order#请求权重order "请求权重(Order)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-UM-Order#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| orderId | LONG | NO | 系统订单号 |
| origClientOrderId | STRING | NO | 用户自定义的订单号 |
| symbol | STRING | YES | 交易对 |
| side | ENUM | YES | 买卖方向 `SELL`, `BUY`; `side`需要和原订单相同 |
| quantity | DECIMAL | YES | 下单数量 |
| price | DECIMAL | YES | 委托价格 |
| priceMatch | ENUM | NO | `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`；不能与price同时传 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 原订单被部分执行且新订单quantity <= executedQty 原订单是GTX，新订单的价格会导致订单立刻执行 同一订单修改次数最多10000次 改单会保留该单原有的selfTradePreventionMode
> * orderId 与 origClientOrderId 必须至少发送一个，同时发送则以 order id为准
> * quantity 与 price 均必须发送
> * 当新订单的 quantity 或 price 不满足PRICE\_FILTER / PERCENT\_FILTER / LOT\_SIZE限制，修改会被拒绝，原订单依旧被保留
> * 订单会在下列情况下被取消：
>   + 原订单被部分执行且新订单 quantity <= executedQty
>   + 原订单是GTX，新订单的价格会导致订单立刻执行
> * 同一订单修改次数最多10000次
> * 改单会保留该单原有的selfTradePreventionMode

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-UM-Order#响应示例 "响应示例的直接链接")

```
{  
    "orderId": 20072994037,  
    "symbol": "BTCUSDT",  
    "status": "NEW",  
    "clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
    "price": "30005",  
    "avgPrice": "0.0",  
    "origQty": "1",  
    "executedQty": "0",  
    "cumQty": "0",  
    "cumQuote": "0",  
    "timeInForce": "GTC",  
    "type": "LIMIT",  
    "reduceOnly": false,  
    "side": "BUY",  
    "positionSide": "LONG",  
    "origType": "LIMIT",  
    "selfTradePreventionMode": "NONE",   
    "goodTillDate": 0       
    "updateTime": 1629182711600,  
    "priceMatch": "NONE"  
}
```

[上一页

杠杆账户撤销单一交易对的所有挂单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol)[下一页

修改CM订单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-CM-Order)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-UM-Order#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-UM-Order#http请求)
* [请求权重(Order)](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-UM-Order#请求权重order)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-UM-Order#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-UM-Order#响应示例)