import json
from datetime import datetime

def load_articles(file_path="articles.json"):
    try:
        with open(file_path, 'r') as f:
            articles = json.load(f)
            return [(datetime.fromisoformat(article['date']), article['title'], article['link']) for article in articles]
    except FileNotFoundError:
        return []

def save_articles(articles, file_path="articles.json"):
    data = [{"date": article[0].isoformat(), "title": article[1], "link": article[2]} for article in articles]
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
