
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect("medicine.db")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        medicine = request.form['medicine']
        quantity = request.form['quantity']

        conn = connect_db()
        conn.execute("INSERT INTO donors (name, phone, medicine, quantity) VALUES (?, ?, ?, ?)",
                     (name, phone, medicine, quantity))
        conn.commit()
        conn.close()

        return "Donation Submitted!"

    return render_template('donate.html')

@app.route('/request', methods=['GET', 'POST'])
def request_medicine():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        medicine = request.form['medicine']
        quantity = request.form['quantity']

        conn = connect_db()
        conn.execute("INSERT INTO requests (name, phone, medicine, quantity) VALUES (?, ?, ?, ?)",
                     (name, phone, medicine, quantity))
        conn.commit()
        conn.close()

        return "Request Submitted!"

    return render_template('request.html')

if __name__ == '__main__':
    app.run(debug=True)