# w_praw_tutorial
Willem's tutorial using praw.

Requirements:

1) Have a Reddit Client ID & Secret: #https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps

2) Install pandas, yaml, flask, praw, feedparser

3) Make sure you have a reddit.yaml file like this
    ---
    debug : True | False                                                     
    client_id : "<your Reddit client_id>"
    client_secret :  "<your Reddit client_secret>"
    number : <number of reddit threads to fetch>
    reddits:
    - alexa 
    - gadgets

Contents:
    1) content_ag.py: Contains Reddit & RSS classes & meta class (using dataframes) for Content Aggregation. Functions to display links and store content in pickle.
    2) scheduled_refresh.pu: Opens us content links at scheduled time. Requires flask.
    3) display_df_via_pickel_html.py: Module to show saved pickle as html table.
    4) w_yaml.py: Functional module to load yaml values.



https://praw.readthedocs.io/en/stable/tutorials/comments.html
https://pypi.org/project/praw/

