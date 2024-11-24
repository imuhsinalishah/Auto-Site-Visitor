from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import random
import requests
from bs4 import BeautifulSoup

# Selenium-based proxy scraper for dynamic sites
def fetch_proxies_free_proxy_list():
    url = "https://free-proxy-list.net/"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    proxies = []
    try:
        driver.get(url)
        print("Fetching proxies from free-proxy-list.net...")
        rows = driver.find_elements(By.CSS_SELECTOR, "#proxylisttable tbody tr")
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            if len(columns) >= 5 and columns[4].text.strip() == "elite proxy":
                proxy = f"{columns[0].text.strip()}:{columns[1].text.strip()}"
                proxies.append(proxy)
    except Exception as e:
        print(f"Error fetching from free-proxy-list.net: {e}")
    finally:
        driver.quit()
    return proxies

# Requests-based proxy scraper for spys.me
def fetch_proxies_spys_me():
    url = "https://spys.me/proxy.txt"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("Fetching proxies from spys.me...")
        lines = response.text.split("\n")
        proxies = [line.split()[0] for line in lines if line and line[0].isdigit()]
        return proxies
    except Exception as e:
        print(f"Error fetching from spys.me: {e}")
        return []

# Selenium-based proxy scraper for hidemy.name
def fetch_proxies_hidemy_name():
    url = "https://hidemy.name/en/proxy-list/"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-web-security")

    driver = webdriver.Chrome(options=chrome_options)
    proxies = []
    try:
        driver.get(url)
        print("Fetching proxies from hidemy.name...")
        rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            if len(columns) >= 7:  # Adjust based on table structure
                proxy = f"{columns[0].text.strip()}:{columns[1].text.strip()}"
                proxies.append(proxy)
    except Exception as e:
        print(f"Error fetching from hidemy.name: {e}")
    finally:
        driver.quit()
    return proxies

# Combine proxies from all sources
def fetch_all_proxies():
    proxies = []
    proxies.extend(fetch_proxies_free_proxy_list())
    proxies.extend(fetch_proxies_spys_me())
    proxies.extend(fetch_proxies_hidemy_name())
    print(f"Total proxies fetched: {len(proxies)}")
    return proxies

# Function to test if a proxy is working
def test_proxy(proxy):
    test_url = "https://httpbin.org/ip"  # HTTPS test
    try:
        response = requests.get(test_url, proxies={"http": f"http://{proxy}", "https": f"http://{proxy}"}, timeout=5)
        if response.status_code == 200:
            print(f"Proxy {proxy} supports HTTPS and is working.")
            return True
    except requests.RequestException:
        print(f"Proxy {proxy} failed HTTPS test.")
    return False


# Function to visit a URL using a proxy
def visit_url_with_proxy(url, proxy, delay=5):
    chrome_options = Options()
    chrome_options.add_argument(f"--proxy-server=http://{proxy}")
    chrome_options.add_argument("--ignore-certificate-errors")  # Ignore SSL errors
    chrome_options.add_argument("--disable-web-security")  # Disable web security
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(url)
        print(f"Visiting {url} using proxy {proxy}")

        # Simulate scrolling
        for _ in range(10):  # Scroll 10 times
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
            time.sleep(random.uniform(1, 3))  # Random delay between scrolls

        print("Completed scrolling.")
    except Exception as e:
        print(f"Error visiting URL with proxy {proxy}: {e}")
    finally:
        driver.quit()
        time.sleep(delay)


# Main function
def main():
    url = input("Enter the URL to visit: ")
    proxies = fetch_all_proxies()
    if not proxies:
        print("No proxies found!")
        return

    for proxy in proxies:
        if test_proxy(proxy):  # Use only working proxies
            visit_url_with_proxy(url, proxy)
        else:
            print(f"Skipping non-working proxy {proxy}")

if __name__ == "__main__":
    main()