import feedparser
from plyer import notification
import time

title = 'News Notification'


def parseFeed():

    f = feedparser.parse("https://feeds.bbci.co.uk/news/rss.xml")
    for newsitem in f["items"]:
        notification.notify (title = newsitem["title"], message = str(newsitem['summary']), app_icon = None, timeout = 100, toast = False)
        time.sleep(1080)

if __name__ == '__main__':
    parseFeed()
