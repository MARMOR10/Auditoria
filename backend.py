from email import message
import mimetypes
from pydoc import resolve
from unicodedata import name
from urllib import response
from flask import Flask, jsonify, request, Response
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb://localhost:27017/database'
#conexiòn para poder manipular las conexiones en mongo db
mongo = PyMongo(app)


@app.route('/products', methods=['POST'])
def create_product():
    # Receiving Data
    name=request.json['name']
    description=request.json['description']
    price=request.json['price']

    if name and description and price:
        _id = mongo.db.products.insert_one(
            {'name':name,'description':description,'price':price}
        )
        id=_id.inserted_id
        print(id)
        response =jsonify({
            'id':str(id),
            'name':name,
            'description':description,
            'price':price
        })      
        return response
    else:    
        return {'message':'received'}
#get
@app.route('/products', methods=['GET'])
def get_products():
    products=mongo.db.products.find()
    #pase los datos en el formato json
    response=json_util.dumps(products)
    return response

#va a buscar lo que le pase el usuario para poder actualizar o eliminar
@app.route('/products/<id>', methods=['GET'])  
def get_product(id):
    product=mongo.db.products.find_one({'_id':ObjectId(id)})
    response =json_util.dumps(product)
    return Response(response,mimetype='application/json')

@app.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    mongo.db.products.delete_one({'_id':ObjectId(id)})
    response=jsonify({'message':'Usuario '+id+ ' fue eliminado salisfatoriamente'})
    return response

@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    #lo que voy a enviar para actualizar
    name=request.json['name']
    description=request.json['description']
    price=request.json['price']

    if name and description and price:
        mongo.db.products.update_one({'_id':ObjectId(id)},{'$set':{
            'name':name,
            'description':description,
            'price':price
        }})
        response=jsonify({'message':'Usuario '+ id +'fue actualizado'})
        return response

@app.errorhandler(404)
def error(error=None):
    message = {
        'message': 'Recurso no encontrado: ' + request.url,
        'status': 404
    }
    #guarda el mensaje en un json para devolver un código 404
    response = jsonify(message)
    response.status_code = 404
    return Response(response, mimetype='application/json')

if __name__ == "__main__":
    app.run(debug=True, port=4000)