from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import w_content_agg as c_a
import w_yaml as w_y

count = 0

def trigger():
    global count
    debug, yaml_data = w_y.ProcessYAML('reddit.yaml')  
    count += 1
    sched.print_jobs()
    if debug == True : print(f"Refreshed: {count}")
    for reddit in yaml_data['reddits'] :
        reddit_new = c_a.RedditNew(reddit, yaml_data['client_id'], yaml_data['client_secret'])
        reddit_new.fetch(int(yaml_data['number']))
        reddit_new.print_info()
        reddit_new.open_urls()

sched = BackgroundScheduler(daemon=True, timezone= 'Pacific/Auckland')
sched.add_job(trigger,'cron',minute='*/15')
sched.start()

app = Flask(__name__)

@app.route("/")
def hello():
    trigger()
    return "Content refresh scheduler is now running!" 

if __name__ == "__main__":
    app.run()