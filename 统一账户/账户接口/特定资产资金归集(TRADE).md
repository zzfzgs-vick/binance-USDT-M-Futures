<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Collection-by-Asset -->

* 统一账户
* 账户接口
* 特定资产资金归集(TRADE)

本页总览

# 特定资产资金归集(TRADE)

## API Description[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Collection-by-Asset#api-description "API Description的直接链接")

特定资产账户资金归集，从合约账户划转到杠杆账户

## HTTP Request[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Collection-by-Asset#http-request "HTTP Request的直接链接")

POST `/papi/v1/asset-collection`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Collection-by-Asset#请求权重ip "请求权重(IP)的直接链接")

**30**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Collection-by-Asset#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| asset | STRING | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 本接口不支持划转BNB资产

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Collection-by-Asset#响应示例 "响应示例的直接链接")

```
{  
    "msg": "success"  
}
```

[上一页

统一账户资金归集(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection)[下一页

BNB划转(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/account/BNB-transfer)

* [API Description](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Collection-by-Asset#api-description)
* [HTTP Request](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Collection-by-Asset#http-request)
* [请求权重(IP)](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Collection-by-Asset#请求权重ip)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Collection-by-Asset#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Collection-by-Asset#响应示例)