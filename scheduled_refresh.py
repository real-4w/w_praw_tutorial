from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
#from content_agg import RedditNew, RedditSource, Source
import content_agg as c_a
import w_yaml as w_y
from tzlocal import get_localzone

count = 0

def trigger():
    global count
    debug, yaml_data = w_y.ProcessYAML('reddit.yaml')  
    count += 1
    sched.print_jobs()
    print(f"Refreshed: {count}")
    for reddit in yaml_data['reddits'] :
        reddit_new = c_a.RedditNew(reddit)
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
    app.run('0.0.0.0',port=5000)