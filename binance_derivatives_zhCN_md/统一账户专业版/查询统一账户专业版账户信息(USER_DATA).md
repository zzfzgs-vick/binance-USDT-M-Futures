<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin-pro/account -->

* 统一账户专业版
* 账户接口
* 查询统一账户专业版信息(USER\_DATA)

本页总览

# 查询统一账户专业版账户信息(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account#接口描述 "接口描述的直接链接")

查询统一账户专业版账户信息

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/portfolio/account`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account#请求权重ip "请求权重(IP)的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account#响应示例 "响应示例的直接链接")

```
{  
        "uniMMR": "5167.92171923",        // 经典统一账户模式维持保证金率  
        "accountEquity": "122607.35137903",   // 经典统一账户总权益，单位为USD  
        "actualEquity": "142607.35137903",    // 不考虑质押率经典统一账户总权益，单位为USD  
        "accountMaintMargin": "23.72469206", // 经典统一账户维持保证金，即账户开仓及借贷总共需要的维持保证金，单位为USD  
        "accountInitialMargin": "47.44938412",  // PM PRO and PM PRO SPAN请忽略  
        "totalAvailableBalance" : "122,559.90199491",  // PM PRO and PM PRO SPAN请忽略  
        "accountStatus": "NORMAL",  // 经典统一账户当前账户状态:"NORMAL"正常状态, "MARGIN_CALL"补充保证金, "SUPPLY_MARGIN"再一次补充保证金, "REDUCE_ONLY"触发交易限制, "ACTIVE_LIQUIDATION"手动强制平仓, "FORCE_LIQUIDATION"强制平仓, "BANKRUPTED"破产  
        "accountType": "PM_1"     //PM_1统一账户专业版, PM_2统一账户， PM_2统一账户专业版SPAN  
}
```

[上一页

统一账户专业版资产阶梯质押率(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate)[下一页

BNB划转(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin-pro/account#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin-pro/account#http请求)
* [请求权重(IP)](/docs/zh-CN/derivatives/portfolio-margin-pro/account#请求权重ip)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin-pro/account#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin-pro/account#响应示例)