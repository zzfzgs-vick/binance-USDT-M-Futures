<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type -->

* U本位合约
* 交易接口
* REST API
* 变换逐全仓模式(TRADE)

本页总览

# 变换逐全仓模式 (TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#接口描述 "接口描述的直接链接")

变换用户在指定symbol合约上的保证金模式：逐仓或全仓。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#http请求 "HTTP请求的直接链接")

POST `/fapi/v1/marginType`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES | 交易对 |
| marginType | ENUM | YES | 保证金模式 ISOLATED(逐仓), CROSSED(全仓) |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#响应示例 "响应示例的直接链接")

```
{  
	"code": 200,  
	"msg": "success"  
}
```

[上一页

账户成交历史(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Account-Trade-List)[下一页

更改持仓模式(TRADE)](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Position-Mode)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/trade/rest-api/Change-Margin-Type#响应示例)