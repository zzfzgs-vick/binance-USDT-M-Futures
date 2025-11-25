<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/convert/Accept-Quote -->

* U本位合约
* 合约钱包闪兑
* 接受报价(TRADE)

本页总览

# 接受报价(TRADE)

## 接口描述[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Accept-Quote#接口描述 "接口描述的直接链接")

通过 quote ID 来接受报价。

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Accept-Quote#http请求 "HTTP请求的直接链接")

POST `/fapi/v1/convert/acceptQuote`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Accept-Quote#请求权重 "请求权重的直接链接")

**200(IP)**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Accept-Quote#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| quoteId | STRING | YES |  |
| recvWindow | LONG | NO | 此值不能大于 60000 |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/convert/Accept-Quote#响应示例 "响应示例的直接链接")

```
{  
  "orderId":"933256278426274426",  
  "createTime":1623381330472,  
  "orderStatus":"PROCESS" //PROCESS/ACCEPT_SUCCESS/SUCCESS/FAIL  
}
```

[上一页

发送获取报价请求(USER\_DATA)](/docs/zh-CN/derivatives/usds-margined-futures/convert/Send-quote-request)[下一页

查询订单状态(USER\_DATA)](/docs/zh-CN/derivatives/usds-margined-futures/convert/Order-Status)

* [接口描述](/docs/zh-CN/derivatives/usds-margined-futures/convert/Accept-Quote#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/convert/Accept-Quote#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/convert/Accept-Quote#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/convert/Accept-Quote#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/convert/Accept-Quote#响应示例)