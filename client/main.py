import sys
sys.path.insert(1, '/Users/anonymous/Desktop/tradingbotV2/src')
import getNews
#import NeuralNetwork
from multiprocessing import Process

print(getNews.News('https://en.wikipedia.org/wiki/Mathematics').get_sentiment())

#Process(target = getNews.News('https://en.wikipedia.org/wiki/Mathematics').get_sentiment()).start()
#Process(target = getNews.News('https://docs.python.org/3/library/multiprocessing.html').get_sentiment()).start()