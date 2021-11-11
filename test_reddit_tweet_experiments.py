import w_yaml as w_y
import w_content_agg as w_c_a
import twitter, sys
if __name__ == '__main__':
    #this realy should go into a seperatefile to keep things tidy.
    debug, yaml_data = w_y.ProcessYAML('reddit.yaml')  
    w_all_content = w_c_a.w_ContentAggregator() 
    #w_all_content.read_pickle("content.pkl")
    for reddit in yaml_data['reddits'] :
        reddit_new = w_c_a.RedditNew(reddit, yaml_data['client_id'], yaml_data['client_secret'])
        reddit_new.fetch(int(yaml_data['number']))
        #reddit_new.print_info()
        reddit_new.open_urls()
        #reddit_new.write_pickle(f"{reddit}.pkl")
        print(reddit_new.urls())
        #w_all_content.add_content_df(reddit_new.return_df())
        #print(w_all_content)
    #w_all_content.write_pickle("content.pkl")
  
    for rss in yaml_data['rss'] :
        rss_new = w_c_a.RSSNew(rss)
        rss_new.fetch(int(yaml_data['number']))
        #rss_new.print_info()
        rss_new.open_urls()
        #rss_new.write_pickle(f"{rss}.pkl")

    debug, yaml_data = w_y.ProcessYAML('twitter.yaml')  
    w_api_key = yaml_data['API_Key']
    w_api_key_secret = yaml_data['API_Key_Secret']
    w_access_token = yaml_data['Access_Token']
    w_access_token_secret = yaml_data['Access_Token_Secret']
    api = twitter.Api(consumer_key=w_api_key, consumer_secret=w_api_key_secret,
                        access_token_key=w_access_token, access_token_secret=w_access_token_secret)
    try:
        status = api.PostUpdate(f"Wow: {reddit_new.urls()}")
    except UnicodeDecodeError:
        print("Your message could not be encoded.  Perhaps it contains non-ASCII characters? ")
        print("Try explicitly specifying the encoding with the --encoding flag")
        sys.exit(2)

    print("{0} just posted: {1}".format(status.user.name, status.text))  

