import requests
import time
import html

DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1098200267733880896/tQIEm4mHDZ6Q_hNnG7A-ujyRkzbzFq0UmUkqFwqvzMiaahHOierBjeaUJz2iPNS-kwCn'
DISCORD_WEBHOOK_URL_CS = 'https://discord.com/api/webhooks/1097698795883610225/NMYBWL8LHiuhhGdw9XRVKNBDj_F7uzSnwPRblIYjoqNDfWGSdQPrgooDKRrs6dwmQEPl'
TRIVIA_CATEGORY = 18

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
                'title': 'Isn\'t that cute?',
                'description': fact,
                'image': {'url': image_url},
                'color': 0x1da1f2
            }
        ]
    }
    response = requests.post(DISCORD_WEBHOOK_URL, json=data)
    if response.status_code != 204:
        print(f'Error sending Discord message: {response.text}')
'------------------------------------------------------------------'

def get_random_computer_science_trivia():
    url = f'https://opentdb.com/api.php?amount=1&category={TRIVIA_CATEGORY}&type=multiple'
    response = requests.get(url)
    data = response.json()
    question = html.unescape(data['results'][0]['question'])
    correct_answer = html.unescape(data['results'][0]['correct_answer'])
    return question, correct_answer

def send_discord_message_CS(question, answer):
    data = {
        'embeds': [
            {
                'title': 'Computer Science Trivia',
                'description': f'**Question:** {question}\n\n**Answer:** ||{answer}||',
                'color': 0x3498db
            }
        ]
    }
    response = requests.post(DISCORD_WEBHOOK_URL_CS, json=data)
    if response.status_code != 204:
        print(f'Error sending Discord message: {response.text}')
        
'------------------------------------------------------------------'
def main():
    while True:
        image_url = get_random_cat_image_url()
        question, answer = get_random_computer_science_trivia()
        fact = get_random_cat_fact()
        send_discord_message(image_url, fact)
        send_discord_message_CS(question, answer)
        time.sleep(300)  

if __name__ == '__main__':
    main()
