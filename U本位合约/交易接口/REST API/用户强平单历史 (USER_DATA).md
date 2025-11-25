<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders -->

* U本位合约
* 交易接口
* REST API
* 用户强平单历史(USER-DATA)

本页总览

# 用户强平单历史 (USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders#接口描述 "接口描述的直接链接")

查询用户强平单历史

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/forceOrders`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders#请求权重 "请求权重的直接链接")

带symbol **20**, 不带symbol **50**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| autoCloseType | ENUM | NO | "LIQUIDATION": 强平单, "ADL": ADL 减仓单. |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| limit | INT | NO | Default 50; max 100. |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 如果没有传 "autoCloseType", 强平单和 ADL 减仓单都会被返回
> * 如果没有传"startTime", 只会返回"endTime"之前 7 天内的数据

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders#响应示例 "响应示例的直接链接")

```
[  
  {  
  	"orderId": 6071832819,  
  	"symbol": "BTCUSDT",  
  	"status": "FILLED",  
  	"clientOrderId": "autoclose-1596107620040000020",  
  	"price": "10871.09",  
  	"avgPrice": "10913.21000",  
  	"origQty": "0.001",  
  	"executedQty": "0.001",  
  	"cumQuote": "10.91321",  
  	"timeInForce": "IOC",  
  	"type": "LIMIT",  
  	"reduceOnly": false,  
  	"closePosition": false,  
  	"side": "SELL",  
  	"positionSide": "BOTH",  
  	"stopPrice": "0",  
  	"workingType": "CONTRACT_PRICE",  
  	"origType": "LIMIT",  
  	"time": 1596107620044,  
  	"updateTime": 1596107620087  
  }  
  {  
   	"orderId": 6072734303,  
   	"symbol": "BTCUSDT",  
   	"status": "FILLED",  
   	"clientOrderId": "adl_autoclose",  
   	"price": "11023.14",  
   	"avgPrice": "10979.82000",  
   	"origQty": "0.001",  
   	"executedQty": "0.001",  
   	"cumQuote": "10.97982",  
   	"timeInForce": "GTC",  
   	"type": "LIMIT",  
   	"reduceOnly": false,  
   	"closePosition": false,  
   	"side": "BUY",  
   	"positionSide": "SHORT",  
   	"stopPrice": "0",  
   	"workingType": "CONTRACT_PRICE",  
   	"origType": "LIMIT",  
   	"time": 1596110725059,  
   	"updateTime": 1596110725071  
  }  
]
```

[上一页

查询当前挂单(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Query-Current-Open-Order)[下一页

账户成交历史(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Users-Force-Orders#响应示例)