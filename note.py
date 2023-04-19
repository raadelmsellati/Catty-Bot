import requests
import time

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1098200267733880896/tQIEm4mHDZ6Q_hNnG7A-ujyRkzbzFq0UmUkqFwqvzMiaahHOierBjeaUJz2iPNS-kwCn'

def get_random_cat_image_url():
    url = 'https://api.thecatapi.com/v1/images/search'
    response = requests.get(url)
    data = response.json()
    image_url = data[0]['url']
    return image_url

def get_random_cat_fact():
    url = 'https://catfact.ninja/fact'
    response = requests.get(url)
    data = response.json()
    fact = data['fact']
    return fact

def send_discord_message(image_url, fact):
    data = {
        'embeds': [
            {
                'title': 'Random Cat Picture and Fact',
                'description': fact,
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
        fact = get_random_cat_fact()
        send_discord_message(image_url, fact)
        time.sleep(300)  

if __name__ == '__main__':
    main()
