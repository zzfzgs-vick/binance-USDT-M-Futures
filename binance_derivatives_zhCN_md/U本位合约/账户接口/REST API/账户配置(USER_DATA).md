<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Config -->

* U本位合约
* 账户接口
* REST API
* 账户配置(USER-DATA)

本页总览

# 账户配置(USER\_DATA)

查询账户配置

## HTTP请求[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Config#http请求 "HTTP请求的直接链接")

GET `/fapi/v1/accountConfig`

## 请求权重[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Config#请求权重 "请求权重的直接链接")

**5**

## 请求参数[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Config#请求参数 "请求参数的直接链接")

| 名称 | 类型 | 是否必需 | 描述 |
| --- | --- | --- | --- |
| recvWindow | LONG | NO |  |
| timestamp | LONG | YES |  |

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Config#响应示例 "响应示例的直接链接")

```
{     
    "feeTier": 0,               // 费率等级  
    "canTrade": true,           // 是否可以交易  
    "canDeposit": true,         // 是否可以存款  
    "canWithdraw": true,        // 是否可以提现  
    "dualSidePosition": true,  
    "updateTime": 0,            // 忽略  
    "multiAssetsMargin": false,  
    "tradeGroupId": -1  
}
```

[上一页

用户手续费率(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/User-Commission-Rate)[下一页

交易对配置(USER-DATA)](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Symbol-Config)

* [HTTP请求](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Config#http请求)
* [请求权重](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Config#请求权重)
* [请求参数](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Config#请求参数)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/account/rest-api/Account-Config#响应示例)