<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2 -->

* U本位合约
* 账户接口
* REST API
* 账户余额V2(USER-DATA)

本页总览

# 账户余额V2 (USER\_DATA)

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2#http请求 "HTTP请求的直接链接")

GET `/fapi/v2/balance`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2#响应示例 "响应示例的直接链接")

```
[  
 	{  
 		"accountAlias": "SgsR",    // 账户唯一识别码  
 		"asset": "USDT",		// 资产  
 		"balance": "122607.35137903",	// 总余额  
 		"crossWalletBalance": "23.72469206", // 全仓余额  
  		"crossUnPnl": "0.00000000",  // 全仓持仓未实现盈亏  
  		"availableBalance": "23.72469206",       // 下单可用余额  
  		"maxWithdrawAmount": "23.72469206",     // 最大可转出余额  
  		"marginAvailable": true,    // 是否可用作联合保证金  
  		"updateTime": 1617939110373  
	}  
]
```

[上一页

账户余额V3(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V3)[下一页

账户信息V3(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Information-V3)

* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Futures-Account-Balance-V2#响应示例)