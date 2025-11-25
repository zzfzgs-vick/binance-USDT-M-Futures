<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders -->

* U本位合约
* 交易接口
* REST API
* 查看当前全部条件挂单(USER-DATA)

本页总览

# 查看当前全部条件挂单 (USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#接口描述 "接口描述的直接链接")

查看当前全部条件挂单

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/openAlgoOrders`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#请求权重 "请求权重的直接链接")

* 带symbol ***1***
* 不带 ***40***
  请小心使用不带symbol参数的调用

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| algoType | STRING | NO |  |
| symbol | STRING | NO |  |
| algoId | LONG | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 不带symbol参数，会返回所有交易对的挂单

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#响应示例 "响应示例的直接链接")

```
[  
   {  
       "algoId": 2148627,  
       "clientAlgoId": "MRumok0dkhrP4kCm12AHaB",  
       "algoType": "CONDITIONAL",  
       "orderType": "TAKE_PROFIT",  
       "symbol": "BNBUSDT",  
       "side": "SELL",  
       "positionSide": "BOTH",  
       "timeInForce": "GTC",  
       "quantity": "0.01",  
       "algoStatus": "NEW",  
       "actualOrderId": "",  
       "actualPrice": "0.00000",  
       "triggerPrice": "750.000",  
       "price": "750.000",  
       "icebergQuantity": null,  
       "tpTriggerPrice": "0.000",  
       "tpPrice": "0.000",  
	   "slTriggerPrice": "0.000",  
	   "slPrice": "0.000",  
       "tpOrderType": "",  
       "selfTradePreventionMode": "EXPIRE_MAKER",  
       "workingType": "CONTRACT_PRICE",  
       "priceMatch": "NONE",  
       "closePosition": false,  
       "priceProtect": false,  
       "reduceOnly": false,  
       "createTime": 1750514941540,  
       "updateTime": 1750514941540,  
       "triggerTime": 0,  
       "goodTillDate": 0  
   }  
]
```

[上一页

查询条件订单 (USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Query-Algo-Order)[下一页

查询所有条件订单(包括历史订单) (USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Query-All-Algo-Orders)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Current-All-Algo-Open-Orders#响应示例)