<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail -->

* 统一账户
* 账户接口
* 获取CM账户信息(USER-DATA)

本页总览

# 获取CM账户信息(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#接口描述 "接口描述的直接链接")

获取现有CM账户资产和仓位信息

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#http请求 "HTTP请求的直接链接")

GET `/papi/v1/cm/account`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#响应示例 "响应示例的直接链接")

```
{  
    "assets": [  
        {  
            "asset": "BTC",  // 资产  
            "crossWalletBalance": "0.00241969",  // 全仓账户余额  
            "crossUnPnl": "0.00000000",  // 全仓持仓未实现盈亏  
            "maintMargin": "0.00000000",    // 维持保证金  
            "initialMargin": "0.00000000",  // 当前所需起始保证金  
            "positionInitialMargin": "0.00000000",  // 持仓所需起始保证金(基于最新标记价格)  
            "openOrderInitialMargin": "0.00000000",  // 当前挂单所需起始保证金(基于最新标记价格)e  
            "updateTime": 1625474304765 // 更新时间  
         }  
     ],  
     "positions": [  
         {  
            "symbol": "BTCUSD_201225",  
            "positionAmt":"0",    
            "initialMargin": "0",  
            "maintMargin": "0",  
            "unrealizedProfit": "0.00000000",  
            "positionInitialMargin": "0",  
            "openOrderInitialMargin": "0",  
            "leverage": "125",  
            "positionSide": "BOTH",  
            "entryPrice": "0.0",  
            "maxQty": "50",    
            "updateTime": 0  
        }  
     ]  
}
```

[上一页

获取UM账户信息(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Account-Detail)[下一页

UM账户配置(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Account-Config)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Get-CM-Account-Detail#响应示例)