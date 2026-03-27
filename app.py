from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)


def get_db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "database.db")

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    db = get_db()

    trending = db.execute("SELECT * FROM designs").fetchall()
    artists = db.execute("SELECT * FROM artists").fetchall()
    reviews = db.execute("SELECT * FROM reviews").fetchall()

    return render_template(
        "index.html",
        trending=trending,
        artists=artists,
        reviews=reviews
    )

@app.route("/book", methods=["POST"])
def book():
    name = request.form["name"]
    service = request.form["service"]

    db = get_db()
    db.execute("INSERT INTO bookings (name, service) VALUES (?,?)", (name, service))
    db.commit()

    return redirect("/")

app.run(debug=True)
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        service = request.form["service"]
        message = request.form["message"]

        db = get_db()
        db.execute(
            "INSERT INTO contacts (name,email,phone,service,message) VALUES (?,?,?,?,?)",
            (name,email,phone,service,message)
        )
        db.commit()

        return redirect("/")

    return render_template("contact.html")
# view details page open
@app.route("/bridal-full-hand")
def bridal_full_hand():
    return render_template("bridal_mehendi.html")


# services section

@app.route('/bridal_mehendi')
def bridal():
    return render_template('bridal_mehendi.html')

@app.route('/party_mehendi')
def party():
    return render_template('party_mehendi.html')

@app.route('/engagement_mehendi')
def engagement():
    return render_template('engagement_mehendi.html')

@app.route('/festival_mehendi')
def festival():
    return render_template('festival_mehendi.html')