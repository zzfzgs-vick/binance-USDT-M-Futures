<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM -->

* 统一账户
* 账户接口
* 查询用户CM手续费率(USER-DATA)

本页总览

# 查询用户CM手续费率(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#接口描述 "接口描述的直接链接")

查询用户CM手续费率

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#http请求 "HTTP请求的直接链接")

GET /`papi/v1/cm/commissionRate`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#请求权重 "请求权重的直接链接")

**20**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#响应示例 "响应示例的直接链接")

```
{  
    "symbol": "BTCUSD_PERP",  
    "makerCommissionRate": "0.00015",  // 0.015%  
    "takerCommissionRate": "0.00040"   // 0.040%  
}
```

[上一页

查询用户UM手续费率(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-UM)[下一页

查询杠杆借贷记录(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-Loan-Record)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Get-User-Commission-Rate-for-CM#响应示例)