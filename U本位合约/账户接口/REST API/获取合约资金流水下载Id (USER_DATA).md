<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Transaction-History -->

* U本位合约
* 账户接口
* REST API
* 获取合约资金流水下载Id(USER-DATA)

本页总览

# 获取合约资金流水下载Id (USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Transaction-History#接口描述 "接口描述的直接链接")

获取合约资金流水下载Id

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Transaction-History#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/income/asyn`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Transaction-History#请求权重 "请求权重的直接链接")

**1000**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Transaction-History#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| startTime | LONG | YES | 起始时间，ms格式时间戳 |
| endTime | LONG | YES | 结束时间，ms格式时间戳 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 存在每月5次的请求限制，网页端和Rest接口下载次数共用。
> * `startTime`与`endTime`间隔不能超过1年

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Transaction-History#响应示例 "响应示例的直接链接")

```
{  
	"avgCostTimestampOfLast30d":7241837, //过去30天平均数据下载时间  
  	"downloadId":"546975389218332672",   //下载Id  
}
```

[上一页

合约交易量化规则指标(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Trading-Quantitative-Rules-Indicators)[下一页

通过下载Id获取合约资金流水下载链接(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Futures-Transaction-History-Download-Link-by-Id)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Transaction-History#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Transaction-History#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Transaction-History#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Transaction-History#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Download-Id-For-Futures-Transaction-History#响应示例)