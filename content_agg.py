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
    self.w_reddit = w_reddit                                   # Willems additions
    self.w_len = 0  
    self.w_urls = []
    self.w_titles = []
    
    self.df_cols = ['Title', 'URL']
    self.w_reddit_df = pd.DataFrame(columns=self.df_cols)                             # pref way? WIP

  def fetch(self, limit: int):
    self.w_len = limit
    self.new_submissions = self.reddit_con.subreddit(self.w_reddit).new(limit=limit)
    
    titles = []
    urls = []                                                   # Was originally part of th __rep__(self) function
    for submission in self.new_submissions:                     #Moved forward to avoid errors 
      titles.append(vars(submission)['title'])
      urls.append(vars(submission)['url'])
      #print(vars(submission)['title'])
    self.w_urls = '\n'.join(urls)  
    self.w_titles = '\n'.join(titles)  

    #print(self.w_urls)

  def __repr__(self):
    return self.w_urls

  # my additions to the class are below:
  def len(self):
    return (self.w_len)

  def urls(self):
    return (self.w_urls)

  def print_info(self):
    print(f"R/{self.w_reddit}: {self.w_len}")
    #for (title, url) in zip(shlex.split(self.w_titles), shlex.split(self.w_urls)):
    #for (title, url) in zip(self.w_titles, self.w_urls):
    #  print (title, url)
    #zipped = (zip(self.w_titles, self.w_urls))
    
    print(self.w_urls)
    print(self.w_titles)
      
  def open_urls(self):
    for tab in shlex.split(self.w_urls) : 
      webbrowser.open_new(tab)

if __name__ == '__main__':
  debug, yaml_data = w_y.ProcessYAML('reddit.yaml')  
   
  for reddit in yaml_data['reddits'] :
    reddit_new = RedditNew(reddit)
    #reddit_new.print_info()
    reddit_new.fetch(2)
    #reddit_new.print_info()
    reddit_new.open_urls()

