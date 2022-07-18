import sqlite3
import pandas as pd
import numpy as np
from csv import reader
import os

if os.getcwd() != '/Users/andrejacobs/Desktop/snapbrillia-ai/source':
    os.chdir('/Users/andrejacobs/Desktop/snapbrillia-ai/source')

with open('job_skills.csv', 'r') as my_data:
    csv_reader = reader(my_data)
    data = list(csv_reader)[1:]

db = sqlite3.connect('job_db')
c = db.cursor()

c.execute('''create table google_jobs (
    company text,
    title text,
    category text,
    location text,
    responsibilities text,
    minimum_qualifications text,
    preferred_qualifications text)''')

c.executemany('''insert into google_jobs values (?,?,?,?,?,?,?)''', data)

db.commit()
c.close()