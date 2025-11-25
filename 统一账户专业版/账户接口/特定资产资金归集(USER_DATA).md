<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset -->

* 统一账户专业版
* 账户接口
* 特定资产资金归集(USER\_DATA)

本页总览

# 特定资产资金归集(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#接口描述 "接口描述的直接链接")

特定资产账户资金归集，从合约账户划转到杠杆账户

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#http请求 "HTTP请求的直接链接")

POST `/sapi/v1/portfolio/asset-collection`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#请求权重ip "请求权重(IP)的直接链接")

**60**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| asset | STRING | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 本接口不支持划转BNB资产

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#响应示例 "响应示例的直接链接")

```
{  
    "msg": "success"  
}
```

[上一页

资金归集(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Auto-collection)[下一页

偿还统一账户专业版穿仓负债](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#http请求)
* [请求权重(IP)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#请求权重ip)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Fund-Collection-by-Asset#响应示例)