from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Enable headless mode
options.add_argument('--disable-gpu')  # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080')  # Optional, set window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
driver.get("https://en.wikipedia.org/wiki/Web_scraping")


title = driver.title # Find the title.  Parts of the header are accessed directly, not via find_element(), which only works on the body
print(title)

body = driver.find_element(By.CSS_SELECTOR,'body') # Find the first body element, typically only one
if body:
    links = body.find_elements(By.CSS_SELECTOR,'a') # Find all the links in the body.
    if len(links) > 0:
        print("href: ", links[0].get_attribute('href'))  # getting the value of an attribute



main_div = body.find_element(By.CSS_SELECTOR,'div[id="mw-content-text"]')
if main_div:
    bolds = main_div.find_elements(By.CSS_SELECTOR,'b')
    if len(bolds) > 0:
        print("bolds: ",bolds[0].text)

# Extract all images with their src attributes
images = [(img.get_attribute('src')) for img in body.find_elements(By.CSS_SELECTOR,'img[src]')] # all img elements with a src attribute
print("Image Sources:", images)
# hmm, this example uses a list comprehension.  We haven't talked about those.  This is the same as:
image_entries = driver.find_elements(By.CSS_SELECTOR,'img[src]')
images = []
for img in image_entries:
    images.append(img.get_attribute('src'))

print("Image Sources:", images)


# li: <li class="row cp-search-result-item" data-test-id="searchResultItem" style="order:0" data-key="search-result-item">

# title: <h3 class="cp-title">

# author: <span class="cp-author-link"><span><a target="_parent" rel="noopener noreferrer" class="author-link" data-key="author-link" href="/v2/search?origin=core-catalog-explore&amp;query=Iris%20Acevedo%20A.&amp;searchType=author">Iris Acevedo A.</a> • </span><span><a target="_parent" rel="noopener noreferrer" class="author-link" data-key="author-link" href="/v2/search?origin=core-catalog-explore&amp;query=Spanishonline%2C%20Costarica&amp;searchType=author">Spanishonline, Costarica</a></span></span>

# format and year: <div class="manifestation-item-format-info-wrap"><a class="manifestation-item-link" href="/v2/record/S981C18115836" target="_parent" lang="en" rel="noopener" data-test-id="item-link-S981C18115836" data-key="bib-manifestation-item-link"><div class="cp-format-info"><span aria-hidden="true" class="display-info"><span class="display-info-primary">eBook<!-- -->, 2025<!-- --> — Spanish</span><span class="call-number"></span></span><span class="cp-screen-reader-message">eBook, 2025. Language: Spanish</span></div></a><div class="manifestation-item-availability-block-wrap"><a class="cp-availability-bib-block" href="https://www.hoopladigital.com/title/18115836" rel="noopener noreferrer" target="_blank"><span aria-hidden="true">Check out now on Hoopla<!-- --> <svg aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg" class="cp-svg icon-svg-new-window icon-new-window" height="24" viewBox="0 0 24 24" width="24"><path clip-rule="evenodd" d="M19 19H5V5H12V3H5C3.89 3 3 3.9 3 5V19C3 20.1 3.89 21 5 21H19C20.1 21 21 20.1 21 19V12H19V19ZM14 3V5H17.59L7.76 14.83L9.17 16.24L19 6.41V10H21V3H14Z" fill="currentColor" fill-rule="evenodd"></path></svg></span><span class="cp-screen-reader-message">Check out now on Hoopla, opens a new window</span></a></div></div>