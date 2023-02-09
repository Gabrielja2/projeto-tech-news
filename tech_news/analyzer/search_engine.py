from tech_news.database import search_news
from datetime import datetime


def search_by_title(title: str) -> list[tuple]:
    try:
        list_by_title = []
        query = {'title': {'$regex': title, '$options': 'i'}}
        news_by_title = search_news(query)
        for news in news_by_title:
            list_by_title += ([(news['title'], news['url'])])

    except ValueError:
        return []

    return list_by_title


def search_by_date(date) -> list[tuple]:
    try:
        list_by_date = []
        new_format_date = datetime.fromisoformat(date).strftime('%d/%m/%Y')
        query = {"timestamp": {"$eq": new_format_date}}
        news_by_date = search_news(query)

        for news in news_by_date:
            list_by_date += ([(news['title'], news['url'])])

        return list_by_date

    except ValueError:
        raise ValueError('Data inválida')


def search_by_category(category):
    try:
        list_by_category = []
        query = {'category': {'$regex': category, '$options': 'i'}}
        news_by_category = search_news(query)

        for news in news_by_category:
            list_by_category += ([(news['title'], news['url'])])

        return list_by_category

    except ValueError:
        return []
