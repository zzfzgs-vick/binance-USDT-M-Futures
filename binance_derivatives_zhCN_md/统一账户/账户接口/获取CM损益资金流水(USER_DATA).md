<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Income-History -->

* 统一账户
* 账户接口
* 获取CM损益资金流水(USER-DATA)

本页总览

# 获取CM损益资金流水(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Income-History#接口描述 "接口描述的直接链接")

获取CM损益资金流水

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Income-History#http请求 "HTTP请求的直接链接")

GET `/papi/v1/cm/income`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Income-History#请求权重 "请求权重的直接链接")

**30**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Income-History#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| incomeType | STRING | NO | "TRANSFER","WELCOME\_BONUS", "FUNDING\_FEE", "REALIZED\_PNL", "COMMISSION", "INSURANCE\_CLEAR", and "DELIVERED\_SETTELMENT" |
| startTime | LONG | NO | 起始时间 |
| endTime | LONG | NO | 结束时间 |
| limit | INT | NO | 默认 100; 最大 1000 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 如果`startTime` 和 `endTime` 均未发送, 只会返回最近7天的数据.
> * 如果`incomeType`没有发送，返回所有类型账户损益资金流水。
> * `trandId` 在相同用户的同一种收益流水类型中是唯一的。
> * 仅保留最近3个月的数据。

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Income-History#响应示例 "响应示例的直接链接")

```
[  
    {  
        "symbol": "",               // 交易对，仅针对涉及交易对的资金流  
        "incomeType": "TRANSFER",   // 资金流类型  
        "income": "-0.37500000",    // 资金流数量，正数代表流入，负数代表流出  
        "asset": "BTC",             // 资产内容  
        "info":"WITHDRAW",          // 备注信息，取决于流水类型  
        "time": 1570608000000,  
        "tranId":"9689322392",      // 划转ID  
        "tradeId":""                // 引起流水产生的原始交易ID  
    },  
    {  
        "symbol": "BTCUSD_200925",  
        "incomeType": "COMMISSION",   
        "income": "-0.01000000",  
        "asset": "BTC",  
        "info":"",  
        "time": 1570636800000,  
        "tranId":"9689322392",  
        "tradeId":"2059192"  
    }  
]
```

[上一页

获取UM损益资金流水(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Income-History)[下一页

获取UM账户信息(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Account-Detail)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Income-History#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Income-History#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Income-History#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Income-History#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Income-History#响应示例)