# wvlottopy

THE WVLOTTOPY DEVELOPERS HAVE NO AFFILIATION WITH THE WEST VIRGINIA STATE LOTTERY

This script generates the most likely lottery numbers based off frequency of winning numbers.

Previously there were records dating back to 1992 that were removed by the website, which has lead me to rewrite and encourage the collaboration and sharing of this work. I have attached an excel file that includes the previous records. Originally excel functionality was stripped for performance but has been reimplemented. The excel files in this repo are only as new as the last commit. The most recent version is updated daily and can be downloaded from https://wvlotterypredictor.xyz/about/records if you want to stay up to date, just replace the excel_lotto_records folder with the one in the zip.

I am welcoming anyone who wants to to port it to their own state/country to do so. I currently have a website www.wvlotterypredictor.xyz hosting my numbers to be refreshed daily. Collaboration and suggestion to a more accurate algorithm is also welcome. I can be contacted about the project through my site email, on here, or on the Twitter linked on my site.

# Good luck!

# CHANGELOG 
- June 29th 2022: Added support for old data that was previously scrubbed from the lottery site. It is more accurate and includes more data than the previous one. Chance for daily3 is now bugged however due to the large amount of numbers and dates. This will be fixed soon.
- October 2026: wvlottery.com moved their past results to a new api so the scripts pull from that now. Added Cash Pop. The site only keeps about 3 years of draws (Cash Pop only 1) so records.py adds every new draw to the excel sheets when a script runs, that way the history keeps growing instead of getting lost again. Chance is now the actual odds of the ticket, which also fixes daily3.

# TODO: 
- Nothing right now, suggestions welcome



