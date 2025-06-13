from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy.schema import Sequence
import random
import string

app = Flask(__name__)

# Enable CORS for React frontend
CORS(app, origins=["http://localhost:8080"])

# Oracle DB configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "oracle+oracledb://system:12345@localhost:1521/XE"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ✅ Define Airplane model
class Airplane(db.Model):
    __tablename__ = 'airplanes'
    id = db.Column(db.Integer, Sequence("airplane_id_seq", start=1, increment=1), primary_key=True)
    airplane_number = db.Column(db.String(6), unique=True, nullable=False)
    model = db.Column(db.String(100), nullable=False)
    total_seats = db.Column(db.Integer, nullable=False)
    economy_seats = db.Column(db.Integer, nullable=False)
    business_seats = db.Column(db.Integer, nullable=False)

# ✅ Create all tables
with app.app_context():
    db.create_all()
    print("✅ Airplane table created successfully!")

# Helper function to generate a unique 6-character airplane number
def generate_airplane_number():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# 📍 GET all airplanes
@app.route("/airplanes", methods=["GET"])
def get_airplanes():
    airplanes = Airplane.query.all()
    return jsonify([
        {
            "id": plane.id,
            "airplane_number": plane.airplane_number,
            "model": plane.model,
            "total_seats": plane.total_seats,
            "economy_seats": plane.economy_seats,
            "business_seats": plane.business_seats
        }
        for plane in airplanes
    ])

# ➕ POST add a new airplane
@app.route("/airplanes", methods=["POST"])
def add_airplane():
    data = request.get_json()
    model = data.get("model")
    manufacturer = data.get("manufacturer")
    capacity = data.get("capacity")
    year = data.get("yearManufactured")

    if not all([model, manufacturer, capacity, year]):
        return jsonify({"error": "Missing required fields"}), 400

    # Business logic: assume 70% economy, 30% business seats
    economy = int(capacity * 0.7)
    business = capacity - economy

    airplane_number = generate_airplane_number()
    while Airplane.query.filter_by(airplane_number=airplane_number).first():
        airplane_number = generate_airplane_number()

    new_plane = Airplane(
        airplane_number=airplane_number,
        model=f"{manufacturer} {model}",
        total_seats=capacity,
        economy_seats=economy,
        business_seats=business
    )

    try:
        db.session.add(new_plane)
        db.session.commit()
        return jsonify({
            "id": new_plane.id,
            "airplane_number": new_plane.airplane_number,
            "model": new_plane.model,
            "total_seats": new_plane.total_seats,
            "economy_seats": new_plane.economy_seats,
            "business_seats": new_plane.business_seats
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Database error: {str(e)}"}), 500

# ❌ DELETE airplane
@app.route("/airplanes/<int:airplane_id>", methods=["DELETE"])
def delete_airplane(airplane_id):
    plane = Airplane.query.get(airplane_id)
    if not plane:
        return jsonify({"error": "Airplane not found"}), 404

    db.session.delete(plane)
    db.session.commit()
    return jsonify({"message": "Airplane deleted successfully"}), 200

# ✅ Test Oracle DB connection
with app.app_context():
    try:
        db.engine.connect()
        print("✅ Connected to Oracle Database successfully!")
    except Exception as e:
        print(f"❌ Error connecting to Oracle DB: {e}")

# 🔥 Run app
if __name__ == "__main__":
    app.run(debug=True)
