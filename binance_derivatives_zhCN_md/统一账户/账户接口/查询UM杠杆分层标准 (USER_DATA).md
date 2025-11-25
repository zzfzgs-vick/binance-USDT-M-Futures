<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets -->

* 统一账户
* 账户接口
* 查询UM杠杆分层标准 (USER-DATA)

本页总览

# 查询UM杠杆分层标准 (USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#接口描述 "接口描述的直接链接")

查询UM杠杆分层标准

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/leverageBracket`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#响应示例 "响应示例的直接链接")

```
[  
    {  
        "symbol": "ETHUSDT",  
        "notionalCoef": "4.0",  
        "brackets": [  
            {  
                "bracket": 1,   // 层级  
                "initialLeverage": 75,  // 该层允许的最高初始杠杆倍数  
                "notionalCap": 10000,  // 该层对应的数量上限  
                "notionalFloor": 0,  // 该层对应的数量下限   
                "maintMarginRatio": 0.0065, // 该层对应的维持保证金率  
                "cum":0 // 速算数  
            },  
        ]  
    }  
]
```

[上一页

查询CM持仓模式(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Current-Position-Mode)[下一页

查询 CM 杠杆分层标准 (USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/CM-Notional-and-Leverage-Brackets)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/UM-Notional-and-Leverage-Brackets#响应示例)