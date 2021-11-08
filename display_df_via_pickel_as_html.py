from flask import *
import pandas as pd
app = Flask(__name__)

@app.route("/")
def hello():
    return "My links can be found at /links."

@app.route("/links")
def show_tables():
    data = pd.read_pickle('reddit.pkl')
    return render_template('view.html',tables=[data.to_html(classes='Links')], titles = ['na', 'Links'])
    
if __name__ == "__main__":
    app.run(debug=True)