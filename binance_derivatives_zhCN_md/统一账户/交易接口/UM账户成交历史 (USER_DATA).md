<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List -->

* 统一账户
* 交易接口
* UM账户成交历史(USER-DATA)

本页总览

# UM账户成交历史 (USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#接口描述 "接口描述的直接链接")

获取UM某交易对的成交历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/userTrades`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES | 交易对 |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| fromId | LONG | NO | 返回该fromId及之后的成交，缺省返回最近的成交 |
| limit | INT | NO | 返回的结果集数量 默认值:50 最大值:1000 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 如果`startTime`和`endTime`均不填，默认返回最近7天数据
> * `startTime`和`endTime`的最大间隔为7天
> * 参数 `fromId` 不能和`startTime` 与 `endTime`一起发送

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#响应示例 "响应示例的直接链接")

```
[  
    {  
        "symbol": "BTCUSDT",  
        "id": 67880589,  
        "orderId": 270093109,  
        "side": "SELL",  
        "price": "28511.00",  
        "qty": "0.010",  
        "realizedPnl": "2.58500000",  
        "quoteQty": "285.11000",  
        "commission": "-0.11404400",  
        "commissionAsset": "USDT",  
        "time": 1680688557875,  
        "buyer": false,  
        "maker": false,  
        "positionSide": "BOTH"  
    }  
]
```

[上一页

获取账户杠杆强制平仓记录(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders)[下一页

CM账户成交历史(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/CM-Account-Trade-List)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/UM-Account-Trade-List#响应示例)