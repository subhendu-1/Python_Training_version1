from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Product, User  # Ensure User model is imported
from log import logger 
from dotenv import load_dotenv 
import os
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from config import Config

# Initialize Flask app FIRST
app = Flask(__name__)

# Load environment variables
load_dotenv()

# Apply configuration
app.config.from_object(Config)

# Initialize JWT
jwt = JWTManager(app)

# Set database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)



@app.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "User already exists"}), 400
   
    new_user = User(username=data["username"], id=data["id"], role=data["role"])
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

@app.route("/")
def hello_world():
    database_url = os.getenv('DATABASE_URL', 'Unknown Database URL')  # Provide a default value
    return "Hello " + database_url

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
            quantity=data.get('quantity', 0)  # Fixed typo
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
    product.quantity = data.get('quantity', 0)  # Fixed typo
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