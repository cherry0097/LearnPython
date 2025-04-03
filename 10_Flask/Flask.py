'''Install PyMongo 1st: pip install pymongo'''

from flask import Flask, jsonify, request
import pymongo
import urllib.parse

# Encode username and password
username = urllib.parse.quote_plus("ratulpal0097")
password = urllib.parse.quote_plus("PikaChu@1997")

# MongoDB Connection URL
mongourl = f"mongodb+srv://{username}:{password}@cluster0.m00nmhh.mongodb.net/"

# Initialize Flask App
app = Flask(__name__)

# Connect to MongoDB
client = pymongo.MongoClient(mongourl)

db = client['UserDatabase'] # Create/Connect to a Database
collection = db['Listofusers'] # Create/Connect to a Collection

@app.route("/")
def home():
    return jsonify({"message": "Welcome to Flask with MongoDB!"})

# Create (Insert Data)
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json  # Get JSON data from request
    if not data:
        return jsonify({"error": "No data provided"}), 400
    result = collection.insert_one(data)  # Insert into MongoDB
    return jsonify({"message": "User added", "id": str(result.inserted_id)})

# Read (Fetch Data)
@app.route("/users", methods=["GET"])
def get_users():
    users = list(collection.find({}, {"_id": 0}))  # Get all users, exclude _id
    return jsonify(users)

if __name__ == "__main__":
    # print(client)

    # list_users = {'name': 'Ratul', 'Age': 27, 'subject': ['DSA','OOP']}
    # collection.insert_one(list_users)
    # list_users = [{
    #     'name': 'Nicolas',
    #     'age': 114,
    #     'subject': ['Machine Learning','Magnetic field']
    # },{
    #     'name': 'Albert',
    #     'age': 150,
    #     'subject': ['Magnetic field','Physics']
    # }]
    # collection.insert_many(list_users)
    app.run(debug=True)
