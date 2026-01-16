import os
from flask import Flask, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)

# --- CONFIGURATION ---
MONGO_URI = "mongodb+srv://mybotuser:OUyx645TaQVQlQiM@trunj.cy6jth5.mongodb.net/?appName=trunj"
client = MongoClient(MONGO_URI)
db = client['telegram_bot']
collection = db['files']

# Aapka Bot Username (Bina @ ke)
BOT_USERNAME = "Filesaver777_bot"

@app.route('/')
def home():
    return "Website is Live and Running!"

@app.route('/file/<file_id>')
def index(file_id):
    file_data = collection.find_one({"file_id": file_id})
    if file_data:
        return render_template('index.html', file_id=file_id)
    return "File Not Found (404 Error)", 404

@app.route('/get-link/<file_id>')
def get_link(file_id):
    # User ko wapas aapke bot par redirect karega
    return redirect(f"https://t.me/{BOT_USERNAME}?start={file_id}")

if __name__ == '__main__':
    app.run()
