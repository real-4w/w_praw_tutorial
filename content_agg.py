#https://codingkaiser.blog/2021/10/30/create-a-content-aggregator-with-python/
#https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

from abc import ABC, abstractmethod
import praw
import os

class Source(ABC):

  @abstractmethod
  def connect(self):
    pass

  @abstractmethod
  def fetch(self):
    pass

CLIENT_ID = 'l3ZMi0eMfq8gb2wtbZlTAQ'                                        #needs a better solution    https://pypi.org/project/azure-keyvault-secrets/
CLIENT_SECRET = 'nJdK4zHFNFA0yDR2Y6U8palQG_O_wA'

class RedditSource(Source):

  def connect(self):
    self.reddit_con = praw.Reddit(client_id=CLIENT_ID,
                      client_secret=CLIENT_SECRET,
                      grant_type_access='client_credentials',
                      user_agent='script/1.0')
    return self.reddit_con

  def fetch(self):
    pass

class RedditHotProgramming(RedditSource):

  def __init__(self) -> None:
    self.reddit_con = super().connect()
    self.hot_submissions = []

  def fetch(self, limit: int):
    self.hot_submissions = self.reddit_con.subreddit('programming').hot(limit=limit)

  def __repr__(self):
    urls = []
    for submission in self.hot_submissions:
      urls.append(vars(submission)['url'])
    return '\n'.join(urls)

if __name__ == '__main__':
  reddit_top_programming = RedditHotProgramming()
  reddit_top_programming.fetch(limit=10)
  print(reddit_top_programming)