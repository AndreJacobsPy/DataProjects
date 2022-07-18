import sqlite3 as sql
import os
import pandas as pd

if os.getcwd() != '/Users/andrejacobs/Desktop/DataProjects/financial market':
    os.chdir('/Users/andrejacobs/Desktop/DataProjects/financial market')

db = sql.connect('finance_db')
c = db.cursor()

c.execute("""create table if not exists financials (
        symbol text,
        name text,
        sector text,
        price float,
        price_earnings float,
        dividend_yield float,
        earnings_share float,
        annual_week_low float,
        annual_week_high float,
        market_cap float,
        epittda float,
        price_sales float,
        price_book float,
        sec_filings text
    )
""")

df = pd.read_csv('financials.csv')
df.columns = ['symbol',
        'name',
        'sector',
        'price',
        'price_earnings' ,
        'dividend_yield' ,
        'earnings_share' ,
        'annual_week_low' ,
        'annual_week_high' ,
        'market_cap' ,
        'epittda' ,
        'price_sales' ,
        'price_book' ,
        'sec_filings' ]

df.to_sql('financials', db, if_exists='append', index=False)
db.commit()
db.close()