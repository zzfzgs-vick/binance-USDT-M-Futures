<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage -->

* 统一账户专业版
* 行情接口
* 查询统一账户资产支持杠杆倍数(USER\_DATA)

本页总览

# 查询统一账户资产支持杠杆倍数(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#接口描述 "接口描述的直接链接")

查询统一账户资产支持杠杆倍数

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/portfolio/margin-asset-leverage`

## 请求权重(IP)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#请求权重ip "请求权重(IP)的直接链接")

**50**

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#响应示例 "响应示例的直接链接")

```
[  
   {  
       "asset": "USDC",  
       "leverage": 10  
   },  
   {  
       "asset": "USDT",  
       "leverage": 10  
   }  
]
```

[上一页

查询统一账户资产价格指数(MARKET\_DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data)[下一页

统一账户资产质押率(MARKET\_DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Classic-Portfolio-Margin-Collateral-Rate)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#http请求)
* [请求权重(IP)](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#请求权重ip)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin-pro/market-data/Get-Portfolio-Margin-Asset-Leverage#响应示例)