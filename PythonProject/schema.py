from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=80))
    password = fields.Str(required=True, validate=validate.Length(min=6))
    role = fields.Str(validate=validate.OneOf(["user", "admin"]))

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=2, max=80))
    price = fields.Float(required=True, validate=validate.Range(min=0))
    description = fields.Str(validate=validate.Length(max=200))
    quantity = fields.Int(required=True, validate=validate.Range(min=0))

