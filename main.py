import requests
import argparse
from urllib.parse import urlparse
import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['TOKEN']


def shorten_link(token, url):
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    payload = {
        "long_url": url
    }
    headers = {
        'Authorization': 'Bearer {}'.format(token),
    }
    response = requests.post(api_url, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data['link']


def count_clicks(token, link):
    parser = urlparse(link)
    parsed_link = '{}{}'.format(parser.hostname, parser.path)
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'.format(
        bitlink=parsed_link)
    headers = {
        'Authorization': 'Bearer {}'.format(token),
    }
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data['total_clicks']


def is_bitlink(link, token):
    parser = urlparse(link)
    parsed_link = '{}{}'.format(parser.hostname, parser.path)
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'.format(
        bitlink=parsed_link)
    headers = {
        'Authorization': 'Bearer {}'.format(token),
    }
    response = requests.get(api_url, headers=headers)
    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('link')
    args = parser.parse_args()
    user_input = args.link

    if is_bitlink(user_input, TOKEN):
        print('Количество кликов:', count_clicks(TOKEN, user_input))
    else:
        try:
            print('Битлинк', shorten_link(TOKEN, user_input))
        except requests.exceptions.HTTPError:
            print('Некорректная ссылка')


if __name__ == "__main__":
    main()
