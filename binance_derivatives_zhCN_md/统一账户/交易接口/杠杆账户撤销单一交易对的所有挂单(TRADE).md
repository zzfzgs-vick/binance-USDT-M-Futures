<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol -->

* 统一账户
* 交易接口
* 杠杆账户撤销单一交易对的所有挂单(TRADE)

本页总览

# 杠杆账户撤销单一交易对的所有挂单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol#接口描述 "接口描述的直接链接")

杠杆账户撤销单一交易对的所有挂单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol#http请求 "HTTP请求的直接链接")

DELETE `/papi/v1/margin/allOpenOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| recvWindow | LONG | NO | 赋值不能超过 60000 |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol#响应示例 "响应示例的直接链接")

```
[  
  {  
    "symbol": "BTCUSDT",  
    "origClientOrderId": "E6APeyTJvkMvLMYMqu1KQ4",  
    "orderId": 11,  
    "orderListId": -1,  
    "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
    "price": "0.089853",  
    "origQty": "0.178622",  
    "executedQty": "0.000000",  
    "cummulativeQuoteQty": "0.000000",  
    "status": "CANCELED",  
    "timeInForce": "GTC",  
    "type": "LIMIT",  
    "side": "BUY"  
  },  
  {  
    "orderListId": 1929,  
    "contingencyType": "OCO",  
    "listStatusType": "ALL_DONE",  
    "listOrderStatus": "ALL_DONE",  
    "listClientOrderId": "2inzWQdDvZLHbbAmAozX2N",  
    "transactionTime": 1585230948299,  
    "symbol": "BTCUSDT",  
    "orders": [  
      {  
        "symbol": "BTCUSDT",  
        "orderId": 20,  
        "clientOrderId": "CwOOIPHSmYywx6jZX77TdL"  
      },  
      {  
        "symbol": "BTCUSDT",  
        "orderId": 21,  
        "clientOrderId": "461cPg51vQjV3zIMOXNz39"  
      }  
    ],  
    "orderReports": [  
      {  
        "symbol": "BTCUSDT",  
        "origClientOrderId": "CwOOIPHSmYywx6jZX77TdL",  
        "orderId": 20,  
        "orderListId": 1929,  
        "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
        "price": "0.668611",  
        "origQty": "0.690354",  
        "executedQty": "0.000000",  
        "cummulativeQuoteQty": "0.000000",  
        "status": "CANCELED",  
        "timeInForce": "GTC",  
        "type": "STOP_LOSS_LIMIT",  
        "side": "BUY",  
        "stopPrice": "0.378131",  
        "icebergQty": "0.017083"  
      },  
      {  
        "symbol": "BTCUSDT",  
        "origClientOrderId": "461cPg51vQjV3zIMOXNz39",  
        "orderId": 21,  
        "orderListId": 1929,  
        "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",  
        "price": "0.008791",  
        "origQty": "0.690354",  
        "executedQty": "0.000000",  
        "cummulativeQuoteQty": "0.000000",  
        "status": "CANCELED",  
        "timeInForce": "GTC",  
        "type": "LIMIT_MAKER",  
        "side": "BUY",  
        "icebergQty": "0.639962"  
      }  
    ]  
  }  
]
```

[上一页

取消杠杆账户OCO订单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-OCO-Orders)[下一页

修改UM订单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Modify-UM-Order)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-All-Open-Orders-on-a-Symbol#响应示例)