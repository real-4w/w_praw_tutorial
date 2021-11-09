from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from content_agg import RedditNew, RedditSource, Source
import content_agg as c_a
import w_yaml as w_y

count = 0

def sensor():
    global count
    debug, yaml_data = w_y.ProcessYAML('reddit.yaml')  
    print(debug)
    count += 1
    sched.print_jobs()
    print('Refreshed: ' , count)
    for reddit in yaml_data['reddits'] :
        reddit_new = RedditNew(reddit)
        reddit_new.fetch(int(yaml_data['number']))
        reddit_new.print_info()
        reddit_new.open_urls()

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'cron',minute='*')
sched.start()

app = Flask(__name__)

@app.route("/")
def hello():
    sensor()
    return "Content refresh scheduler is now running!"

if __name__ == "__main__":
    app.run('0.0.0.0',port=5000)