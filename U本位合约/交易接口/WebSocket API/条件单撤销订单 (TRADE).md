<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order -->

* U本位合约
* 交易接口
* WebSocket API
* 条件单撤销订单(TRADE)

本页总览

# 条件单撤销订单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#接口描述 "接口描述的直接链接")

撤销条件订单

## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#方式 "方式的直接链接")

`algoOrder.cancel`

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#请求 "请求的直接链接")

```
{  
   	"id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",  
    "method": "algoOrder.cancel",   
    "params": {   
      "apiKey": "HsOehcfih8ZRxnhjp2XjGXhsOBd6msAhKz9joQaWwZ7arcJTlD2hGOGQj1lGdTjR",   
      "algoId": 283194212,   
      "clientalgoid": "DolwRKnQNjoc1E9Bbh03ER",  
      "timestamp": 1703439070722,   
      "signature": "b09c49815b4e3f1f6098cd9fbe26a933a9af79803deaaaae03c29f719c08a8a8"   
    }  
}
```

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| algoid | LONG | NO | 系统订单号 |
| clientalgoid | STRING | NO | 用户自定义的订单号 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * `algoid` 与 `clientalgoid` 必须至少发送一个

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#响应示例 "响应示例的直接链接")

```
{  
  "id": "06c9dbd8-ccbf-4ecf-a29c-fe31495ac73f",  
  "status": 200,  
  "result": {  
    "algoId": 3000000000003505,  
    "clientAlgoId": "0Xkl1p621E4EryvufmYre1",  
    "algoType": "CONDITIONAL",  
    "orderType": "TAKE_PROFIT",  
    "symbol": "BTCUSDT",  
    "side": "SELL",  
    "positionSide": "SHORT",  
    "timeInForce": "GTC",  
    "quantity": "1.000",  
    "algoStatus": "CANCELED",  
    "triggerPrice": "120000.00",  
    "price": "160000.00",  
    "icebergQuantity": null,  
    "selfTradePreventionMode": "EXPIRE_MAKER",  
    "workingType": "CONTRACT_PRICE",  
    "priceMatch": "NONE",  
    "closePosition": false,  
    "priceProtect": false,  
    "reduceOnly": false,  
    "createTime": 1762507264142,  
    "updateTime": 1762507264143,  
    "triggerTime": 0,  
    "goodTillDate": 0  
  },  
  "rateLimits": [  
    {  
      "rateLimitType": "REQUEST_WEIGHT",  
      "interval": "MINUTE",  
      "intervalNum": 1,  
      "limit": 2400,  
      "count": 1  
    }  
  ]  
}
```

[上一页

条件单下单(TRADE)](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/New-Algo-Order)[下一页

市场数据连接](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#接口描述)
* [方式](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#方式)
* [请求](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/trade/websocket-api/Cancel-Algo-Order#响应示例)