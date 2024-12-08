from flask import Flask, jsonify, request
from flask_cors import CORS # type: ignore
from pymongo import MongoClient
from urllib.parse import quote_plus

app = Flask(__name__)
CORS(app)

username = quote_plus('besbeselyes')
password = quote_plus('')

# linking with mongo database
client = MongoClient(f'mongodb+srv://{username}:{password}@translations.m0mui.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster')
db = client.translationDB
collection = db.translation

@app.route('/')
def home():
    return "Welcome to the Task Management Application"

@app.route('/api/manage', methods=['POST'])
def create():
    data = request.json
    category = data['title']
    category = data['category']
    priority = data['priority']
    desctiption=data['description']
    due_date=data['due_date']
    completion_status=data['comp']
    db.session.commit()
    
@app.route('/api/get', methods=['PUT'])
def get():
    data = request.json
    title = data.get('title')
    description = data.get('description')
    priority = data.get('priority')
    category = data.get('category')
    due_date = data.get('due_date')
    completion_status = data.get('completion_status')
    db.session.commit()

@app.route('/api/get', methods=['GET'])
def get():
    field_value = request.args.get('id')
    query = {"id": field_value}
    projection={'id', 'title', 'description', 'priority','category','due_date','completion_status'}
    documents = list(collection.find(query, projection))
    return jsonify(documents)

@app.route('/api/delete', methods=['DELETE'])
def delete(id):
    task = request.args.get(id)
    db.session.delete(id)
    db.session.commit()