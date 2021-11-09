from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

count = 0
def sensor():
    global count
    sched.print_jobs()
    print('Count: ' , count)
    count += 1

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'cron',minute='*')
sched.start()

app = Flask(__name__)

@app.route("/")
def hello():
    #sensor()
    return "Willem's scheduler is now running!"

if __name__ == "__main__":
    app.run('0.0.0.0',port=5000)