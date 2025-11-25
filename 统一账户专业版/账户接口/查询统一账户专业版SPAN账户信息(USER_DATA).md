<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2 -->

* 统一账户专业版
* 账户接口
* 查询统一账户专业版SPAN信息(USER\_DATA)

本页总览

# 查询统一账户专业版SPAN账户信息(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#接口描述 "接口描述的直接链接")

查询统一账户专业版SPAN账户信息

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#http请求 "HTTP请求的直接链接")

GET `/sapi/v2/portfolio/account`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#请求权重ip "请求权重(IP)的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#响应示例 "响应示例的直接链接")

```
{  
        "uniMMR": "5167.92171923",          
        "accountEquity": "122607.35137903",  // Account equity, unit：USD  
        "actualEquity": "142607.35137903",   // Actual equity, unit：USD  
        "accountMaintMargin": "23.72469206", //Account maintenance margin, unit：USD  
        "riskUnitMMList":[  
             {  
                 "asset": "BTC",  
                 "uniMaintainUsd": "23.72469206"  
             }  
        ]  
        "marginMM": "0.00000000",   
        "otherMM": "0.00000000",   
        "accountStatus": "NORMAL",   // Classic Portfolio margin account status:"NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY", "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"  
        "accountType": "PM_3"     //PM_1 for classic PM, PM_2 for PM, PM_3 for PM Pro(SPAN)   
}
```

[上一页

查询统一账户专业版期货负余额收息历史(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Negative-Balance-Interest-History)[下一页

查询统一账户专业版账户余额(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Balance-Info)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#http请求)
* [请求权重(IP)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#请求权重ip)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Get-Classic-Portfolio-Margin-Account-Info-V2#响应示例)