<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-Order -->

* 统一账户
* 交易接口
* 杠杆账户撤销订单 (TRADE)

本页总览

# 杠杆账户撤销订单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-Order#接口描述 "接口描述的直接链接")

杠杆账户撤销订单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-Order#http请求 "HTTP请求的直接链接")

DELETE `/papi/v1/margin/order`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-Order#请求权重 "请求权重的直接链接")

**2**

**参数:**

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| orderId | LONG | NO |  |
| origClientOrderId | STRING | NO |  |
| newClientOrderId | STRING | NO | 用于唯一识别此撤销订单，默认自动生成。 |
| recvWindow | LONG | NO | 赋值不能超过 `60000` |
| timestamp | LONG | YES |  |

> * `orderId` 或 `origClientOrderId` 必须至少发送一个

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-Order#响应示例 "响应示例的直接链接")

```
{  
  "symbol": "LTCBTC",  
  "orderId": 28,  
  "origClientOrderId": "myOrder1",  
  "clientOrderId": "cancelMyOrder1",  
  "price": "1.00000000",  
  "origQty": "10.00000000",  
  "executedQty": "8.00000000",  
  "cummulativeQuoteQty": "8.00000000",  
  "status": "CANCELED",  
  "timeInForce": "GTC",  
  "type": "LIMIT",  
  "side": "SELL"  
}
```

[上一页

取消全部CM条件单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-CM-Open-Conditional-Orders)[下一页

取消杠杆账户OCO订单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-OCO-Orders)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-Order#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-Order#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-Order#请求权重)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-Margin-Account-Order#响应示例)