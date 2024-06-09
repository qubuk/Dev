import requests
import json

# Twoje dane dostępowe do TikTok API
ACCESS_TOKEN = 'your_access_token'
USER_ID = 'your_user_id'

# URL endpointów API
FOLLOWERS_COUNT_URL = f'https://api.tiktok.com/user/{USER_ID}/followers'
UPDATE_BIO_URL = f'https://api.tiktok.com/user/{USER_ID}/update'

def get_followers_count():
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}'
    }
    response = requests.get(FOLLOWERS_COUNT_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('followers_count')
    else:
        print(f'Błąd podczas pobierania liczby obserwujących: {response.status_code}')
        return None

def update_bio(followers_count):
    new_bio = f"Brawl Stars forever ✨🔥\n💚 BS Content Creator: 💚\n{followers_count}/1000"
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    payload = {
        'bio': new_bio
    }
    response = requests.post(UPDATE_BIO_URL, headers=headers, data=json.dumps(payload))
    if response.status_code == 200:
        print('BIO zostało zaktualizowane pomyślnie.')
    else:
        print(f'Błąd podczas aktualizacji BIO: {response.status_code}')

def main():
    followers_count = get_followers_count()
    if followers_count is not None:
        update_bio(followers_count)

if __name__ == "__main__":
    main()