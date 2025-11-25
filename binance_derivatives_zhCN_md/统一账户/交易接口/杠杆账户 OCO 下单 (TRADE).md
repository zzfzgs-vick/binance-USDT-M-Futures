<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO -->

* 统一账户
* 交易接口
* 杠杆账户OCO下单(TRADE)

本页总览

# 杠杆账户 OCO 下单 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#接口描述 "接口描述的直接链接")

杠杆账户发送新 OCO 订单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#http请求 "HTTP请求的直接链接")

POST `/papi/v1/margin/order/oco`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| listClientOrderId | STRING | NO | 整个 orderList 的唯一 ID |
| side | ENUM | YES | 详见枚举定义：订单方向 |
| quantity | DECIMAL | YES |  |
| limitClientOrderId | STRING | NO | 限价单的唯一 ID |
| price | DECIMAL | YES |  |
| limitIcebergQty | DECIMAL | NO |  |
| stopClientOrderId | STRING | NO | 止损/止损限价单的唯一 ID |
| stopPrice | DECIMAL | YES |  |
| stopLimitPrice | DECIMAL | NO | 如果提供，须配合提交`stopLimitTimeInForce` |
| stopIcebergQty | DECIMAL | NO |  |
| stopLimitTimeInForce | ENUM | NO | 有效值 `GTC/FOK/IOC` |
| newOrderRespType | ENUM | NO | 详见枚举定义：订单返回类型 |
| sideEffectType | ENUM | NO | NO\_SIDE\_EFFECT, MARGIN\_BUY, AUTO\_REPAY; 默认为 NO\_SIDE\_EFFECT |
| recvWindow | LONG | NO | 不能大于 `60000` |
| timestamp | LONG | YES |  |

Other Info:

> * 价格限制：
>   + `SELL`: 限价 > 最新成交价 >触发价
>   + `BUY`: 限价 < 最新成交价 < 触发价
> * 数量限制：
>   + 两个 legs 必须具有同样的数量
>   + `ICEBERG` 数量不必相同
> * 下单 rate：
>   + 一个`OCO`订单被算成 2 个普通订单

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#响应示例 "响应示例的直接链接")

```
{  
  "orderListId": 0,  
  "contingencyType": "OCO",  
  "listStatusType": "EXEC_STARTED",  
  "listOrderStatus": "EXECUTING",  
  "listClientOrderId": "JYVpp3F0f5CAG15DhtrqLp",  
  "transactionTime": 1563417480525,  
  "symbol": "LTCBTC",  
  "marginBuyBorrowAmount": "5",       // 下单后没有发生借款则不返回该字段  
  "marginBuyBorrowAsset": "BTC",    // 下单后没有发生借款则不返回该字段  
  "orders": [  
    {  
      "symbol": "LTCBTC",  
      "orderId": 2,  
      "clientOrderId": "Kk7sqHb9J6mJWTMDVW7Vos"  
    },  
    {  
      "symbol": "LTCBTC",  
      "orderId": 3,  
      "clientOrderId": "xTXKaGYd4bluPVp78IVRvl"  
    }  
  ],  
  "orderReports": [  
    {  
      "symbol": "LTCBTC",  
      "orderId": 2,  
      "orderListId": 0,  
      "clientOrderId": "Kk7sqHb9J6mJWTMDVW7Vos",  
      "transactTime": 1563417480525,  
      "price": "0.000000",  
      "origQty": "0.624363",  
      "executedQty": "0.000000",  
      "cummulativeQuoteQty": "0.000000",  
      "status": "NEW",  
      "timeInForce": "GTC",  
      "type": "STOP_LOSS",  
      "side": "BUY",  
      "stopPrice": "0.960664"  
    },  
    {  
      "symbol": "LTCBTC",  
      "orderId": 3,  
      "orderListId": 0,  
      "clientOrderId": "xTXKaGYd4bluPVp78IVRvl",  
      "transactTime": 1563417480525,  
      "price": "0.036435",  
      "origQty": "0.624363",  
      "executedQty": "0.000000",  
      "cummulativeQuoteQty": "0.000000",  
      "status": "NEW",  
      "timeInForce": "GTC",  
      "type": "LIMIT_MAKER",  
      "side": "BUY"  
    }  
  ]  
}
```

[上一页

杠杆账户归还借贷(MARGIN)](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Repay)[下一页

撤销UM订单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-UM-Order)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-New-OCO#响应示例)