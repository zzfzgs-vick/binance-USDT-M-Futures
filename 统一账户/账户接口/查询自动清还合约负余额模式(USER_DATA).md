<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status -->

* 统一账户
* 账户接口
* 查询自动清还合约负余额模式(USER-DATA)

本页总览

# 查询自动清还合约负余额模式(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#接口描述 "接口描述的直接链接")

查询自动清还合约负余额模式

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#http请求 "HTTP请求的直接链接")

GET `/papi/v1/repay-futures-switch`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#请求权重ip "请求权重(IP)的直接链接")

**30**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#响应示例 "响应示例的直接链接")

```
{  
    "autoRepay": true  //  `true`代表自动清还合约负余额; `false`代表关闭自动清还合约负余额  
}
```

[上一页

查询杠杆还贷记录(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record)[下一页

更改自动清还合约负余额模式(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/account/Change-Auto-repay-futures-Status)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#http请求)
* [请求权重(IP)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#请求权重ip)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status#响应示例)