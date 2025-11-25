<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount -->

* 统一账户专业版
* 账户接口
* 查询统一账户专业版穿仓借贷金额(USER\_DATA)

本页总览

# 查询统一账户专业版穿仓借贷金额 (USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#接口描述 "接口描述的直接链接")

查询统一账户专业版穿仓借贷金额

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#http请求 "HTTP请求的直接链接")

GET `/sapi/v1/portfolio/pmLoan`

## 请求权重(UID)[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#请求权重uid "请求权重(UID)的直接链接")

**500**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

> * 如果不存在统一账户专业版穿仓负债，amount显示为0

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#响应示例 "响应示例的直接链接")

```
{  
   "asset": "BUSD",     
   "amount":  "579.45", // 统一账户用户强平穿仓负债，单位为BUSD  
}
```

[上一页

偿还统一账户专业版穿仓负债](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Classic-Portfolio-Margin-Bankruptcy-Loan-Repay)[下一页

清还合约负余额(USER\_DATA)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Repay-futures-Negative-Balance)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#http请求)
* [请求权重(UID)](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#请求权重uid)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin-pro/account/Query-Classic-Portfolio-Margin-Bankruptcy-Loan-Amount#响应示例)