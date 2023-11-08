import os 
import json 
from flask import Flask, request
from flask_pymongo import PyMongo
from bson import json_util, ObjectId

## SET environment variable -export 
MONGODB_URL = os.environ.get("MONGODB_ENDPOINT")  #mongodbUrl

app = Flask(__name__)                            #flask object
app.config["Mongo_URL"] = MONGODB_URL
mongo = PyMongo(app)                             #mongoDb object


@app.route('/')
def hello_world():
    return 'Hello there, its pritesh!'

@app.route('/items',methods=['GET'])
def get_all_items():
    items = list(mongo.db.items.find())
    return parse_json(items), 200

@app.route('/items', methods=['POST'])
def create_item():
    item = request.get_json()
    inserte_item = mongo.db.items.insert_one(item)
    return parse_json(inserted_item.inserted_id),201

@app.route('/items/<item_id>' , methods=['GET'])
def get_item(item_id):
    item = mongo.db.items.find_one_or_404({'_id': ObjectId(item_id)})
    return parse_json(item), 200

@app.route('/items/<item_id>', methods=['PUT'])
 def update_item(item_id):
   item = request.get_json()
   result = mongo.db.items.update_one({'_id': item_id_obj},{'$set':item})
   if result.matched_count == 0:
      return prase_json({'error': 'Item not found'}), 404
    updated_item = mongo.db.items.find_one({'_id': item_id_obj})
   return parse_json({'message': 'Item updated successfully','item':updated_item}),200

@app.route('/items/<item_id>' method=['DELETE'])
def delete_item(item_id):
   item_id_obj = ObjectId(item_id)
   result = mongo.db.items.delete_one({'_id':item_id_obj})
   if result.deleted_count == 0:
     return parse_json({'error': 'Item not found'}),404
   return parse_json({'message':'Item deleted successfully'}) , 200

if __name__ == "__main__":
   app.run(debug=True)

