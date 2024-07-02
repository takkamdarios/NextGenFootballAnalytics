import requests
from utils.config import API_CONFIGS, COMMON_HEADERS

def fetch_data_from_source(source_name):
    """
    Fetches data from a given source by name using the configuration defined in API_CONFIGS.

    Parameters:
        source_name (str): The name of the source from which to fetch data.

    Returns:
        dict or None: The data fetched from the API, or None if an error occurs.
    """
    source_config = API_CONFIGS.get(source_name)
    if not source_config:
        print(f"No configuration found for source: {source_name}")
        return None

    headers = COMMON_HEADERS.copy()  # Start with common headers
    if 'api_key' in source_config:
        headers['Authorization'] = f"Bearer {source_config['api_key']}"  # Add authorization if needed

    try:
        response = requests.get(source_config['url'], headers=headers)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.json()  # Assuming the API returns JSON data
    except requests.RequestException as e:
        print(f"Failed to fetch data from {source_name}: {e}")
        return None

def fetch_all_data():
    """
    Fetches data from all configured sources.

    Returns:
        dict: A dictionary containing the data fetched from each source keyed by source name.
    """
    all_data = {}
    for source_name in API_CONFIGS.keys():
        print(f"Fetching data from {source_name}")
        data = fetch_data_from_source(source_name)
        if data:
            all_data[source_name] = data
        else:
            print(f"No data fetched from {source_name}")
    return all_data

# Example usage
if __name__ == "__main__":
    all_data = fetch_all_data()
    for source, data in all_data.items():
        print(f"Data from {source}: {data}")
