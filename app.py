import os, sys
from flask import Flask, jsonify, render_template
import sqlite3
import json

app = Flask(__name__, static_url_path='')

class Collectable:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.display_name = ""
        self.price = 0
        self.type = ""
        self.location = ""
        self.start_month = ""
        self.end_month = ""
        self.start_hour = ""
        self.end_hour = ""

@app.route('/')
def home():
    return render_template(
        "home.html",
        data=get_data().get_json()["data"],
        month=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    )

def get_data():
    conn = sqlite3.connect('db.sqlite')
    cur = conn.cursor()
    cur.execute("""SELECT * FROM collections""")
    data = {}
    d = []
    for c in cur.fetchall():
        t = {}
        t["id"] = c[0]
        t["name"] = c[1].replace(" ", "_")
        t["display_name"] = c[1].title()
        t["price"] = c[2]
        t["type"] = c[3]
        t["location"] = c[4]
        t["start_month"] = c[7]
        t["end_month"] = c[8]
        t["start_hour"] = c[5]
        t["end_hour"] = c[6]
        print(t)
        d.append(t)

    data = {
        "data": d
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run()