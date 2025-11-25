<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer -->

* 统一账户专业版
* 账户接口
* BNB划转(USER\_DATA)

本页总览

# BNB划转(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#接口描述 "接口描述的直接链接")

BNB在杠杆账户和USD-M期货账户划转

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/portfolio/bnb-transfer`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#请求权重ip "请求权重(IP)的直接链接")

**1500**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| amount | DECIMAL | YES |  |
| transferSide | STRING | YES | "TO\_UM","FROM\_UM" |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 本接口每10分钟仅可以调用2次

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#响应示例 "响应示例的直接链接")

```
{  
     "tranId": 100000001  
}
```

[上一页

查询统一账户专业版信息(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/account)[下一页

资金归集(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Auto-collection)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#http请求)
* [请求权重(IP)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#请求权重ip)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin-pro/account/BNB-transfer#响应示例)