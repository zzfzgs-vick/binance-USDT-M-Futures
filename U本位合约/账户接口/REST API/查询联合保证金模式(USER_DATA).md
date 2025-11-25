<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode -->

* U本位合约
* 账户接口
* REST API
* 查询联合保证金模式(USER-DATA)

本页总览

# 查询联合保证金模式(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#接口描述 "接口描述的直接链接")

查询用户目前在 ***所有symbol*** 合约上的联合保证金模式。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/multiAssetsMargin`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#请求权重 "请求权重的直接链接")

30

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#响应示例 "响应示例的直接链接")

```
{  
	"multiAssetsMargin": true // "true": 联合保证金模式开启；"false": 联合保证金模式关闭  
}
```

[上一页

杠杆分层标准(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets)[下一页

查询持仓模式(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Position-Mode)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode#响应示例)