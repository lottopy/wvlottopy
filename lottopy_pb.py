# WVLottopy: Matteo DiBiagio
from fractions import Fraction as frac
import pandas as pd
import requests
from collections import Counter


def get_data():
    # previous records which have since been removed from wvlottery.com's database
    df_old = pd.read_excel('./excel_lotto_records/lotto.xlsx')
    salvaged = df_old[['Date', 'Numbers', 'PB']]

    # Current web records 
    url = 'https://gateway.loyalty.wvlottery.com/services/jackpot/api/v1/jackpot-results?gameId=12&jackpotStatus=PAYABLE&size=500&sort=externalId,drawDate,desc&page='
    header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    }
    # Get web data, the new site pulls past draws from json 500 at a time
    web = {'Date': [], 'Numbers': [], 'PB': []}
    page = 0
    while True:
        r = requests.get(url + str(page), headers=header)
        data = r.json()
        for x in data['content']:
            web['Date'].append(x['drawingDate'])
            web['Numbers'].append('–'.join(str(n['data']) for n in x['resultData'] if n['type'] == 'REGULAR'))
            web['PB'].append([n['data'] for n in x['resultData'] if n['type'] == 'SPECIAL'][0])
        if data['last']:
            break
        page += 1
    dfs = [pd.DataFrame(web)]
    pd.set_option('display.max_rows', None)
    # Specifies no max rows, otherwise only shows 10 records
    df = pd.concat([dfs[0], salvaged], ignore_index=True)
    df2 = df[['Date', 'Numbers', 'PB']]
    date = list(df2['Date']) 
    nums = list(df2['Numbers'].astype('str')) 
    PBs = list(df2['PB'].astype('int'))
    return date, nums, PBs

date, nums, PBs = get_data()

# Formatting 
hyphenfree = []
for x in nums:
    hyphenfree.append(x.replace('–',', ')) 
splitlist = ", ".join(hyphenfree)
sep = splitlist.split(", ")

for n in range(0, 69):
    most_common = Counter(sep).most_common(5)
    likely_nums = [v[0] for v in most_common]
    frequency = [v[-1] for v in most_common]
    
for n in range(0, 26):
    most_common_pb = Counter(PBs).most_common(1)
    PB = [v[0] for v in most_common_pb]
    frequency_pb = [v[-1] for v in most_common_pb]

sorted_nums = sorted(likely_nums, key=lambda x: (len(x), x))
total_freq = sum(frequency + frequency_pb) 
Chance = frac(total_freq, 292201338) # Chance = number call freq / all possible numbers i.e. 292201338
Forecast = str(" - ".join(sorted_nums))

print(f"Likely numbers are . . .  {Forecast} PB: {PB}\n"
f"With percent chance of winning being {Chance}")