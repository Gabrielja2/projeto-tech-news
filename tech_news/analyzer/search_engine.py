from tech_news.database import search_news


def search_by_title(title: str) -> list[tuple]:
    try:
        news_list = []
        find_news = search_news({'title': {'$regex': title, '$options': 'i'}})
        for news in find_news:
            news_list += ([(news['title'], news['url'])])

    except ValueError:
        return []

    return news_list


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
