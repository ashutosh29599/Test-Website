from flask import Flask, render_template
# render_template accesses the html file, and display on the url
# layout.html is the parent html and home is the child, so home doesn't require html tags

app = Flask(__name__)

@app.route('/') # / refers to the homepage, and the whole parameter is the url
def home(): # this fn defines what your webpage will do
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__": # this script's name is __main__, if we were to import this script, name would be "script1"
    app.run(debug=True)