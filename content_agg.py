from abc import ABC, abstractmethod
import webbrowser, praw, feedparser, datetime
import pandas as pd
import w_yaml as w_y

debug, yaml_data = w_y.ProcessYAML('reddit.yaml')  

class Source(ABC):
  
  @abstractmethod
  def connect(self):
    pass

  @abstractmethod
  def fetch(self):
    pass

class RedditSource(Source):
  # this function is fixed: dirty access to yaml_data for 'client_id' and 'client_secret'
  def connect(self, client_id: str, client_secret: str):
  #def connect(self):
    #self.reddit_con = praw.Reddit(client_id=yaml_data['client_id'], client_secret=yaml_data['client_secret'], grant_type_access='client_credentials', user_agent='script/1.0')
    self.reddit_con = praw.Reddit(client_id=client_id, client_secret=client_secret, grant_type_access='client_credentials', user_agent='script/1.0')
    return self.reddit_con

  def fetch(self):
    pass

class RedditNew(RedditSource):
  """Create a class for getting a Reddit r/<name>.

  Args:
      RedditSource (string): Should contain Reddit's r/<name>
  """
  def __init__(self, w_reddit: str) -> None:
    self.reddit_con = super().connect(yaml_data['client_id'], yaml_data['client_secret'])
    self.new_submissions = []
    self.w_reddit = w_reddit                                                              
    self.w_len = 0  
    self.w_reddit_df = pd.DataFrame(columns=['date', 'title', 'url'])                          

  def fetch(self, limit: int):
    """Function to get <limit> reddit articles from the Reddit r/<w_reddit> as per class. Function will update values in the instance of the RedditNew Class.

    Args:
        limit (int): number of articles
    """
    self.w_len = limit
    self.new_submissions = self.reddit_con.subreddit(self.w_reddit).new(limit=limit)
    for submission in self.new_submissions:                                              
      self.w_reddit_df.loc[len(self.w_reddit_df.index)] = [datetime.datetime.fromtimestamp(vars(submission)['created']), vars(submission)['title'], vars(submission)['url']]
  
  def __repr__(self):
    """Returns a string summary print(RedditNew) is called.
    """
    return(f"{self.w_reddit}: {self.w_len}")

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

  def return_df(self):
    return (self.w_reddit_df)
 
  def read_pickle(self, pickle: str):
    self.w_reddit_df = pd.read_pickle(pickle)

  def write_pickle(self, pickle: str):
    self.w_reddit_df.to_pickle(pickle)

class RSSSource(Source):
  def connect(self):
      pass
  def fetch(self):
      pass

class RSSNew(RSSSource):

  def __init__(self, w_rss: str) -> None:
    self.w_rss = w_rss
    self.w_len = 0
    self.w_rss_df = pd.DataFrame(columns=['date', 'title', 'url'])                      

  def fetch(self, limit: int):
    self.w_len = limit
    i = 0
    NewsFeed = feedparser.parse(self.w_rss)
    for entry in NewsFeed['entries']:                                                   # gives xx rss entries as are on the page
      if i < self.w_len :
        self.w_rss_df.loc[len(self.w_rss_df.index)] = [entry.published, entry.title, entry.link]
        i += 1
 
  def __repr__(self):
    """Returns a string summary print(RSSNew) is called.
    """
    return(f"RSS: {self.w_rss}: {self.w_len}")

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

  def return_df(self):
    return (self.w_rss_df)
  
  def read_pickle(self, pickle: str):
    self.w_content_df = pd.read_pickle(pickle)

  def write_pickle(self, pickle: str):
    self.w_content_df.to_pickle(pickle)

class w_ContentAggregator(ABC):
  def __init__(self) -> None:
    super().__init__()
    self.w_content_df = pd.DataFrame(columns=['date', 'title', 'url'])   

  def __repr__(self):
    """Returns a string summary print(RedditNew) is called.
    """
    return(f"w_ContentAggregator:\n {self.w_content_df}")

  def read_pickle(self, pickle: str):
    self.w_content_df = pd.read_pickle(pickle)
  
  def add_content_df(self, w_df_add: pd.DataFrame):
    self.w_content_df = self.w_content_df.append(w_df_add, ignore_index = True)
  
  def write_pickle(self, pickle: str):
    self.w_content_df.to_pickle(pickle)

if __name__ == '__main__':
  w_all_content = w_ContentAggregator() 
  #w_all_content.read_pickle("content.pkl")
  for reddit in yaml_data['reddits'] :
    reddit_new = RedditNew(reddit)
    reddit_new.fetch(int(yaml_data['number']))
    reddit_new.print_info()
    reddit_new.open_urls()
    #reddit_new.write_pickle(f"{reddit}.pkl")
    #w_all_content.add_content_df(reddit_new.return_df())
  #print(w_all_content)
  #w_all_content.write_pickle("content.pkl")
  #for rss in yaml_data['rss'] :
    #rss_new = RSSNew(rss)
    #rss_new.fetch(int(yaml_data['number']))
    #rss_new.print_info()
    #rss_new.open_urls()
    #rss_new.write_pickle()

