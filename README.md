from HsiehBing/stockcrawler
## Stockcrawler
功能敘述: #為查詢股價(還有TSE，OTC，小台1，小台2)，P台股當日走勢，C當前匯率，F台股個當日買賣超，E盤後法人，K-K線，V虛擬貨幣價格，*為120日內走勢，**為30日內 走勢，美股大小寫都可以，盤後資訊(ETSE、EFB、EFS、EDB、EDS)，更新股號名稱對照UpDate
## 輸出介面 
主要分為文字輸出與圖像輸出，圖像輸出係透過imgur api顯示

## 功能對照

  | function        | 代碼   | python file          | 說明                              |
  | :----:          | :----: | :----:              | :----                             |
  | finainces       | #      | yfinaince.py        | 台股為yahoo爬蟲，美股為yfinance爬蟲 |
  | Vitual_Currency | V      | virtual_currency.py | 使用binance api                   |
  | Currency        | C      | currency.py         | 爬台灣銀行資訊                     |
  | glucose_graph   | *      | imgur.py            | 使用yfinance                      |
  | sTrendTrad      | F      | Trend_Trad.py       | yahoo爬蟲                         |
  | Draw_candle     | K      | candle.py           | 使用yfinance                      |
  | today_price     | P      | running_price.py    | yahoo爬蟲                         |
  | enddistr        | E      | After_hour.py       | 台灣證交所                         |\

UpDate 更新 r_Input.pkl、r_Output.pkl主要是以dictionary形式查詢股名對應股號  update.py
### 字體選擇 .font 用SimHei

## 安裝

```python
pip install -r requirements.txt
```

## 執行
執行前需要先更正Channel Access Token、與Channel Secret\
1. 可以直接啟動
```python
python3 app.py
```
2.可以透過gunicron啟動或加上-d 於背景執行 
```python
gunicorn -w 1 -b localhost:8080 app:app
```
*需搭配nginx或apache*

## MVC(Model Views Controllers)
- Model :負責資料存取
  - update.py、r_Input.pkl、r_Output.pkl、.fonts、fonts、SimHei.ttf \
  *ex ./Model/r_input.pkl*

- View:負責顯示資料\
  - static/tmp

- Controllers :負責處理訊息
  - yfinaince.py、virtual_currency.py、currency.py、imgur.py、Trend_Trad.py、candle.py、running_price.py、After_hour.py \
    *ex from Controllers.yfinance import**

## 更新日誌
