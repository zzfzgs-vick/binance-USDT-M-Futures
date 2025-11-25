<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders -->

* 统一账户
* 交易接口
* 取消全部UM条件单(TRADE)

本页总览

# 取消全部UM条件单(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#接口描述 "接口描述的直接链接")

取消全部UM条件单

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#http请求 "HTTP请求的直接链接")

DELETE `/papi/v1/um/conditional/allOpenOrders`

## 请求权重(Order)[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#请求权重order "请求权重(Order)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#响应示例 "响应示例的直接链接")

```
{  
    "code": "200",   
    "msg": "The operation of cancel all conditional open order is done."  
}
```

[上一页

取消UM条件订单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-UM-Conditional-Order)[下一页

撤销CM订单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-CM-Order)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#http请求)
* [请求权重(Order)](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#请求权重order)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Cancel-All-UM-Open-Conditional-Orders#响应示例)