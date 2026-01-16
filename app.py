import os
from flask import Flask, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)

# --- MONGO DB SETUP ---
# Aapki di hui MongoDB URL
MONGO_URI = "mongodb+srv://mybotuser:OUyx645TaQVQlQiM@trunj.cy6jth5.mongodb.net/?appName=trunj"
client = MongoClient(MONGO_URI)
db = client['telegram_bot']  # Aapka DB Name
collection = db['files']    # Aapka Collection Name

@app.route('/')
def home():
    return "Website is Live and Running!"

@app.route('/file/<file_id>')
def index(file_id):
    # Database se check karega ki file exist karti hai ya nahi
    file_data = collection.find_one({"file_id": file_id})
    if file_data:
        # Agar file milti hai toh ads wala page dikhayega
        return render_template('index.html', file_id=file_id)
    return "File Not Found (404 Error) - Please check your link.", 404

@app.route('/get-link/<file_id>')
def get_link(file_id):
    # YAHAN APNA BOT USERNAME DALEIN (Bina @ ke)
    # Maan lijiye aapka bot username 'TRUNJ_Bot' hai
    bot_username = "AAPKA_BOT_USERNAME_YAHAN" 
    return redirect(f"https://t.me/{bot_username}?start={file_id}")

if __name__ == '__main__':
    app.run()
