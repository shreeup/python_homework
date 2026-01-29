from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import json

####### Task 2
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")


title = driver.title # Find the title.  Parts of the header are accessed directly, not via find_element(), which only works on the body
print(title)

####### Task 3
results=[]
listitems = driver.find_elements(By.CSS_SELECTOR,'li.row.cp-search-result-item') # Find the first body element, typically only one
for listitem in listitems:
    titleelement = listitem.find_element(By.CSS_SELECTOR,'h3.cp-title') 
    titletext=titleelement.text
    authors = listitem.find_elements(By.CSS_SELECTOR,'span.cp-author-link') 
    authortexts=[]
    if len(authors) > 0:
       authortexts = ";".join([a.text for a in authors])  
    format_year_element = listitem.find_element(By.CSS_SELECTOR, 'div.manifestation-item-format-info-wrap span.display-info-primary')
    format_year_text = format_year_element.text
    results.append({
        "Title": titletext,
        "Author": authortexts, "Format-Year": format_year_text})
df = pd.DataFrame(results)
print(df)
######### Task 4
df.to_csv('get_books.csv')
with open('get_books.json', 'w') as json_file:
    json.dump(results, json_file, indent=4) #


