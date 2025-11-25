<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection -->

* 统一账户
* 账户接口
* 统一账户资金归集(TRADE)

本页总览

# 统一账户资金归集(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#接口描述 "接口描述的直接链接")

资金归集到统一账户钱包

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#http请求 "HTTP请求的直接链接")

POST `/papi/v1/auto-collection`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#请求权重 "请求权重的直接链接")

**750**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| recvWindow | LONG | NO | 赋值不能超过 60000 |
| timestamp | LONG | YES |  |

> * BNB资产不会归集
> * 滚动每小时仅能调用500次

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#响应示例 "响应示例的直接链接")

```
{  
    "msg": "success"  
}
```

[上一页

查询统一账户期货负余额收息历史(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Portfolio-Margin-Negative-Balance-Interest-History)[下一页

特定资产资金归集(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Collection-by-Asset)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Fund-Auto-collection#响应示例)