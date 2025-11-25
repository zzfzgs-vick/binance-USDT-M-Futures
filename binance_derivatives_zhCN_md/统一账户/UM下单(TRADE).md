<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade -->

* 统一账户
* 交易接口
* UM下单(TRADE)

本页总览

# UM下单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade#接口描述 "接口描述的直接链接")

UM下单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade#http请求 "HTTP请求的直接链接")

POST `/papi/v1/um/order`

## 请求权重(Order)[​](/docs/zh-CN/derivatives/portfolio-margin/trade#请求权重order "请求权重(Order)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES | 交易对 |
| side | ENUM | YES | 方向 |
| positionSide | ENUM | NO | 持仓方向，单向持仓模式下非必填，默认且仅可填`BOTH`;在双向持仓模式下必填,且仅可选择 `LONG` 或 `SHORT` |
| type | ENUM | YES | `LIMIT`, `MARKET` |
| timeInForce | ENUM | NO | 有效方法 |
| quantity | DECIMAL | NO | 下单数量 |
| reduceOnly | STRING | NO | `true`或`false`; 非双开模式下默认false；双开模式下不接受此参数 |
| price | DECIMAL | NO | 委托价格 |
| newClientOrderId | STRING | NO | 用户自定义的订单号，不可以重复出现在挂单中。如空缺系统会自动赋值。必须满足正则规则: `^[\.A-Z\:/a-z0-9_-]{1,32}$` |
| newOrderRespType | ENUM | NO | `ACK`， `RESULT`，默认 `ACK` |
| priceMatch | ENUM | NO | `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`；不能与price同时传 |
| selfTradePreventionMode | ENUM | NO | NONE / EXPIRE\_TAKER/ EXPIRE\_MAKER/ EXPIRE\_BOTH； 默认NONE |
| goodTillDate | LONG | NO | TIF为GTD时订单的自动取消时间， 当timeInforce为GTD时必传；传入的时间戳仅保留秒级精度，毫秒级部分会被自动忽略，时间戳需大于当前时间+600s且小于253402300799000 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

根据 order `type`的不同，某些参数强制要求，具体如下:

| 类型 | 强制要求的参数 |
| --- | --- |
| `LIMIT` | `timeInForce`, `quantity`, `price` |
| `MARKET` | `quantity` |

> * `newOrderRespType` 如果传 `RESULT`:
>   + `MARKET` 订单将直接返回成交结果；
>   + 配合使用特殊 `timeInForce` 的 `LIMIT` 订单将直接返回成交或过期拒绝结果。
> * `selfTradePreventionMode` 仅在 `timeInForce`为`IOC`或`GTC`或`GTD`时生效.
> * 极端行情时，`timeInForce`为`GTD`的订单自动取消可能有一定延迟

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade#响应示例 "响应示例的直接链接")

```
{  
    "clientOrderId": "testOrder",  
    "cumQty": "0",  
    "cumQuote": "0",  
    "executedQty": "0",  
    "orderId": 22542179,  
    "avgPrice": "0.00000",  
    "origQty": "10",  
    "price": "0",  
    "reduceOnly": false,  
    "side": "BUY",  
    "positionSide": "SHORT",  
    "status": "NEW",  
    "symbol": "BTCUSDT",  
    "timeInForce": "GTD",  
    "type": "MARKET",  
    "selfTradePreventionMode": "NONE", ////订单自成交保护模式  
    "goodTillDate": 1693207680000,      //订单TIF为GTD时的自动取消时间   
    "updateTime": 1566818724722,  
    "priceMatch": "NONE"  
}
```

[上一页

测试服务器连通性PING](/docs/zh-CN/derivatives/portfolio-margin/market-data)[下一页

UM条件单下单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/New-UM-Conditional-Order)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade#http请求)
* [请求权重(Order)](/docs/zh-CN/derivatives/portfolio-margin/trade#请求权重order)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade#响应示例)