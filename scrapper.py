import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
from urllib.parse import urljoin

today = date.today()
tomorrow = today + timedelta(days=1)
today_str = today.strftime("%d-%m-%Y")
tomorrow_str = tomorrow.strftime("%d-%m-%Y")

print(f"I am searching for power cut news for '{today_str}' or '{tomorrow_str}'.")

index_url = "https://www.livechennai.com/powercut_schedule.asp"
base_url = "https://www.livechennai.com/"
target_link = None

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

print(f"Fetching data from {index_url}...")

try:
    response = requests.get(index_url, headers=headers)
    response.raise_for_status() 
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        exit(1)
        
except requests.RequestException as e:
    print(f"Error occurred while fetching data: {e}")
    exit(1)

news_content_wrapper = soup.find('div', class_='news-content-wrapper')

if not news_content_wrapper:
    print("Could not find news content wrapper div on the page")
    exit(1)

# Safely access table rows only if we found the wrapper
table_rows = news_content_wrapper.find_all('tr')

if not table_rows:
    print("No table rows found in the news content")
    exit(1)

for row in table_rows:

    link_tag = row.find('a')

    if link_tag:
        link_text = link_tag.get_text()

        is_power_cut_link = "power cut" in link_text.lower()
        is_for_today = today_str in link_text
        is_for_tomorrow = tomorrow_str in link_text

        if is_power_cut_link and (is_for_today or is_for_tomorrow):
            print(f"Match Found! -> {link_text.strip()}")

            relative_path = link_tag['href']
            target_link = urljoin(base_url, relative_path)
            break

if target_link:
    print(f"Proceeding to scrape details from: {target_link}")
    try:
        response_detail = requests.get(target_link, headers=headers)
        response_detail.raise_for_status()
        soup_detail = BeautifulSoup(response_detail.text, 'html.parser')
        
        content_div = soup_detail.find('div', class_='news-content')
        
        if content_div:
            powercut_info = content_div.get_text(separator='\n').strip()
            print("\n--- POWER CUT SCHEDULE ---")
            print(powercut_info)
        else:
            print("Could not find the content div on the detail page.")

    except requests.RequestException as e:
        print(f"Error occurred while fetching detail page: {e}")

else:
    print("\nNo power cut schedule link was found for today or tomorrow.")
