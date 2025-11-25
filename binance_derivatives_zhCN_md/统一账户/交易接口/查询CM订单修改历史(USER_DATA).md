<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Modify-Order-History -->

* 统一账户
* 交易接口
* 查询CM订单修改历史(USER\_DATA)

本页总览

# 查询CM订单修改历史(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Modify-Order-History#接口描述 "接口描述的直接链接")

查询CM订单修改历史

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Modify-Order-History#http请求 "HTTP请求的直接链接")

GET `/papi/v1/cm/orderAmendment`

## 请求权重(Order)[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Modify-Order-History#请求权重order "请求权重(Order)的直接链接")

**1**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Modify-Order-History#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 类型 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | YES | 交易对 |
| orderId | LONG | NO | 系统订单号 |
| origClientOrderId | STRING | NO | 用户自定义的订单号 |
| startTime | LONG | NO | 起始时间 |
| endTime | LONG | NO | 结束时间 |
| limit | INT | NO | 默认值 50, 最大值 100 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 至少需要发送 `orderId` 与 `origClientOrderId`中的一个，同时发送则以 orderId 为准

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Modify-Order-History#响应示例 "响应示例的直接链接")

```
[  
    {  
        "amendmentId": 5363,    // 修改记录号  
        "symbol": "BTCUSD_PERP",  
        "pair": "BTCUSD",  
        "orderId": 20072994037,  
        "clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
        "time": 1629184560899,  // 修改时间  
        "amendment": {  
            "price": {  
                "before": "30004",  
                "after": "30003.2"  
            },  
            "origQty": {  
                "before": "1",  
                "after": "1"  
            },  
            "count": 3  // 修改记数，代表该修改记录是这笔订单第几次修改  
        }  
    },  
    {  
        "amendmentId": 5361,  
        "symbol": "BTCUSD_PERP",  
        "pair": "BTCUSD",  
        "orderId": 20072994037,  
        "clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
        "time": 1629184533946,  
        "amendment": {  
            "price": {  
                "before": "30005",  
                "after": "30004"  
            },  
            "origQty": {  
                "before": "1",  
                "after": "1"  
            },  
            "count": 2  
        }  
    },  
    {  
        "amendmentId": 5325,  
        "symbol": "BTCUSD_PERP",  
        "pair": "BTCUSD",  
        "orderId": 20072994037,  
        "clientOrderId": "LJ9R4QZDihCaS8UAOOLpgW",  
        "time": 1629182711787,  
        "amendment": {  
            "price": {  
                "before": "30002",  
                "after": "30005"  
            },  
            "origQty": {  
                "before": "1",  
                "after": "1"  
            },  
            "count": 1  
        }  
    }  
]
```

[上一页

查询UM订单修改历史(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-UM-Modify-Order-History)[下一页

获取账户杠杆强制平仓记录(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-Users-Margin-Force-Orders)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Modify-Order-History#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Modify-Order-History#http请求)
* [请求权重(Order)](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Modify-Order-History#请求权重order)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Modify-Order-History#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Query-CM-Modify-Order-History#响应示例)