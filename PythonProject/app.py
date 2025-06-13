from flask import Flask, jsonify
from models import db
from config import Config
from auth import auth_bp
from product import product_bp
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

with app.app_context():
    db.create_all()  # ✅ Ensure tables are created before first use

app.register_blueprint(auth_bp)
app.register_blueprint(product_bp)

# ✅ Centralized Error Handling
@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
