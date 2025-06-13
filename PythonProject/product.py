from flask import Blueprint, jsonify, request
from models import db, Product
from schema import ProductSchema
from flask_jwt_extended import jwt_required

product_bp = Blueprint("product_bp", __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# 📖 GET /products/<id> → Retrieve product by ID
@product_bp.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    return jsonify(product_schema.dump(product))

# 📚 GET /products → Retrieve all products
@product_bp.route("/products", methods=["GET"])
def get_all_products():
    products = Product.query.all()
    return jsonify(products_schema.dump(products)), 200

# ➕ POST /products → Add a new product (Requires JWT Authentication)
@product_bp.route("/products", methods=["POST"])
@jwt_required()
def create_product():
    data = request.get_json()
    errors = product_schema.validate(data)  # ✅ Validate input
    if errors:
        print(errors)  # ✅ Debugging step
        return jsonify(errors), 400  # ✅ Return validation errors

    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()
    return jsonify(product_schema.dump(new_product)), 201
