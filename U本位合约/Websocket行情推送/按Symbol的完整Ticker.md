<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams -->

* U本位合约
* Websocket行情推送
* 按 Symbol 的完整 Ticker

本页总览

# 按Symbol的完整Ticker

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#数据流描述 "数据流描述的直接链接")

按Symbol刷新的24小时完整ticker信息

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#stream-name "Stream Name的直接链接")

`<symbol>@ticker`

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#更新速度 "更新速度的直接链接")

**2000ms**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#响应示例 "响应示例的直接链接")

```
{  
  "e": "24hrTicker",  // 事件类型  
  "E": 123456789,     // 事件时间  
  "s": "BNBUSDT",      // 交易对  
  "p": "0.0015",      // 24小时价格变化  
  "P": "250.00",      // 24小时价格变化(百分比)  
  "w": "0.0018",      // 平均价格  
  "c": "0.0025",      // 最新成交价格  
  "Q": "10",          // 最新成交价格上的成交量  
  "o": "0.0010",      // 24小时内第一比成交的价格  
  "h": "0.0025",      // 24小时内最高成交价  
  "l": "0.0010",      // 24小时内最低成交价  
  "v": "10000",       // 24小时内成交量  
  "q": "18",          // 24小时内成交额  
  "O": 0,             // 统计开始时间  
  "C": 86400000,      // 统计关闭时间  
  "F": 0,             // 24小时内第一笔成交交易ID  
  "L": 18150,         // 24小时内最后一笔成交交易ID  
  "n": 18151          // 24小时内成交数  
}
```

[上一页

全市场的完整Ticker](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Tickers-Streams)[下一页

全市场的精简Ticker](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream)

* [数据流描述](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#数据流描述)
* [Stream Name](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#stream-name)
* [更新速度](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#更新速度)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Ticker-Streams#响应示例)