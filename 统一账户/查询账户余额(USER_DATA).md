<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account -->

* 统一账户
* 账户接口
* 查询账户余额(USER-DATA)

本页总览

# 查询账户余额(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account#接口描述 "接口描述的直接链接")

查询账户余额

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account#http请求 "HTTP请求的直接链接")

GET `/papi/v1/balance`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| asset | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account#响应示例 "响应示例的直接链接")

```
[  
    {  
        "asset": "USDT",    // 资产  
        "totalWalletBalance": "122607.35137903", // 钱包余额 =  全仓杠杆未锁定 + 全仓杠杆锁定 + u本位合约钱包余额 + 币本位合约钱包余额  
        "crossMarginAsset": "92.27530794", // 全仓资产 = 全仓杠杆未锁定 + 全仓杠杆锁定  
        "crossMarginBorrowed": "10.00000000", // 全仓杠杆借贷  
        "crossMarginFree": "100.00000000", // 全仓杠杆未锁定  
        "crossMarginInterest": "0.72469206", // 全仓杠杆利息  
        "crossMarginLocked": "3.00000000", //全仓杠杆锁定   
        "umWalletBalance": "0.00000000",  // u本位合约钱包余额  
        "umUnrealizedPNL": "23.72469206",     // u本位未实现盈亏  
        "cmWalletBalance": "23.72469206",       // 币本位合约钱包余额  
        "cmUnrealizedPNL": "",    // 币本位未实现盈亏  
        "updateTime": 1617939110373,  
        "negativeBalance": "0"  
    }  
]
```

**或 (发送asset)**

```
{  
    "asset": "USDT",      
    "totalWalletBalance": "122607.35137903",   
    "crossMarginBorrowed": "10.00000000",   
    "crossMarginFree": "100.00000000",   
    "crossMarginInterest": "0.72469206",   
    "crossMarginLocked": "3.00000000",  
    "umWalletBalance": "0.00000000",    
    "umUnrealizedPNL": "23.72469206",       
    "cmWalletBalance": "23.72469206",        
    "cmUnrealizedPNL": "",     
    "updateTime": 1617939110373,  
    "negativeBalance": "0"  
}
```

[上一页

listenKey过期推送](/docs/zh-CN/derivatives/portfolio-margin/user-data-streams/Event-User-Data-Stream-Expired)[下一页

查询账户信息(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account#响应示例)