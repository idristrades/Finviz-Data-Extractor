# Finviz-Data-Extractor
Extracts data from finviz and shortsqueeze for a given ticker

# How to use
scraping.py <Ticker Name>

for eg; scraping.py META

This will show the Shares Float and Short Float for that ticker.

If it cannot pull the data from Finviz it will use shortsqueeze.com as a backup. As of now shortsqueeze.com data is not as updated but it shows how to retrieve it.
