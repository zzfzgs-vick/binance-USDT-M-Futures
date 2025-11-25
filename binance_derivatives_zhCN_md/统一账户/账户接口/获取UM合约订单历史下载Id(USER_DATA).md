<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History -->

* 统一账户
* 账户接口
* 获取UM合约订单历史下载Id(USER-DATA)

本页总览

# 获取UM合约订单历史下载Id(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#接口描述 "接口描述的直接链接")

获取UM合约订单历史下载Id

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#http请求 "HTTP请求的直接链接")

GET `papi/v1/um/order/asyn`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#请求权重 "请求权重的直接链接")

**1500**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| startTime | LONG | YES | 起始时间，ms格式时间戳 |
| endTime | LONG | YES | 结束时间，ms格式时间戳 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 存在每月10次的请求限制，网页端和Rest接口下载次数共用。
> * `startTime`与`endTime`间隔不能超过1年

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#响应示例 "响应示例的直接链接")

```
{  
	"avgCostTimestampOfLast30d":7241837, //过去30天平均数据下载时间  
  	"downloadId":"546975389218332672",   //下载Id  
}
```

[上一页

通过下载Id获取UM合约交易历史下载链接(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Trade-Download-Link-by-Id)[下一页

通过下载Id获取UM合约订单历史下载链接(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History#响应示例)