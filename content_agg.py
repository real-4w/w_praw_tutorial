#https://codingkaiser.blog/2021/10/30/create-a-content-aggregator-with-python/
#https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps
#https://www.geeksforgeeks.org/inheritance-in-python/
from abc import ABC, abstractmethod
import webbrowser, shlex, praw
import pandas as pd
import w_yaml as w_y

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
    self.w_reddit = w_reddit                                                              # Willems additions
    self.w_len = 0  
    self.w_reddit_df = pd.DataFrame(columns=['title', 'url'])                             # pref way? WIP

  def fetch(self, limit: int):
    self.w_len = limit
    self.new_submissions = self.reddit_con.subreddit(self.w_reddit).new(limit=limit)
    for submission in self.new_submissions:                                               # Moved forward from __repr__ to avoid errors 
      self.w_reddit_df.loc[len(self.w_reddit_df.index)] = [vars(submission)['title'], vars(submission)['url']]
        
  def __repr__(self):
    return self.w_urls

  # my additions to the class are below:
  def len(self):
    return (self.w_len)

  def urls(self):
    return (self.w_reddit_df['url'])

  def print_info(self):
    print(f"\nR/{self.w_reddit}: {self.w_len}")
    print(self.w_reddit_df)
      
  def open_urls(self):
    for tab in self.w_reddit_df['url'] : 
      webbrowser.open_new(tab)

if __name__ == '__main__':
  debug, yaml_data = w_y.ProcessYAML('reddit.yaml')  
   
  for reddit in yaml_data['reddits'] :
    reddit_new = RedditNew(reddit)
    reddit_new.fetch(2)
    reddit_new.print_info()
    reddit_new.open_urls()