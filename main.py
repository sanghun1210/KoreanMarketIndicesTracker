from pykrx import stock
from datetime import datetime, timedelta

def rename_stock_column(df):
    new_column_names = {
        '날짜' : 'date',
        '시가': 'open_price',
        '고가': 'high_price',
        '저가': 'low_price',
        '종가': 'trade_price',
        '거래량': 'volume',
    }
    df.rename(columns=new_column_names, inplace=True)
    return df

def main():
    current_date = datetime.now()
    date_300_days_ago = current_date - timedelta(days=300)
    after_string = current_date.strftime("%Y%m%d")
    before_string = date_300_days_ago.strftime("%Y%m%d")

    #코스피 지수 조회
    kospi_index = stock.get_index_ticker_list(market="KOSPI")
    print("KOSPI Indices:", kospi_index)
    df = stock.get_index_ohlcv_by_date(before_string, after_string, '1001')
    df.drop('거래대금', axis=1, inplace=True)
    df.drop('상장시가총액', axis=1, inplace=True)
    print(df.tail())
    df = rename_stock_column(df)
    df = df.rename_axis('date', axis=0)
    print(df.tail())

    df.to_csv('kospi_'+after_string+'.csv', index=True)


if __name__ == "__main__":
    main()

# 코스피 지수별 종가 조회
# for idx in kospi_index:
#     close_price = stock.get_index_ohlcv_by_date(before_string, after_string, idx)['종가']
#     print(f"Index: {idx}, Close Price: {close_price}")

# # 코스닥 지수 조회
# kosdaq_index = stock.get_index_ticker_list(market="KOSDAQ")
# print("KOSDAQ Indices:", kosdaq_index)

# # 코스닥 지수별 종가 조회
# for idx in kosdaq_index:
#     close_price = stock.get_index_ohlcv_by_date("yyyyMMdd", "yyyyMMdd", idx)['종가']
#     print(f"Index: {idx}, Close Price: {close_price}")