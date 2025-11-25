<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status -->

* 统一账户
* 交易接口
* 获取UM BNB抵扣开关状态(USER\_DATA)

本页总览

# 获取UM BNB抵扣开关状态(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#接口描述 "接口描述的直接链接")

查询用户 ***所有 symbol*** UM合约交易BNB抵扣开关状态(手续费抵扣开或关)

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/feeBurn`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#请求权重 "请求权重的直接链接")

**30**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#响应示例 "响应示例的直接链接")

```
{  
	"feeBurn": true // "true": 手续费抵扣开; "false": 手续费抵扣关  
}
```

[上一页

UM合约交易BNB抵扣开关(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade)[下一页

查询查询杠杆账户订单(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Margin-Account-Order)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status#响应示例)