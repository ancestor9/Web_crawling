# 주식투자분석: 삼성전자와 SK하이닉스
# requests, bs4, pandas, matplolib, 
# def, for, if 
# finance.yahoo.com/000660.KS/, finance.yahoo.com/005930.KS/ --> Historical Data
# 코드 구조화 by 함수 : html을 bs4(1) --> bs4로 dataframe(2) --> matplotlib로 시각화(3)

import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib  # 먼저 import 해야 함
matplotlib.use('Agg')  # GUI 백엔드 대신 Agg 사용
import matplotlib.pyplot as plt

def get_web_data(url: str) -> BeautifulSoup:
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, features='html.parser')

def extract_stock_data(soup: BeautifulSoup) -> pd.DataFrame:
    
    dates = []
    prices = []
    volumes = []
    rows = soup.find_all("tr")
    for row in rows[1:]:
        cells = row.find_all("td")
        if len(cells) == 7:
            date = pd.to_datetime(cells[0].text).date()
            price = int(cells[4].text.replace(',', '').replace('.00', ''))
            volume = int(cells[6].text.replace(',', ''))
            dates.append(date)
            prices.append(price)
            volumes.append(volume)
            
    return pd.DataFrame({'date' : dates, 'price': prices, 'volume': volumes})

# ------------ 2개 히사의 데이터 수집 후 시각화
stock_url = {
    'SK hynix' : 'https://finance.yahoo.com/quote/000660.KS/history/',
    'Samsung Electronics' : 'https://finance.yahoo.com/quote/005930.KS/history/'
}

# for stock_name, url in stock_url.items():
#     print(stock_name, url)
#     soup = get_web_data(url)
#     df = extract_stock_data(soup)
#     print(df.head())

def main():
    df = {}
    for stock_name, url in stock_url.items():
        print(stock_name, url)
        soup = get_web_data(url)
        df[stock_name] = extract_stock_data(soup)
        
        print(df[stock_name].head(10))

if __name__ == "__main__":
    main()
