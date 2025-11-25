<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id -->

* 统一账户
* 账户接口
* 通过下载Id获取UM合约订单历史下载链接(USER-DATA)

本页总览

# 通过下载Id获取UM合约订单历史下载链接 (USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#接口描述 "接口描述的直接链接")

通过下载Id获取UM合约订单历史下载链接

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#http请求 "HTTP请求的直接链接")

GET `/papi/v1/um/order/asyn/id`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#请求权重 "请求权重的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| downloadId | STRING | YES | 通过下载id 接口获取 |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 下载链接有效期：24小时。

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#响应示例 "响应示例的直接链接")

> **响应:**

```
{  
	"downloadId":"545923594199212032", // 下载Id  
  	"status":"completed",     // 状态，枚举类型：completed 已完成，processing 处理中  
  	"url":"www.binance.com",  // 适配该笔ID请求的下载链接   
    "s3Link": null,        
  	"notified":true,          // 忽略  
  	"expirationTimestamp":1645009771000,  // 晚于该时间戳之后链接将自动失效  
  	"isExpired":null,  
}
```

> **或** (服务器仍在处理中会返回)

```
{  
	"downloadId":"545923594199212032",  
  	"status":"processing",  
  	"url":"",   
    "s3Link": null,  
  	"notified":false,  
  	"expirationTimestamp":-1  
  	"isExpired":null, 	  
}
```

[上一页

获取UM合约订单历史下载Id(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Order-History)[下一页

获取UM合约资金流水历史下载Id(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Download-Id-For-UM-Futures-Transaction-History)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Get-UM-Futures-Order-Download-Link-by-Id#响应示例)