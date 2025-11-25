<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets -->

* U本位合约
* 账户接口
* REST API
* 杠杆分层标准(USER-DATA)

本页总览

# 杠杆分层标准 (USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#接口描述 "接口描述的直接链接")

查询账户特定交易对的杠杆分层标准

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/leverageBracket`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#响应示例 "响应示例的直接链接")

> **响应:**

```
[  
    {  
        "symbol": "ETHUSDT",  
	    "notionalCoef": 1.50,   //用户bracket相对默认bracket的倍数，仅在和交易对默认不一样时显示  
        "brackets": [  
            {  
                "bracket": 1,   // 层级  
                "initialLeverage": 75,  // 该层允许的最高初始杠杆倍数  
                "notionalCap": 10000,  // 该层对应的名义价值上限  
                "notionalFloor": 0,  // 该层对应的名义价值下限   
                "maintMarginRatio": 0.0065, // 该层对应的维持保证金率  
                "cum": 0.0 // 速算数  
            },  
        ]  
    }  
]
```

> **或** (若发送symbol)

```
{  
    "symbol": "ETHUSDT",  
    "notionalCoef": 1.50,  
    "brackets": [  
        {  
            "bracket": 1,  
            "initialLeverage": 75,  
            "notionalCap": 10000,  
            "notionalFloor": 0,  
            "maintMarginRatio": 0.0065,  
            "cum":0  
        },  
    ]  
}
```

[上一页

查询用户下单限频(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Query-Rate-Limit)[下一页

查询联合保证金模式(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Get-Current-Multi-Assets-Mode)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Notional-and-Leverage-Brackets#响应示例)