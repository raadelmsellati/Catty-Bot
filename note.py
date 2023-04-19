import time
from instaloader import Instaloader, Profile
from discord_webhook import DiscordWebhook

GIN = '365Journey'
I = '!Journey2023'

INSTAGRAM_USERNAME = 'r3diant'  # Replace with the desired Instagram username (e.g., 'bbc')
WEBHOOK_URL = 'https://discord.com/api/webhooks/1098200267733880896/tQIEm4mHDZ6Q_hNnG7A-ujyRkzbzFq0UmUkqFwqvzMiaahHOierBjeaUJz2iPNS-kwCn'  # Replace with your Discord webhook URL

def get_recent_posts(username):
    loader = Instaloader()
    loader.login(GIN, I)
    profile = Profile.from_username(loader.context, username)
    posts = list(profile.get_posts())[:5]  # Get the 5 most recent posts
    return posts

def send_to_discord(post):
    webhook = DiscordWebhook(url=WEBHOOK_URL)
    embed = {
        'title': f'New post from {INSTAGRAM_USERNAME}',
        'description': f'[View post on Instagram]({post.url})',
        'color': 0x1da1f2,  # Instagram's color in hex
        'image': {'url': post.url},
    }
    webhook.add_embed(embed)
    webhook.execute()

def main():
    recent_posts = get_recent_posts(INSTAGRAM_USERNAME)
    last_post_time = max(post.date_utc for post in recent_posts)

    while True:
        time.sleep(60)  # Check for new posts every minute
        current_recent_posts = get_recent_posts(INSTAGRAM_USERNAME)
        current_last_post_time = max(post.date_utc for post in current_recent_posts)

        if current_last_post_time > last_post_time:
            for post in current_recent_posts:
                if post.date_utc > last_post_time:
                    send_to_discord(post)

            last_post_time = current_last_post_time

if __name__ == '__main__':
    main()
