from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Product, User
from log import logger
from dotenv import load_dotenv
import os
from flask_jwt_extended import JWTManager,create_access_token, jwt_required, get_jwt_identity,get_jwt
from config import Config
load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)
#app.config["SeCRET_KEY"] = os.getenv('SECRET_KEY')
jwt=JWTManager(app)
 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle+oracledb://system:12345@localhost:1521/?service_name=XEPDB1'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
# db = SQLAlchemy(app)
db.init_app(app)
 
 
 
@app.route("/", methods=["POST","GET"])
def register_user():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "User already exists"}), 400
   
    new_user = User(username=data["username"],id=data["id"], role=data["role"])
    new_user.set_password(data["password"])
    new_user.role = data.get("role", "user")
 
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created successfully"}), 201
 
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
 
    if not user or not user.check_password(data["password"]):
        return jsonify({"msg": "Bad username or password"}), 401
 
    access_token = create_access_token(
        identity=user.username, additional_claims={"role": user.role})
    return jsonify(access_token=access_token), 200
   
 

@app.before_request
def create_tables():
    db.create_all()
 
 
# 📋 READ ALL
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    claims = get_jwt()
    current_user = get_jwt_identity()
    return jsonify({"msg": "Welcome to the protected route!", "user": current_user, "claims": claims}), 200
   
 
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        logger.warning(f'Product ID {product_id} not found.')
        return jsonify({'error': 'Product not found'}), 404
    logger.info(f'Fetched product ID {product_id}')
    return jsonify(product.to_dict()), 200
 
@app.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    logger.info('Fetched all products.')
    return jsonify([product.to_dict() for product in products]), 200    
 
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    try:
        new_product = Product(
            id=data['id'],
            name=data['name'],
            price=data['price'],
            description=data.get('description', ''),
            qyuantity=data.get('qyuantity', 0)
        )
        db.session.add(new_product)
        db.session.commit()
        logger.info(f'Created product: {new_product.name} (ID: {new_product.id})')
        return jsonify(new_product.to_dict()), 201
    except Exception as e:
        logger.error(f'Error creating product: {str(e)}')
        return jsonify({'error': 'Failed to create product'}), 500
 
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        logger.warning(f'Product ID {product_id} not found for update.')
        return jsonify({'error': 'Product not found'}), 404
    data = request.get_json()
    product.name = data['name']
    product.price = data['price']
    product.description = data.get('description', '')
    product.qyuantity = data.get('qyuantity', 0)
    db.session.commit()
    logger.info(f'Updated product ID {product_id}')
    return jsonify(product.to_dict()), 200
 
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        logger.warning(f'Product ID {product_id} not found for deletion.')
        return jsonify({'error': 'Product not found'}), 404
    db.session.delete(product)
    db.session.commit()
    logger.info(f'Deleted product ID {product_id}')
    return jsonify({'message': 'Product deleted successfully'}), 200
 
if __name__ == '__main__':
    logger.info("Starting Flask application...")
    app.run(debug=True)