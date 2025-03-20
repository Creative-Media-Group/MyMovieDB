from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def mainpage():
    return render_template("index.html", title="MyMovieDB")


if __name__ == "__main__":
    app.run(debug=False)
