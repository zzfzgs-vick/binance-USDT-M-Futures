<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status -->

* 统一账户
* 账户接口
* 更改自动清还合约负余额模式(TRADE)

本页总览

# 更改自动清还合约负余额模式(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#接口描述 "接口描述的直接链接")

更改自动支付合约负余额模式

## HTTP Request[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#http-request "HTTP Request的直接链接")

POST `/papi/v1/repay-futures-switch`

## 请求权重(IP):[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#请求权重ip "请求权重(IP):的直接链接")

**750**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| autoRepay | STRING | YES | 默认为`true`; `false`代表关闭自动清还合约负余额 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#响应示例 "响应示例的直接链接")

```
{  
    "msg": "success"  
}
```

[上一页

查询自动清还合约负余额模式(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status)[下一页

获取杠杆利息历史(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Margin-BorrowLoan-Interest-History)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#接口描述)
* [HTTP Request](/docs/zh-CN/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#http-request)
* [请求权重(IP):](/docs/zh-CN/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#请求权重ip)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status#响应示例)