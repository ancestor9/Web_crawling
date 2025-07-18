# 주식투자분석: 삼성전자와 SK하이닉스 https://www.youtube.com/watch?v=u8YdqOqcUsg&t=151s 
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

stock_url = 'https://finance.yahoo.com/quote/000660.KS/history/'

# response = requests.get(url=stock_url)
# print(response)
# -----------
# headers = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get(url=stock_url, headers=headers)
# print(response)
# soup = BeautifulSoup(response.text, features= 'html.parser')
# print(soup)

# ------- html을 bs4(1)
# print(type(stock_url))

def get_web_data(url: str) -> BeautifulSoup:
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    return BeautifulSoup(response.text, features='html.parser')

# soup = get_web_data(stock_url)
# print(soup)

# -------------- bs4로 dataframe(2) 
# rows = soup.find_all("tr")
# print(rows)
# print(type(rows))

# for row in rows:
#     print(row)

# for row in rows[1:5]:
#     # print(row)
#     cells = row.find_all("td")
#     # print(cells)
#     # print(len(cells))
#     if len(cells) == 7:
#         # date = cells[0]
#         date = pd.to_datetime(cells[0].text).date() # pandas에서 날짜로 변경
#         date = pd.to_datetime(date).strftime('%Y-%m-%d') 
#         print(date)
#         price = cells[4].text
#         price = cells[4].text.replace(',', '').replace('.00', '')
#         print(price)

# print(len(rows[1:]))

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


# df = extract_stock_data(soup)
# print(df)
# ------------matplotlib로 시각화(3)
# import matplotlib
# matplotlib.use('Agg')  # GUI 백엔드 대신 Agg 사용
# import matplotlib.pyplot as plt

# plt.plot(df['date'], df['price'], color='blue', label='Price')
# plt.show()

# # GUI 없이 저장
# plt.savefig("plot.png")  # PNG 파일로 저장
# print("그래프가 plot.png 파일로 저장되었습니다.")

def plot_stock_data(df: pd.DataFrame) -> None:
    plt.figure(figsize=(14, 7))

    # Plotting stock price
    plt.subplot(2, 1, 1)
    plt.plot(df['date'], df['price'], color='blue', label='Price')
    plt.title('Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.xticks(rotation=45)
    plt.legend()

    # Plotting volume
    plt.subplot(2, 1, 2)
    plt.bar(df['date'], df['volume'], color='orange', label='Volume')
    plt.title('Stock Volume Over Time')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.xticks(rotation=45)
    plt.legend()

    plt.tight_layout()
    
    plt.savefig("skhinix1_plot.png")
    # plt.show()

# # Call the plotting function
# soup = get_web_data(stock_url)
# stock_data = extract_stock_data(soup)
# plot_stock_data(stock_data)


# ------------- 마무리(4)

def main():
    soup = get_web_data(stock_url)
    stock_data = extract_stock_data(soup)
    plot_stock_data(stock_data)

if __name__ == "__main__":
    main()
