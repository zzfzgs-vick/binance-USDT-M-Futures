<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History -->

* 统一账户专业版
* 账户接口
* 查询统一账户专业版期货负余额收息历史(USER\_DATA)

本页总览

# 查询经典统一账户专业版期货负余额收息历史(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#接口描述 "接口描述的直接链接")

查询统一账户专业版期货负余额收息历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/portfolio/interest-history`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#请求权重ip "请求权重(IP)的直接链接")

**50**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| asset | STRING | NO |  |
| startTime | LONG | NO | 起始时间 |
| endTime | LONG | NO | 结束时间 |
| size | LONG | NO | 返回的结果集数量 默认值:10 最大值:100 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#响应示例 "响应示例的直接链接")

```
[  
    {  
        "asset": "USDT",      
        "interest": "24.4440",               //利息金额  
        "interestAccruedTime": 1670227200000,  
        "interestRate": "0.0001164",         //日利率   
        "principal": "210000"  
    }   
]
```

[上一页

查询自动清还合约负余额模式(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Auto-repay-futures-Status)[下一页

查询统一账户专业版SPAN信息(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#http请求)
* [请求权重(IP)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#请求权重ip)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History#响应示例)