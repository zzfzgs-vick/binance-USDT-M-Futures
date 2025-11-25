<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History -->

* 统一账户
* 账户接口
* 查询统一账户期货负余额收息历史(USER-DATA)

本页总览

# 查询统一账户期货负余额收息历史(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#接口描述 "接口描述的直接链接")

查询统一账户期货负余额收息历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#http请求 "HTTP请求的直接链接")

GET `/papi/v1/portfolio/interest-history`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#请求权重 "请求权重的直接链接")

**50**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| asset | STRING | NO |  |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| size | LONG | NO | Default:10 Max:100 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 响应返回为降序排列。
> * 查询时间范围最大不得超过30天，这是确保数据正确性必须的。
> * 若`startTime`和`endTime`没传，则默认返回最近7天数据。
> * 如果发送了`startTime`且未发送`endTime`，则返回`startTime`到现在的的利息历史记录；若`startTime`至今超过30天，则返回过去30天的利息历史记录。
> * 如果没有发送`startTime`而发送了`endTime`，则返回`endTime`之前7天的利息历史记录。

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#响应示例 "响应示例的直接链接")

```
[  
    {  
        "asset": "USDT",      
        "interest": "24.4440",               //利息金额  
        "interestAccuredTime": 1670227200000,  
        "interestRate": "0.0001164",         //日利率   
        "principal": "210000"  
    }  
]
```

[上一页

清还合约负余额(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Repay-futures-Negative-Balance)[下一页

统一账户资金归集(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History#响应示例)