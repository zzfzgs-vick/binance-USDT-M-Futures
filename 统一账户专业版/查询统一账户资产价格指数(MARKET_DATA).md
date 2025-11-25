<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin-pro/market-data -->

* 统一账户专业版
* 行情接口
* 查询统一账户资产价格指数(MARKET\_DATA)

本页总览

# 查询统一账户资产价格指数(MARKET\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#接口描述 "接口描述的直接链接")

查询统一账户资产价格指数

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/portfolio/asset-index-price`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#请求权重ip "请求权重(IP)的直接链接")

传asset为**1** 或不传asset**50**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| asset | STRING | NO |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#响应示例 "响应示例的直接链接")

```
[  
   {  
       "asset": "BTC",  
       "assetIndexPrice": "28251.9136906",  //USD价格指数  
       "time": 1683518338121  
   }  
]
```

[上一页

基本信息](/docs/zh-CN/derivatives/portfolio-margin-pro/general-info)[下一页

查询统一账户资产支持杠杆倍数(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#http请求)
* [请求权重(IP)](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#请求权重ip)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data#响应示例)