<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade -->

* 统一账户
* 交易接口
* UM合约交易BNB抵扣开关(TRADE)

本页总览

# UM合约交易BNB抵扣开关(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#接口描述 "接口描述的直接链接")

改变用户 ***所有 symbol*** UM合约交易BNB抵扣开关(手续费抵扣开或关)

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#http请求 "HTTP请求的直接链接")

POST `/papi/v1/um/feeBurn`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| feeBurn | STRING | YES | "true": 手续费抵扣开; "false": 手续费抵扣关 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#响应示例 "响应示例的直接链接")

```
{  
	"code": 200,  
	"msg": "success"  
}
```

[上一页

CM持仓ADL队列估算(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/CM-Position-ADL-Quantile-Estimation)[下一页

获取UM BNB抵扣开关状态(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Get-UM-Futures-BNB-Burn-Status)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Toggle-BNB-Burn-On-UM-Futures-Trade#响应示例)