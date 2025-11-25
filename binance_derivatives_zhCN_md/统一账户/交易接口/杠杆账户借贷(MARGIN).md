<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow -->

* 统一账户
* 交易接口
* 杠杆账户借贷(MARGIN)

本页总览

# 杠杆账户借贷(MARGIN)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#接口描述 "接口描述的直接链接")

申请借贷

## HTTP Request[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#http-request "HTTP Request的直接链接")

POST `/papi/v1/marginLoan`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#请求权重 "请求权重的直接链接")

**100**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| asset | STRING | YES |  |
| amount | DECIMAL | YES |  |
| recvWindow | LONG | NO | 赋值不能超过`60000` |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#响应示例 "响应示例的直接链接")

```
{  
    "tranId": 100000001 //transaction id  
}
```

[上一页

杠杆账户下单(TRADE)](/docs/zh-CN/derivatives/portfolio-margin/trade/New-Margin-Order)[下一页

杠杆账户归还借贷(MARGIN)](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Repay)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#接口描述)
* [HTTP Request](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#http-request)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/trade/Margin-Account-Borrow#响应示例)