<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Order -->

* U本位合约
* 交易接口
* REST API
* 修改订单(TRADE)

本页总览

# 修改订单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Order#接口描述 "接口描述的直接链接")

修改订单功能，当前只支持限价（LIMIT）订单修改，修改后会在撮合队列里重新排序

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Order#http请求 "HTTP请求的直接链接")

PUT `/fapi/v1/order`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Order#请求权重 "请求权重的直接链接")

10s order rate limit(X-MBX-ORDER-COUNT-10S)为1;
1min order rate limit(X-MBX-ORDER-COUNT-1M)为1;
IP rate limit(x-mbx-used-weight-1m)为0

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Order#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| orderId | LONG | NO | 系统订单号 |
| origClientOrderId | STRING | NO | 用户自定义的订单号 |
| symbol | STRING | YES | 交易对 |
| side | ENUM | YES | 买卖方向 `SELL`, `BUY` |
| quantity | DECIMAL | YES | 下单数量,使用`closePosition`不支持此参数。 |
| price | DECIMAL | YES | 委托价格 |
| priceMatch | ENUM | NO | `OPPONENT`/ `OPPONENT_5`/ `OPPONENT_10`/ `OPPONENT_20`/`QUEUE`/ `QUEUE_5`/ `QUEUE_10`/ `QUEUE_20`；不能与price同时传 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * `orderId` 与 `origClientOrderId` 必须至少发送一个，同时发送则以 order id为准
> * `quantity` 与 `price` 均必须发送，这点和 dapi 修改订单不同
> * 当新订单的`quantity` 或 `price`不满足PRICE\_FILTER / PERCENT\_FILTER / LOT\_SIZE限制，修改会被拒绝，原订单依旧被保留
> * 订单会在下列情况下被取消：
>   + 原订单被部分执行且新订单`quantity` <= `executedQty`
>   + 原订单是`GTX`，新订单的价格会导致订单立刻执行
> * 同一订单修改次数最多10000次

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Order#响应示例 "响应示例的直接链接")

```
{  
 	"orderId": 20072994037,  
 	"symbol": "BTCUSDT",  
 	"pair": "BTCUSDT",  
 	"status": "NEW",  
 	"clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
 	"price": "30005",  
 	"avgPrice": "0.0",  
 	"origQty": "1",  
 	"executedQty": "0",  
 	"cumQty": "0",  
 	"cumBase": "0",  
 	"timeInForce": "GTC",  
 	"type": "LIMIT",  
 	"reduceOnly": false,  
 	"closePosition": false,  
 	"side": "BUY",  
 	"positionSide": "LONG",  
 	"stopPrice": "0",  
 	"workingType": "CONTRACT_PRICE",  
 	"priceProtect": false,  
 	"origType": "LIMIT",  
    "priceMatch": "NONE",              //盘口价格下单模式  
    "selfTradePreventionMode": "NONE", //订单自成交保护模式  
    "goodTillDate": 0,                 //订单TIF为GTD时的自动取消时间  
 	"updateTime": 1629182711600  
}
```

[上一页

批量下单(TRADE)](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Place-Multiple-Orders)[下一页

批量修改订单(TRADE)](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Multiple-Orders)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Order#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Order#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Order#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Order#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Modify-Order#响应示例)