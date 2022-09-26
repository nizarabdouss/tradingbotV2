import torch
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import requests
from bs4 import BeautifulSoup
import re
from newspaper import Article
from time import sleep
from tqdm import tqdm
from requests_html import HTMLSession

def collect_coins() -> list[str]:
    """Get User input for coin list"""
    coins = input("Enter coin to search for (enter coins seperated by a comma):\n")
    coins = coins.split(",")
    return coins


class News:
    def __init__(self, url, coins) -> None:
        self.url = url
        self.coins = coins

    def load_article(self):
        article = Article(self.url)
        article.download()
        article.parse()
        article.nlp()
        print(self.coins)
        self.is_in(article)
        return None

    def get_sentiment(self) -> int:

        article = self.load_article()
        if article is not None:
            tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

            model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

            tokens = tokenizer.encode(article, return_tensors = 'pt')

            result = model(tokens)
            return int(torch.argmax(result.logits)) + 1
        return None

    def progress_bar(self):

        for i in tqdm(range(30)):
            sleep(1)

    def is_in(self, article):
        print(article.text)
        for i in self.coins:
            print(i in article.text)

class Scraper:
    def __init__(self, url):
        self.url = url
        self.session = HTMLSession()
        self.urls = self.collect_urls()

    def collect_urls(self):
        urls = []
        r = self.session.get(self.url)
        r.html.render(sleep = 1, scrolldown = 5)
        articles = r.html.find('article')
        for article in articles:
            newsItem = article.find('a', first = True)
            link = newsItem.absolute_links
            urls.append(link.pop())
        return urls
    
    def get_urls(self):
        return self.urls
coins = collect_coins()
for i in Scraper('https://cointelegraph.com/tags/altcoin').get_urls():
    print(i)
    print(News(i, coins).get_sentiment())