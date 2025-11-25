<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate -->

* 统一账户专业版
* 行情接口
* 统一账户资产质押率(MARKET\_DATA)

本页总览

# 统一账户资产质押率(MARKET\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#接口描述 "接口描述的直接链接")

统一账户资产质押率

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/portfolio/collateralRate`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#请求权重ip "请求权重(IP)的直接链接")

**50**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#请求参数 "请求参数的直接链接")

None

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#响应示例 "响应示例的直接链接")

```
[  
   {  
       "asset": "USDC",  
       "collateralRate": "1.0000" //质押率  
   },  
   {  
       "asset": "BUSD",  
       "collateralRate": "1.0000"  
   },  
]
```

[上一页

查询统一账户资产支持杠杆倍数(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage)[下一页

统一账户专业版资产阶梯质押率(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Portfolio-Margin-Pro-Tiered-Collateral-Rate)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#http请求)
* [请求权重(IP)](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#请求权重ip)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate#响应示例)