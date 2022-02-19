import argparse
import os
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


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
    bit_link = response.json()
    return bit_link['link']


def count_clicks(token, link):
    url_result_parser = urlparse(link)
    parsed_link = '{}{}'.format(url_result_parser.hostname, url_result_parser.path)
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'.format(
        bitlink=parsed_link)
    headers = {
        'Authorization': 'Bearer {}'.format(token),
    }
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    clicks = response.json()
    return clicks['total_clicks']


def is_bitlink(link, token):
    url_result_parser = urlparse(link)
    parsed_link = '{}{}'.format(url_result_parser.hostname, url_result_parser.path)
    api_url = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'.format(
        bitlink=parsed_link)
    headers = {
        'Authorization': 'Bearer {}'.format(token),
    }
    response = requests.get(api_url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    token = os.getenv('BITLY_TOKEN')
    parser = argparse.ArgumentParser()
    parser.add_argument('link')
    args = parser.parse_args()
    user_input = args.link

    if is_bitlink(user_input, token):
        try:
            print('Количество кликов:', count_clicks(token, user_input))
        except requests.exceptions.HTTPError:
            print('Некорректная ссылка')
    else:
        try:
            print('Битлинк', shorten_link(token, user_input))
        except requests.exceptions.HTTPError:
            print('Некорректная ссылка')


if __name__ == "__main__":
    main()
