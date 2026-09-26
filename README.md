# wvlottopy

THE WVLOTTOPY DEVELOPERS HAVE NO AFFILIATION WITH THE WEST VIRGINIA STATE LOTTERY

This script generates the most likely lottery numbers based off frequency of winning numbers.

Previously there were records dating back to 1992 that were removed by the website, which has lead me to rewrite and encourage the collaboration and sharing of this work. I have attached an excel file that includes the previous records. Originally excel functionality was stripped for performance but has been reimplemented.

I am welcoming anyone who wants to to port it to their own state/country to do so. I currently have a website www.wvlotterypredictor.xyz hosting my numbers to be refreshed daily. Collaboration and suggestion to a more accurate algorithm is also welcome. I can be contacted about the project through my site email, on here, or on the Twitter linked on my site.

# How the site works
- Each game has its own script. It pulls every past draw from the WV Lottery results api (the same one wvlottery.com uses for its past draws page), adds the older records from the excel files where there are any, and counts how often each number has been drawn. The chance shown is the actual odds of that ticket hitting, every ticket has the same odds so the forecast is just going with the numbers that have been called the most.
- On the site the scripts write their numbers to a csv instead of printing them. cron runs each one about 45 minutes after that game's drawing so the new numbers are already posted.
- The site itself is Django served by gunicorn behind nginx. It reads the csv files for the home page and caches the page in redis, which gets cleared every hour.

# Good luck!

# CHANGELOG 
- September 26th 2026: wvlottery.com was rebuilt and the old history tables are gone, so every script now pulls past draws from the json results api the new site uses. Added Cash Pop. Updated Mega Millions odds for the 2025 changes.
- September 26th 2026 (later): The excel records were never actually getting counted (they use - and the site used –), they are now. Numbers that cant be drawn anymore since the ball ranges changed get skipped. Chance is now the real odds of the forecast ticket winning instead of the frequency number, Daily3 and Daily4 are the odds for a box play.
- June 29th 2022: Added support for old data that was previously scrubbed from the lottery site. It is more accurate and includes more data than the previous one. Chance for daily3 is now bugged however due to the large amount of numbers and dates. This will be fixed soon.
