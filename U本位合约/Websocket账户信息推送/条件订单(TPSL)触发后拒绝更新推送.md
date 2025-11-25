<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Conditional-Order-Trigger-Reject -->

* U本位合约
* Websocket账户信息推送
* 条件订单（TPSL）触发后拒绝更新推送

本页总览

# 条件订单(TP/SL)触发后拒绝更新推送

## 事件描述[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Conditional-Order-Trigger-Reject#事件描述 "事件描述的直接链接")

`CONDITIONAL_ORDER_TRIGGER_REJECT` 在止盈止损单触发后被拒绝时推送

## 事件类型[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Conditional-Order-Trigger-Reject#事件类型 "事件类型的直接链接")

`CONDITIONAL_ORDER_TRIGGER_REJECT`

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Conditional-Order-Trigger-Reject#响应示例 "响应示例的直接链接")

```
{  
    "e":"CONDITIONAL_ORDER_TRIGGER_REJECT",      // 事件类型  
    "E":1685517224945,      // 事件时间  
    "T":1685517224955,      // 撮合时间  
    "or":{  
      "s":"ETHUSDT",      // 交易对  
      "i":155618472834,      // 订单号  
      "r":"Due to the order could not be filled immediately, the FOK order has been rejected. The order will not be recorded in the order history",      // 拒绝原因  
     }  
}
```

[上一页

网格更新推送](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-GRID-UPDATE)[下一页

条件订单交易更新推送](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Algo-Order-Update)

* [事件描述](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Conditional-Order-Trigger-Reject#事件描述)
* [事件类型](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Conditional-Order-Trigger-Reject#事件类型)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/user-data-streams/Event-Conditional-Order-Trigger-Reject#响应示例)