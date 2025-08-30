import os
import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
from urllib.parse import urljoin

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

def send_telegram_message(message: str):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram bot token or chat ID not set in environment variables.")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print(f"Failed to send message via Telegram: {response.text}")
    except Exception as e:
        print(f"Exception occurred while sending Telegram message: {e}")

today = date.today()
tomorrow = today + timedelta(days=1)
today_str = today.strftime("%d-%m-%Y")
tomorrow_str = tomorrow.strftime("%d-%m-%Y")

print(f"I am searching for power cut news for '{tomorrow_str}'.")

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

news_cards = news_content_wrapper.find_all('div', class_='card mb-3 bg-color')

if not news_cards:
    print("No news cards found in the news content")
    exit(1)

for card in news_cards:
    title_tag = card.find('h5', class_='card-title')
    if title_tag:
        link_tag = title_tag.find('a')
        if link_tag:
            link_text = link_tag.get_text()

            is_power_cut_link = "power shutdown" in link_text.lower() or "power cut" in link_text.lower()
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
            # Send power cut info to Telegram
            send_telegram_message(f"<b>Power Cut Schedule:</b>\n{powercut_info}")
        else:
            print("Could not find the content div on the detail page.")

    except requests.RequestException as e:
        print(f"Error occurred while fetching detail page: {e}")

else:
    print("\nNo power cut schedule link was found for today or tomorrow.")
