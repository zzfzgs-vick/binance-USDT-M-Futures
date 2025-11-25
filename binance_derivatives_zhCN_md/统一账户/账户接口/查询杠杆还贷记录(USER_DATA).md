<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record -->

* 统一账户
* 账户接口
* 查询杠杆还贷记录(USER-DATA)

本页总览

# 查询杠杆还贷记录(USER\_DATA)

## 接口描述[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#接口描述 "接口描述的直接链接")

查询杠杆还贷记录

## HTTP请求[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#http请求 "HTTP请求的直接链接")

GET `/papi/v1/margin/repayLoan`

## 请求权重[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#请求权重 "请求权重的直接链接")

**10**

## 请求参数[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| asset | STRING | YES |  |
| txId | LONG | NO | the `tranId` in `POST/papi/v1/repayLoan` |
| startTime | LONG | NO |  |
| endTime | LONG | NO |  |
| current | LONG | NO | 当前查询页。 开始值 1。 默认:1 |
| size | LONG | NO | Default:10 Max:100 |
| archived | STRING | NO | Default: `false`. Set to `true` for archived data from 6 months ago |
| recvWindow | LONG | NO | 赋值不能超过 60000 |
| timestamp | LONG | YES |  |

> * 必须发送txId 或 startTime，txId 优先
> * 响应返回为降序排列。
> * 查询时间范围最大不得超过30天。
> * 若startTime和endTime没传，则默认返回最近7天数据
> * 如果想查询6个月以前数据，设置 archived 为 true

## 响应示例[​](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#响应示例 "响应示例的直接链接")

```
{  
     "rows": [  
         {  
                "amount": "14.00000000",   //还款总额  
                "asset": "BNB",     
                "interest": "0.01866667",    //支付的利息  
                "principal": "13.98133333",   //支付的本金  
                "status": "CONFIRMED",   //状态: PENDING (等待执行), CONFIRMED (成功还款), FAILED (执行失败);  
                "timestamp": 1563438204000,  
                "txId": 2970933056  
         }  
     ],  
     "total": 1  
}
```

[上一页

查询杠杆借贷记录(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-Loan-Record)[下一页

查询自动清还合约负余额模式(USER-DATA)](/docs/zh-CN/derivatives/portfolio-margin/account/Get-Auto-repay-futures-Status)

* [接口描述](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#接口描述)
* [HTTP请求](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#http请求)
* [请求权重](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#请求权重)
* [请求参数](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#请求参数)
* [响应示例](/docs/zh-CN/derivatives/portfolio-margin/account/Query-Margin-repay-Record#响应示例)