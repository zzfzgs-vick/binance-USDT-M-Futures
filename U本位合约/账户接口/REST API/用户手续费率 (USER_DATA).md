<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate -->

* U本位合约
* 账户接口
* REST API
* 用户手续费率(USER-DATA)

本页总览

# 用户手续费率 (USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#接口描述 "接口描述的直接链接")

查询用户手续费率

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/commissionRate`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#响应示例 "响应示例的直接链接")

```
{  
	"symbol": "BTCUSDT",  
  	"makerCommissionRate": "0.0002",  // 0.02%  
  	"takerCommissionRate": "0.0004"   // 0.04%  
}
```

[上一页

获取划转历史](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Future-Account-Transaction-History-List)[下一页

账户配置(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Config)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate#响应示例)