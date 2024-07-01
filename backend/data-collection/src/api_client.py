import requests

# Example API key and URL (Replace with actual ones)
API_KEY = 'YOUR_API_KEY'
API_URL = 'https://api.nativestats.com/matches/live'

def fetch_match_data():
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
