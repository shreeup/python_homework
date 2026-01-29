import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://owasp.org/Top10/")

# Wait until links are present
wait = WebDriverWait(driver, 10)

links = wait.until(
    EC.presence_of_all_elements_located(
        (
            By.XPATH,
            "//a[starts-with(normalize-space(text()), 'A') and contains(text(), ':2025')]"
        )
    )
)

vulnerabilities = []

for link in links:
    vulnerabilities.append({
        "title": link.text.strip(),
        "url": link.get_attribute("href")
    })

driver.quit()

# Verify output
print(vulnerabilities)

# Write CSV
with open("owasp_top_10.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "url"])
    writer.writeheader()
    writer.writerows(vulnerabilities)

print("owasp_top_10.csv written successfully")
