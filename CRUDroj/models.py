from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200), nullable=True)
    qyuantity = db.Column(db.Integer, nullable=False, default=0)
 
    def __repr__(self):
        return f'<Product {self.name}>'
 
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'quantity': self.qyuantity
        }


