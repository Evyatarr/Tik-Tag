import urllib.parse

from flask import Flask, render_template, request
from flask_qrcode import QRcode

app = Flask(__name__)
QRcode(app)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        html_name = request.form.get("field1_name")
        html_number = request.form.get("field2_phone")
        return render_template("index.html", link=(link_generator(html_name, html_number)))
    return render_template("index.html")


def link_generator(name, phone):
    phone = phone.replace("-", "")
    phone = phone.replace("0", "972", 1)
    message = (f"Hello {name}!, I've found your luggage! Please contact me so you can take It back! ")
    encoded_message = urllib.parse.quote(message)
    wa_link = (f"https://wa.me/{phone}?text={encoded_message}")
    return wa_link

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/usa", methods=["POST", "GET"])
def usa():
    if request.method == "POST":
        html_name = request.form.get("field1_name")
        html_number = request.form.get("field2_phone")
        return render_template("index.html", link=(link_generator_usa(html_name, html_number)))
    return render_template("index.html")


def link_generator_usa(name, phone):
    phone = phone.replace("-", "")
    message = (f"Hello {name}!, I've found your luggage! Please contact me so you can take It back! ")
    encoded_message = urllib.parse.quote(message)
    wa_link = (f"https://wa.me/1{phone}?text={encoded_message}")
    return wa_link

if __name__ == "__main__":
    app.run()
