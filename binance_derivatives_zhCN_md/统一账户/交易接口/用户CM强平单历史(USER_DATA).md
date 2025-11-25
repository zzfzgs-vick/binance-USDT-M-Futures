<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders -->

* 统一账户
* 交易接口
* 用户CM强平单历史(USER-DATA)

本页总览

# 用户CM强平单历史(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#接口描述 "接口描述的直接链接")

查询用户CM强平单历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#http请求 "HTTP请求的直接链接")

GET `/papi/v1/cm/forceOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#请求权重 "请求权重的直接链接")

带 symbol **20**, 不带 symbol **50**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| autoCloseType | ENUM | NO | `LIQUIDATION`: 强平单, `ADL`: ADL 减仓单. |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| limit | INT | NO | 默认 50；最大 100. |
| recvWindow | LONG | NO | 赋值不能超过 60000 |
| timestamp | LONG | YES |  |

* 如果没有传`autoCloseType`，强平单和 ADL 减仓单都会被返回
* 如果没有传`startTime`, 只会返回`endTime`之前 7 天内的数据

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#响应示例 "响应示例的直接链接")

```
[  
  {  
    "orderId": 165123080,  
    "symbol": "BTCUSD_200925",  
    "pair": "BTCUSD",  
    "status": "FILLED",  
    "clientOrderId": "autoclose-1596542005017000006",  
    "price": "11326.9",  
    "avgPrice": "11326.9",  
    "origQty": "1",  
    "executedQty": "1",  
    "cumBase": "0.00882854",  
    "timeInForce": "IOC",  
    "type": "LIMIT",  
    "reduceOnly": false,  
    "side": "SELL",  
    "positionSide": "BOTH",  
    "origType": "LIMIT",  
    "time": 1596542005019,  
    "updateTime": 1596542005050,  
  }  
]
```

[上一页

用户强平单历史(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-UM-Force-Orders)[下一页

查询UM订单修改历史(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Modify-Order-History)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-CM-Force-Orders#响应示例)