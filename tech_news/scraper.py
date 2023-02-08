import time
import requests
from requests.exceptions import ConnectTimeout, HTTPError, ReadTimeout


trybe_blog_url = "https://blog.betrybe.com/"

headers = {"user-agent": "Fake user-agent"}


def fetch(url: str):
    time.sleep(1)
    try:
        res = requests.get(url=trybe_blog_url, headers=headers, timeout=3)
        res.raise_for_status()
    except (ConnectTimeout, HTTPError, ReadTimeout):
        return None

    return res.text


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
