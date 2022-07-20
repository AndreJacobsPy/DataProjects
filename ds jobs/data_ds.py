import sqlite3 as sql
import pandas as pd
import os

if os.getcwd() != '/Users/andrejacobs/Desktop':
    os.chdir('/Users/andrejacobs/Desktop')

df = pd.read_csv('Uncleaned_DS_jobs.csv')
df.columns = ['Index', 'JobTitle', 'SalaryEstimate', 'JobDescription', 'Rating',
              'CompanyName', 'Location', 'Headquarters', 'Size', 'Founded',
              'TypeOfOwnership', 'Industry', 'Sector', 'Revenue', 'Competitors']
print(df.columns)
print(df.dtypes)

os.chdir('DataProjects/ds jobs')

db = sql.connect('dsjobs')
c = db.cursor()

df.to_sql('jobs', db, index=False)

db.commit()

c.execute('select * from jobs;')
print(c.fetchone())

db.close()


