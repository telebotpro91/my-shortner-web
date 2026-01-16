import os
from flask import Flask, render_template, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Setup (Same as Bot)
MONGO_URI = "mongodb+srv://mybotuser:OUyx645TaQVQlQiM@trunj.cy6jth5.mongodb.net/?appName=trunj"
client = MongoClient(MONGO_URI)
db = client['telegram_bot_db'] # Bot bhi isi DB mein save kar raha hai
files_col = db['stored_files'] # Bot isi collection mein daal raha hai

@app.route('/')
def home():
    return "<h1>Website is Online</h1><p>Send a file to the bot to get a link.</p>"

@app.route('/file/<file_id>')
def get_file(file_id):
    try:
        # Database se file dhundna ID ke zariye
        file_data = files_col.find_one({"_id": ObjectId(file_id)})
        
        if file_data:
            # Agar file mil gayi toh download page dikhao
            return f"<h1>File Found: {file_data['file_name']}</h1><p>Ads will appear here.</p><button>Download Now</button>"
        
        return "<h1>404: File Not Found in Database</h1>", 404
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>", 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
