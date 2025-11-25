<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin -->

* 统一账户专业版
* 账户接口
* 查询统一账户LDUSDT可转金额(USER\_DATA)

本页总览

# 查询统一账户LDUSDT可转金额(TRADE)

# Get Transferable Earn Asset Balance for Portfolio Margin (USER\_DATA)

## API Description[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#api-description "API Description的直接链接")

Get transferable earn asset balance for all types of Portfolio Margin account

## HTTP Request[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#http-request "HTTP Request的直接链接")

GET `/sapi/v1/portfolio/earn-asset-balance`

## Request Weight(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#request-weightip "Request Weight(IP)的直接链接")

**1500**

## Request Parameters[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#request-parameters "Request Parameters的直接链接")

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| asset | STRING | YES | `LDUSDT` only |
| transferType | STRING | YES | `EARN_TO_FUTURE` /`FUTURE_TO_EARN` |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## Response Example[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#response-example "Response Example的直接链接")

```
{  
    "asset": "LDUSDT",  
    "amount": "0.55"  
}
```

[上一页

统一账户LDUSDT转入(TRADE)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Transfer-LDUSDT-Portfolio-Margin)[下一页

账户信息流连接](/docs/zh-CN/derivatives/portfolio-margin-pro/portfolio-margin-pro-user-data-stream)

* [API Description](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#api-description)
* [HTTP Request](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#http-request)
* [Request Weight(IP)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#request-weightip)
* [Request Parameters](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#request-parameters)
* [Response Example](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Transferable-Earn-Asset-Balance-Portfolio-Margin#response-example)