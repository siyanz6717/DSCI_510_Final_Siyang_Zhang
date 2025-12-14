# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Clearing up the directory
current_folder = os.path.dirname(os.path.abspath(__file__))
project = os.path.dirname(current_folder)
raw_dir = os.path.join(project, "data", "raw")

# Mimic Header
headers = {"User-Agent": "Mozilla/5.0"}

# Scraping Cost of Living
url_col = "https://www.numbeo.com/cost-of-living/rankings_current.jsp"
soup_col = BeautifulSoup(requests.get(url_col, headers=headers).content, 'html.parser')
table_col = soup_col.find('table', {'id': 't2'})

rows_col = []
for tr in table_col.find('tbody').find_all('tr'):
    cells = [td.get_text(strip=True) for td in tr.find_all('td')]
    if cells:
        rows_col.append(cells)

cols_col = [th.get_text(strip=True) for th in table_col.find('thead').find_all('th')]
pd.DataFrame(rows_col, columns=cols_col).to_csv(os.path.join(raw_dir, "cost_of_living.csv"), index=False)
# Scraping Quality of Life
url_qol = "https://www.numbeo.com/quality-of-life/rankings_current.jsp"
soup_qol = BeautifulSoup(requests.get(url_qol, headers=headers).content, 'html.parser')
table_qol = soup_qol.find('table', {'id': 't2'})

rows_qol = []
for tr in table_qol.find('tbody').find_all('tr'):
    cells = [td.get_text(strip=True) for td in tr.find_all('td')]
    if cells:
        rows_qol.append(cells)

cols_qol = [th.get_text(strip=True) for th in table_qol.find('thead').find_all('th')]
pd.DataFrame(rows_qol, columns=cols_qol).to_csv(os.path.join(raw_dir, "quality_of_life.csv"), index=False)