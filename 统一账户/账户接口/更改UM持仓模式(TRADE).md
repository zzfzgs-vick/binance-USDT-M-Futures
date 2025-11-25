<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Position-Mode -->

* 统一账户
* 账户接口
* 更改UM持仓模式(TRADE)

本页总览

# 更改UM持仓模式(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Position-Mode#接口描述 "接口描述的直接链接")

变换用户在UM所有symbol合约上的持仓模式：双向持仓或单向持仓。

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Position-Mode#http请求 "HTTP请求的直接链接")

POST `/papi/v1/um/positionSide/dual`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Position-Mode#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Position-Mode#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| dualSidePosition | STRING | YES | "true": 双向持仓模式；"false": 单向持仓模式 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Position-Mode#响应示例 "响应示例的直接链接")

```
{  
    "code": 200,  
    "msg": "success"  
}
```

[上一页

调整CM开仓杠杆(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage)[下一页

更改CM持仓模式(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/account/Change-CM-Position-Mode)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Position-Mode#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Position-Mode#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Position-Mode#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Position-Mode#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Position-Mode#响应示例)