from urllib.parse import urljoin
import requests

def fetch_weather(city):
    payload = {
        'nTqM': '',
        "lang": "ru"
    }
    url = urljoin('https://wttr.in/', f'/{city}')
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.text


def main():
    cities = ["cherepovec", "london", "sheremetevo"]
    for city in cities:
        weather = fetch_weather(city)
        print(weather)


if __name__ == "__main__":
    main()
