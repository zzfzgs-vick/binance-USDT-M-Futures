<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream -->

* U本位合约
* Websocket行情推送
* 按Symbol的精简 Ticker

本页总览

# 按交易对的精简Ticker

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#数据流描述 "数据流描述的直接链接")

按Symbol刷新的24小时精简ticker信息.

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#stream-name "Stream Name的直接链接")

`<symbol>@miniTicker`

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#更新速度 "更新速度的直接链接")

**2s**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#响应示例 "响应示例的直接链接")

```
  {  
    "e": "24hrMiniTicker",  // 事件类型  
    "E": 123456789,         // 事件时间(毫秒)  
    "s": "BNBUSDT",          // 交易对  
    "c": "0.0025",          // 最新成交价格  
    "o": "0.0010",          // 24小时前开始第一笔成交价格  
    "h": "0.0025",          // 24小时内最高成交价  
    "l": "0.0010",          // 24小时内最低成交价  
    "v": "10000",           // 成交量  
    "q": "18"               // 成交额  
  }
```

[上一页

连续合约 K 线](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Continuous-Contract-Kline-Candlestick-Streams)[下一页

全市场的完整Ticker](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Tickers-Streams)

* [数据流描述](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#数据流描述)
* [Stream Name](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#stream-name)
* [更新速度](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#更新速度)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Mini-Ticker-Stream#响应示例)