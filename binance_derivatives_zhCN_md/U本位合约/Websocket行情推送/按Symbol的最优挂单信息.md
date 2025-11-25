<!-- Source: https://developers.binance.com/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams -->

* U本位合约
* Websocket行情推送
* 按 Symbol 的最优挂单信息

本页总览

# 按Symbol的最优挂单信息

## 数据流描述[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#数据流描述 "数据流描述的直接链接")

实时推送指定交易对最优挂单信息

## Stream Name[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#stream-name "Stream Name的直接链接")

`<symbol>@bookTicker`

**注意：** 响应消息不包含RPI订单，其不可见。

## 更新速度[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#更新速度 "更新速度的直接链接")

**实时**

## 响应示例[​](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#响应示例 "响应示例的直接链接")

```
{  
  "e":"bookTicker",		// 事件类型  
  "u":400900217,     	// 更新ID  
  "E": 1568014460893,	// 事件推送时间  
  "T": 1568014460891,	// 撮合时间  
  "s":"BNBUSDT",     	// 交易对  
  "b":"25.35190000", 	// 买单最优挂单价格  
  "B":"31.21000000", 	// 买单最优挂单数量  
  "a":"25.36520000", 	// 卖单最优挂单价格  
  "A":"40.66000000"  	// 卖单最优挂单数量  
}
```

[上一页

全市场的精简Ticker](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/All-Market-Mini-Tickers-Stream)[下一页

全市场最优挂单信息](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/All-Book-Tickers-Stream)

* [数据流描述](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#数据流描述)
* [Stream Name](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#stream-name)
* [更新速度](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#更新速度)
* [响应示例](/docs/zh-CN/derivatives/usds-margined-futures/websocket-market-streams/Individual-Symbol-Book-Ticker-Streams#响应示例)