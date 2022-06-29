# WVLottopy megamil: Matteo DiBiagio
from fractions import Fraction as frac
import pandas as pd
import requests
from collections import Counter

def get_data():
    # previous records which have since been removed from wvlottery.com's database
    df_old = pd.read_excel('./excel_lotto_records/lotto_megamil.xlsx')
    salvaged = df_old[['Date', 'Numbers', 'MB']]

    url = 'https://wvlottery.com/draw-games/mega-millions/?game-analyze=mega-millions&what-to-search=historysearch&date-range=-1'
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    # Get web data
    r = requests.get(url, headers=header)
    dfs = pd.read_html(r.text)
    pd.set_option('display.max_rows', None)
    # Specifies no max rows, otherwise only shows 10 records
    df = dfs[0].append(salvaged, ignore_index=True)
    df2 = df[['Date', 'Numbers', 'MB', 'MP']]
    date = list(df2['Date']) 
    nums = list(df2['Numbers'].astype('str')) 
    MBs = list(df2['MB'].astype('int'))
    return date, nums, MBs

date, nums, MBs = get_data()

# Formatting 
hyphenfree = []
for x in nums:
    hyphenfree.append(x.replace('–',', ')) 
splitlist = ", ".join(hyphenfree)
sep = splitlist.split(", ")

for n in range(0, 70):
    most_common= Counter(sep).most_common(5)
    likely_nums = [v[0] for v in most_common]
    frequency = [v[-1] for v in most_common]
    
for n in range(0, 25):
    most_common_mb = Counter(MBs).most_common(1)
    MB = [v[0] for v in most_common_mb]
    frequency_mb = [v[-1] for v in most_common_mb]

sorted_nums = sorted(likely_nums)
total_freq = sum(frequency + frequency_mb) 
Chance = frac(total_freq, 302575350) # Chance = number call freq / all possible numbers i.e. 11238513
Winning_Numbers = str("-".join(sorted_nums))

print(f"Likely numbers are . . .  {Winning_Numbers} MB: {MB}\n"
f"With percent chance of winning being {Chance}")