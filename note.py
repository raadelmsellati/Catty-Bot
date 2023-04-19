import requests
import time

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1098200267733880896/tQIEm4mHDZ6Q_hNnG7A-ujyRkzbzFq0UmUkqFwqvzMiaahHOierBjeaUJz2iPNS-kwCn'

def get_random_cat_image_url():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    data = response.json()
    image_url = data[0]['url']
    return image_url

def send_discord_message(image_url):
    data = {
        'embeds': [
            {
                'title': 'Random Cat Picture',
                'image': {'url': image_url},
            }
        ]
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code != 204:
        print(f'Error sending Discord message: {response.text}')

def main():
    while True:
        image_url = get_random_cat_image_url()
        send_discord_message(image_url)
        time.sleep(3600)  # Wait for 3600 seconds (1 hour) before sending the next picture

if __name__ == '__main__':
    main()
