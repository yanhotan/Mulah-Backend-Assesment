from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime

def scrape_the_verge():
    options = webdriver.ChromeOptions()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    
    url = "https://www.theverge.com/"
    driver.get(url)
    time.sleep(10)  # Wait for the page to load

    articles = []
    try:
        article_elements = driver.find_elements(By.XPATH, "//div[@class='c-entry-box--compact__body']")
        for article in article_elements:
            link = article.find_element(By.TAG_NAME, "a")
            title = link.text.strip()
            article_link = link.get_attribute("href")
            
            driver.get(article_link)
            time.sleep(3)

            try:
                date_element = driver.find_element(By.XPATH, "//time")
                datetime_str = date_element.get_attribute("datetime")
                article_date = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")
                articles.append((article_date, title, article_link))
            except Exception:
                continue

    except Exception as e:
        print("Error during scraping:", e)

    driver.quit()
    return articles
