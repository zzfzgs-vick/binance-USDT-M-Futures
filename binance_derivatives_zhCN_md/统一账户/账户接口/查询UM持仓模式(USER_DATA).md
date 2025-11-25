<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode -->

* 统一账户
* 账户接口
* 查询UM持仓模式(USER-DATA)

本页总览

# 查询UM持仓模式(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#接口描述 "接口描述的直接链接")

查询用户目前在UM所有symbol合约上的持仓模式: 双向持仓或单向持仓。

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/positionSide/dual`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#请求权重 "请求权重的直接链接")

**30**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#响应示例 "响应示例的直接链接")

```
{  
    "dualSidePosition": true // "true": 双向持仓模式；"false": 单向持仓模式  
}
```

[上一页

更改CM持仓模式(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/account/Change-CM-Position-Mode)[下一页

查询CM持仓模式(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Current-Position-Mode)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Current-Position-Mode#响应示例)