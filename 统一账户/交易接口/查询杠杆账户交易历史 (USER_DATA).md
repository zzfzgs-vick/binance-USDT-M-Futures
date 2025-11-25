<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List -->

* 统一账户
* 交易接口
* 查询杠杆账户交易历史 (USER-DATA)

本页总览

# 查询杠杆账户交易历史 (USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#接口描述 "接口描述的直接链接")

查询杠杆账户交易历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/myTrades`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| orderId | LONG | NO |  |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| fromId | LONG | NO | 获取TradeId，默认获取近期交易历史。 |
| limit | INT | NO | 默认 500; 最大 1000. |
| recvWindow | LONG | NO | 赋值不能大于 60000 |
| timestamp | LONG | YES |  |

**注意:**

* 如果设置 `fromId` , 获取订单 id >= `fromId`， 否则返回近期订单历史。
* `startTime` 和 `endTime`的间隔需要小于24小时。

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#响应示例 "响应示例的直接链接")

```
[  
    {  
        "commission": "0.00006000",  
        "commissionAsset": "BTC",  
        "id": 34,  
        "isBestMatch": true,  
        "isBuyer": false,  
        "isMaker": false,  
        "orderId": 39324,  
        "price": "0.02000000",  
        "qty": "3.00000000",  
        "symbol": "BNBBTC",  
        "time": 1561973357171  
    }  
]
```

[上一页

查询杠杆账户 OCO 挂单 (USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-Open-OCO)[下一页

杠杆账户还款(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Repay-Debt)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Trade-List#响应示例)