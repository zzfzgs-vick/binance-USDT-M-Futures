<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Query-UM-Position-Information -->

* 统一账户
* 账户接口
* 用户 UM 持仓风险(USER-DATA)

本页总览

# 用户UM持仓风险(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-UM-Position-Information#接口描述 "接口描述的直接链接")

获取用户UM持仓风险

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-UM-Position-Information#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/positionRisk`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-UM-Position-Information#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-UM-Position-Information#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| symbol | STRING | NO |  |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 请与账户推送信息`ACCOUNT_UPDATE`配合使用，以满足您的及时性和准确性需求。
> * 对于单向持仓模式，仅会展示`BOTH`方向的持仓
> * 对于双向持仓模式，会展示所有`BOTH`，`LONG`，和`SHORT`方向的持仓

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-UM-Position-Information#响应示例 "响应示例的直接链接")

> * 单向持仓模式下:

```
 [  
    {  
        "entryPrice": "0.00000", // 开仓均价  
        "leverage": "10", // 当前杠杆倍数  
        "markPrice": "6679.50671178",   // 当前标记价格  
        "maxNotionalValue": "20000000", // 当前杠杆倍数允许的名义价值上限  
        "positionAmt": "0.000", // 头寸数量，符号代表多空方向, 正数为多，负数为空  
        "notional": "0",  
        "symbol": "BTCUSDT", // 交易对  
        "unRealizedProfit": "0.00000000", // 持仓未实现盈亏  
        "liquidationPrice": "6170.20509059",  
        "positionSide": "BOTH", // 持仓方向  
        "updateTime": 1625474304765   // 更新时间  
    }  
]
```

> * 双向持仓模式下(存在持仓才会返回):

```
[  
    {  
        "symbol": "BTCUSDT",  
        "positionAmt": "0.001",  
        "entryPrice": "22185.2",  
        "markPrice": "21123.05052574",  
        "unRealizedProfit": "-1.06214947",  
        "liquidationPrice": "6170.20509059",  
        "leverage": "4",  
        "maxNotionalValue": "100000000",  
        "positionSide": "LONG",  
        "notional": "21.12305052",  
        "updateTime": 1655217461579  
    },  
    {  
        "symbol": "BTCUSDT",  
        "positionAmt": "0.000",  
        "entryPrice": "0.0",  
        "markPrice": "21123.05052574",  
        "unRealizedProfit": "0.00000000",  
        "liquidationPrice": "6170.20509059",  
        "leverage": "4",  
        "maxNotionalValue": "100000000",  
        "positionSide": "SHORT",  
        "notional": "0",  
        "updateTime": 0  
    }  
]
```

[上一页

查询账户最大可转出额度(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw)[下一页

用户 CM 持仓风险(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Query-CM-Position-Information)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Query-UM-Position-Information#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Query-UM-Position-Information#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Query-UM-Position-Information#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Query-UM-Position-Information#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Query-UM-Position-Information#响应示例)