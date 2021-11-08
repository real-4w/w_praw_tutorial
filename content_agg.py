from abc import ABC, abstractmethod
import webbrowser, praw, feedparser
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

class RSSSource(Source):
  def connect(self):
      pass
  def fetch(self):
      pass

class RSSNew(RSSSource):

  def __init__(self, w_rss: str) -> None:
    self.w_rss = w_rss
    self.w_len = 0
    self.w_rss_df = pd.DataFrame(columns=['date', 'title', 'url'])                      # Use dataframe for simplicity/

  def fetch(self, limit: int):
    self.w_len = limit
    i = 0
    NewsFeed = feedparser.parse(self.w_rss)
    for entry in NewsFeed['entries']:                                                   # gives xx rss entries as are on the page
      if i < self.w_len :
        self.w_rss_df.loc[len(self.w_rss_df.index)] = [entry.published, entry.title, entry.link]
        i += 1
 
  def __repr__(self):
    """Returns a string summary self.print() is called.
    """
    return(f"\nRSS: {self.w_rss}: {self.w_len}")

  def len(self):
    return (self.w_len)

  def urls(self):
    return (self.w_rss_df['url'])

  def print_info(self):
    print(f"\nR/{self.w_rss}: {self.w_len}")
    print(self.w_rss_df)

  def open_urls(self):
    for tab in self.w_rss_df['url'] : 
      webbrowser.open_new(tab)

class RedditNew(RedditSource):
  """Create a class for getting a Reddit r/<name>.

  Args:
      RedditSource (string): Should contain Reddit's r/<name>
  """
  def __init__(self, w_reddit: str) -> None:
    self.reddit_con = super().connect()
    self.new_submissions = []
    self.w_reddit = w_reddit                                                              
    self.w_len = 0  
    self.w_reddit_df = pd.DataFrame(columns=['title', 'url'])                             # Use dataframe for simplicity/

  def fetch(self, limit: int):
    """Function to get <limit> reddit articles from the Reddit r/<w_reddit> as per class. Function will update values in the instance of the RedditNew Class.

    Args:
        limit (int): number of articles
    """
    self.w_len = limit
    self.new_submissions = self.reddit_con.subreddit(self.w_reddit).new(limit=limit)
    for submission in self.new_submissions:                                               # Moved forward from __repr__ to avoid errors 
      self.w_reddit_df.loc[len(self.w_reddit_df.index)] = [vars(submission)['title'], vars(submission)['url']]
        
  def __repr__(self):
    """Returns a string summary print(RedditNew) is called.
    """
    return(f"\nR/{self.w_reddit}: {self.w_len}")

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
    reddit_new.fetch(int(yaml_data['number']))
    reddit_new.print_info()
    reddit_new.open_urls()
  
  for rss in yaml_data['rss'] :
    rss_new = RSSNew(rss)
    rss_new.fetch(int(yaml_data['number']))
    rss_new.print_info()
    rss_new.open_urls()
  