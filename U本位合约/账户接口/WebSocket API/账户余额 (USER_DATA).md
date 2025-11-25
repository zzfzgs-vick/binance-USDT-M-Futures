<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Futures-Account-Balance -->

* U本位合约
* 账户接口
* WebSocket API
* 账户余额(USER-DATA)

本页总览

# 账户余额 (USER\_DATA)

查询账户余额

## 方式[​](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Futures-Account-Balance#方式 "方式的直接链接")

`account.balance`

## 请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Futures-Account-Balance#请求 "请求的直接链接")

```
{  
    "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
    "method": "account.balance",  
    "params": {  
        "apiKey": "xTaDyrmvA9XT2oBHHjy39zyPzKCvMdtH3b9q4xadkAg2dNSJXQGCxzui26L823W2",  
        "timestamp": 1702561978458,  
        "signature": "208bb94a26f99aa122b1319490ca9cb2798fccc81d9b6449521a26268d53217a"  
    }  
}
```

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Futures-Account-Balance#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Futures-Account-Balance#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Futures-Account-Balance#响应示例 "响应示例的直接链接")

```
{  
    "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",  
    "status": 200,  
    "result": [  
      {  
        "accountAlias": "SgsR",    // 账户唯一识别码  
        "asset": "USDT",		// 资产  
        "balance": "122607.35137903",	// 总余额  
        "crossWalletBalance": "23.72469206", // 全仓余额  
          "crossUnPnl": "0.00000000"  // 全仓持仓未实现盈亏  
          "availableBalance": "23.72469206",       // 下单可用余额  
          "maxWithdrawAmount": "23.72469206",     // 最大可转出余额  
          "marginAvailable": true,    // 是否可用作联合保证金  
          "updateTime": 1617939110373  
      }  
    ],  
    "rateLimits": [  
      {  
        "rateLimitType": "REQUEST_WEIGHT",  
        "interval": "MINUTE",  
        "intervalNum": 1,  
        "limit": 2400,  
        "count": 20  
      }  
    ]  
}
```

[上一页

账户余额(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api)[下一页

账户信息V2(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Account-Information-V2)

* [方式](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Futures-Account-Balance#方式)
* [请求](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Futures-Account-Balance#请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Futures-Account-Balance#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Futures-Account-Balance#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/account/websocket-api/Futures-Account-Balance#响应示例)