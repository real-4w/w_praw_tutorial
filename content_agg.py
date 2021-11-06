#https://codingkaiser.blog/2021/10/30/create-a-content-aggregator-with-python/
#https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps
#https://www.geeksforgeeks.org/inheritance-in-python/

from abc import ABC, abstractmethod
import praw
import w_yaml as w_y
#import os

class Source(ABC):
  
  @abstractmethod
  def connect(self):
    pass

  @abstractmethod
  def fetch(self):
    pass

class RedditSource(Source):

  def connect(self):
    self.reddit_con = praw.Reddit(client_id=yaml_data['client_id'], client_secret=yaml_data['client_secret'], grant_type_access='client_credentials', user_agent='script/1.0')
    return self.reddit_con

  def fetch(self):
    pass

#wip class
class RedditNew(RedditSource):
  """Create a class for a Reddit r/<name>

  Args:
      RedditSource (string): Should contain Reddit's r/<name>
  """
  def __init__(self, w_reddit: str) -> None:
    self.reddit_con = super().connect()
    self.new_submissions = []
    self.w_reddit = w_reddit
    
  def fetch(self, limit: int):
    self.new_submissions = self.reddit_con.subreddit(self.w_reddit).new(limit=limit)

  def __repr__(self):
    urls = []
    for submission in self.new_submissions:
      urls.append(vars(submission)['url'])
    return '\n'.join(urls)

class RedditHotProgramming(RedditSource):
#original class : can be deleted later.
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
  debug, yaml_data = w_y.ProcessYAML('reddit.yaml')  
   
  for reddit in yaml_data['reddits'] :
    reddit_new = RedditNew(reddit)
    reddit_new.fetch(5)
    print(reddit_new)
  
  #reddit_top_programming = RedditHotProgramming()
  #reddit_top_programming.fetch(limit=10)
  #print(reddit_top_programming)
  