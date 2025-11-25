<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information -->

* 统一账户
* 账户接口
* 查询账户信息(USER-DATA)

本页总览

# 查询账户信息(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#接口描述 "接口描述的直接链接")

查询账户信息

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#http请求 "HTTP请求的直接链接")

GET `/papi/v1/account`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#响应示例 "响应示例的直接链接")

```
{  
   "uniMMR": "5167.92171923",   // 统一账户维持保证金率  
   "accountEquity": "73.47428058",   // 以USD计价的账户权益  
   "actualEquity": "122607.35137903",   // 不考虑质押率的以USD计价账户权益  
   "accountInitialMargin": "23.72469206",   
   "accountMaintMargin": "23.72469206", // 以USD计价统一账户维持保证金  
   "accountStatus": "NORMAL"   // 统一账户账户状态："NORMAL", "MARGIN_CALL", "SUPPLY_MARGIN", "REDUCE_ONLY", "ACTIVE_LIQUIDATION", "FORCE_LIQUIDATION", "BANKRUPTED"  
   "virtualMaxWithdrawAmount": "1627523.32459208"  // 以USD计价的最大可转出  
   "totalAvailableBalance":"",  
   "totalMarginOpenLoss":"",   
   "updateTime": 1657707212154 // 更新时间   
}
```

[上一页

查询账户余额(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account)[下一页

查询账户最大可借贷额度 (USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information#响应示例)