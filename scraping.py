# Import Packages and Modules
from requests import get
from bs4 import BeautifulSoup
from time import sleep
from time import time
# import webbrowser
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

# Prompt for ticker symbol (e.g. AAPL)
stock = input('Enter ticker symbol:')
# op = webdriver.ChromeOptions()
# #op.add_argument('headless')
# op.add_argument('--disable-blink-features=AutomationControlled')
# op.add_argument("--no-sandbox")
# op.add_argument("--disable-setuid-sandbox")
# op.add_argument("--remote-debugging-port=9222")  # this
# op.add_argument("--disable-dev-shm-using")
# op.add_argument("--disable-extensions")
# op.add_argument("--disable-gpu")
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=op)


# Set start time to measure the speed of the whole operation
start = time()

# Try scraping the data from finviz.com
#try:
    # Get html from finviz.com
# finviz_url = 'https://finviz.com/quote.ashx?t=' + stock
# # response = get(finviz_url)
# driver.get(finviz_url)
# sleep(3)
# rows = driver.find_elements(By.CLASS_NAME, 'table-dark-row')
# # resp = urlopen(finviz_url)
# # page_html = BeautifulSoup(response.text,'html.parser')
# # rows = page_html.find_all('tr', class_ = 'table-dark-row')

# # Find share float on finviz.com
# second_row = rows[1]
# finviz_float = second_row.find_elements(By.XPATH, './/td[@class="snapshot-td2"]')[4].get_attribute("textContent")
# #finviz_float = second_row.find_all('td', class_ = 'snapshot-td2')[4].text

# # Find short float (%) on finviz.com
# third_row = rows[2]
# #finviz_short_float = third_row.find_all('td', class_ = 'snapshot-td2')[4].text
# finviz_short_float = third_row.find_elements(By.XPATH, './/td[@class="snapshot-td2"]')[4].get_attribute("textContent")

# # Print results
# print('Finviz - Share Float: '+ finviz_float + ', Short Float: ' + finviz_short_float)

# If not available on finviz.com, print error message
# except:
#    print('Ticker symbol not available on finviz.com')

# Try scraping the data from shortsqueeze.com
#try:
    # Get html from shortsqueeze.com
sscom_url = 'http://shortsqueeze.com/?symbol=' + stock
response = get(sscom_url)
page_html = BeautifulSoup(response.text,'html.parser')

# Find share float on shortsqueeze.com
# table = page_html.find_all('table', attrs = {'width':'100%'})[8]
# sscom_float = table.find('td', attrs = {'align':'right'}).text

# Find short float on shortsqueeze.com
table = page_html.find_all('table', attrs = {'width':'100%'})[7]
sscom_short_float = table.find_all('td', attrs = {'align':'right'})[6].text.replace(" ","")
share_float = float(sscom_short_float.replace(',', ''))
share_float = str('float = M'), round(float(share_float) / 1000000, 1)
#share_float = round(float(share_float) / 1000000, 1)

# Print results
#print('shortsqueeze.com - Share Float: ' + sscom_float + ', Short Float:' + sscom_short_float)
print('shortsqueeze.com - Shares Float: ' + str(share_float))

# If not available on shortsqueeze.com, print error message
#except:
#    print('Ticker symbol not available on shortsqueeze.com')
    
# Calculate the time taken for the entire scraping operation
end = time()
print('Time taken: ' + str(round(end - start, 2)) + 's')

# Short pause to quickly read the share float and short float results, before opening the SEC filings webpage
sleep(2)

# Open SEC filings webpage
#webbrowser.open('https://www.sec.gov/cgi-bin/browse-edgar?CIK=' + stock + '&owner=exclude&action=getcompany')
