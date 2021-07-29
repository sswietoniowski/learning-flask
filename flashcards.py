from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template(
        "welcome.html",
        page_name="Welcome Page",
        message="Here's a message from the view."
    )
