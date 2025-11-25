<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders -->

* 统一账户
* 交易接口
* 获取账户杠杆强制平仓记录(USER-DATA)

本页总览

# 获取账户杠杆强制平仓记录(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#接口描述 "接口描述的直接链接")

获取账户杠杆强制平仓记录

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/forceOrders`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#请求权重 "请求权重的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| current | LONG | NO | 当前查询页。 开始值 1. 默认:1 |
| size | LONG | NO | 默认:10 最大:100 |
| recvWindow | LONG | NO | 赋值不能大于 `60000` |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#响应示例 "响应示例的直接链接")

```
{  
    "rows": [  
        {  
            "avgPrice": "0.00388359",  
            "executedQty": "31.39000000",  
            "orderId": 180015097,  
            "price": "0.00388110",  
            "qty": "31.39000000",  
            "side": "SELL",  
            "symbol": "BNBBTC",  
            "timeInForce": "GTC",  
            "updatedTime": 1558941374745  
        }  
    ],  
    "total": 1  
}
```

[上一页

查询CM订单修改历史(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Modify-Order-History)[下一页

UM账户成交历史(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders#响应示例)