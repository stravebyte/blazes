from flask import Flask, render_template, request, redirect, url_for, session
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "qun3i648"
# MongoDB connection
connection_string = "mongodb+srv://Stravecodes:ASh2LeaVounah7pu@strave.3nqbbea.mongodb.net/FF?retryWrites=true&w=majority&appName=Strave"
client = pymongo.MongoClient(connection_string)

db = client.FF
usr_col = db["users"]
msg_col = db["messages"]

def find_registration_id_by_payment_id(payment_id):
    # Query MongoDB to find registration_id based on payment_id
    registration = usr_col.find_one({'payment_id': payment_id})

    if registration:
        return registration['_id']
    else:
        return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/email_submit", methods=["POST"])
def email_submit():
    if request.method == "POST":
        name = request.form.get("name")
        msg = request.form.get("message")

        msg_col.insert_one({"name":name, "msg":msg})
        return redirect("/")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route('/submit', methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        whatsapp = request.form.get("whatsapp")
        uid = request.form.get("uid")
        upi_id = request.form.get("upi")
        data = {
            "name": name,
            "uid": uid,
            "upi_id": upi_id,
            "whatsapp":whatsapp
        }
        session['user_data'] = data
        return render_template("pay.html")
    return render_template("register.html")

@app.route("/payment")
def payment_page():
    return render_template("pay.html")

@app.route("/success")
def handle_payment_success():
    data = session.get('user_data')
    if data:
        usr_col.insert_one(data)
        session.pop("user_data")
        return render_template("successful.html")
    else:
        return redirect(url_for("register"))

if __name__ == "__main__":
    app.run(debug=True)
