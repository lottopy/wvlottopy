# WVLottopy: Matteo DiBiagio
from fractions import Fraction as frac
import pandas as pd
import requests
from collections import Counter

def get_data():
    # Old data from WVLottery.com
    df_old = pd.read_excel('./excel_lotto_records/daily4.xlsx')
    salvaged = df_old[['Date', 'Numbers']]

    url = 'https://wvlottery.com/draw-games/daily-4/?game-analyze=daily-4&what-to-search=historysearch&date-range=-1'
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }
    # Get web data
    r = requests.get(url, headers=header)
    dfs = list(pd.read_html(r.text))
    pd.set_option('display.max_rows', None)
    # Specifies no max rows, otherwise only shows 10 records
    df = pd.concat([dfs[0], salvaged], ignore_index=True)
    df2 = df[['Date', 'Numbers']]
    date = list(df2['Date']) 
    nums = list(df2['Numbers'].astype('str')) 
    return date, nums

date, nums = get_data()

# Formatting 
hyphenfree = []
for x in nums:
    hyphenfree.append(x.replace('–',', ')) 
splitlist = ", ".join(hyphenfree)
sep = splitlist.split(", ")

for n in range(0, 9):
    most_common= Counter(sep).most_common(4)
    likely_nums = [v[0] for v in most_common]
    frequency = [v[-1] for v in most_common]

sorted_nums = sorted(likely_nums)
total_freq = sum(frequency) 
Chance  = frac(total_freq, 10000) # Chance = number call freq / all possible numbers i.e. 10000
Forecast = str("-".join(sorted_nums))

print(f"Likely numbers are . . .  {Forecast}, \n"
f"With percent chance of winning being {Chance}")