# from flask import Flask

# app = Flask(__name__)



# @app.route('/home/<string:name>')
# def custom_home(name):
#     return render_template("app.html", name=name)


# # @app.route('/home/<int:product_id>')

# # def product_id
# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask
 
app = Flask(__name__)
 
@app.route('/Home/<string:name>')
def hello_world(name):
    # return f"<h1>Hello, <font color=blue>{name}!</font><h1>"
     return render_template("sample.html", name=name)
 
@app.route('/Product/<int:product_id>')
def product(product_id):
    return f"Product ID: {product_id}"
 
@app.route('/Product/<int:product_id>/<int:quantity>', methods=['POST'])
def product_with_quantity(product_id, quantity):
    return f"Product ID: {product_id}, Quantity: {quantity}"
 
@app.errorhandler(404)
def page_not_found(e):
    return "Page not found", 404
 
if __name__ == '__main__':
    app.run(debug=True)