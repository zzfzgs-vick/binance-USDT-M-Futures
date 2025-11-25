<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow -->

* 统一账户
* 账户接口
* 查询账户最大可借贷额度 (USER-DATA)

本页总览

# 查询账户最大可借贷额度 (USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#接口描述 "接口描述的直接链接")

查询账户最大可借贷额度

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/maxBorrowable`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| asset | STRING | YES |  |
| recvWindow | LONG | NO | 赋值不能超过 `60000` |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#响应示例 "响应示例的直接链接")

```
{  
  "amount": "1.69248805", // 系统可借充足情况下用户账户当前最大可借额度  
  "borrowLimit": "60" // 平台限制的用户当前等级可以借的额度  
}
```

[上一页

查询账户信息(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Account-Information)[下一页

查询账户最大可转出额度(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-Max-Withdraw)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Margin-Max-Borrow#响应示例)