<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage -->

* 统一账户
* 账户接口
* 调整CM开仓杠杆(TRADE)

本页总览

# 调整CM开仓杠杆(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#接口描述 "接口描述的直接链接")

调整用户在指定CM symbol合约的开仓杠杆。不同持仓方向上使用相同杠杆倍数，共享允许的最大交易标的资产数量

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#http请求 "HTTP请求的直接链接")

POST `/papi/v1/cm/leverage`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| leverage | INT | YES | target initial leverage: int from 1 to 125 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#响应示例 "响应示例的直接链接")

```
{  
    "leverage": 21,  
    "maxQty": "1000",  
    "symbol": "BTCUSD_200925"  
}
```

[上一页

调整UM开仓杠杆(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Initial-Leverage)[下一页

更改UM持仓模式(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/account/Change-UM-Position-Mode)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Change-CM-Initial-Leverage#响应示例)