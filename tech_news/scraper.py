import time
import requests
from parsel import Selector
from requests.exceptions import ConnectTimeout, HTTPError, ReadTimeout
from tech_news.database import create_news


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


def scrape_updates(html_content: str) -> list:
    selec = Selector(html_content)
    result = []
    for post in selec.css("div.archive-main"):
        href = post.css("h2 > a ::attr(href)").getall()
        result += href

    return result


def scrape_next_page_link(html_content):
    selec = Selector(html_content)
    return selec.css("a.next ::attr(href)").get()


def scrape_news(html_content):
    try:
        selec = Selector(html_content)
        category = selec.css("span.label ::text").get()
        reading_time = int(
            selec.css("li.meta-reading-time ::text").re_first(r"\d+")
        )
        timestamp = selec.css("li.meta-date ::text").get()
        title = selec.css("h1.entry-title ::text").get().strip()
        url = selec.css("link[rel=canonical] ::attr(href)").get()
        writer = selec.css("span.author ::text").get()
        summary = "".join(
            selec.css("div.entry-content > p:first-of-type ::text").getall()
            ).strip()

        news = {
            "category": category,
            "reading_time": reading_time,
            "timestamp": timestamp,
            "title": title,
            "url": url,
            "writer": writer,
            "summary": summary
        }

    except ValueError:
        raise ValueError
    return news


def get_tech_news(amount: int):
    result_html = fetch(trybe_blog_url)
    list_href = scrape_updates(result_html)
    list = []

    while len(list_href) < amount:
        next_page_href = scrape_next_page_link(result_html)
        result_html = fetch(next_page_href)
        list_href += scrape_updates(result_html)

    for href in list_href[:amount]:
        result = fetch(href)
        news = scrape_news(result)
        list += [news]

    create_news(list)

    return list
# list = [scrape_news(fetch(href)) for href in list_href[:amount]]
# create_news(list)
# return list
