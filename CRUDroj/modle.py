class User(db.Model):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(80), unique=True, nullable=False)
    password=db.Column(db.String(120), nullable=False)  
    role=db.Column(db.String(50), nullable=False)  # New field for role
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role
        }
    def set_password(self, password):
        self.password = generate_password_hash(password)
 
    def check_password(self, password):
        return check_password_hash(self.password, password)