from project import app
from flask import jsonify, render_template
from project.models import Producto, ProductoSchema

producto_schema=ProductoSchema()            # para crear un producto
productos_schema=ProductoSchema(many=True)  # multiples registros

@app.route('/',methods=['GET'])
def get_Productos():   
    all_productos=Producto.query.all()
    result=productos_schema.dump(all_productos)
    producto= jsonify(result) 
    return producto

@app.route('/productos')
def muestraProductos():    
    productos=get_Productos()
    return render_template('index.html', producto = productos)
    
    
    

# @app.route('/productos/<id>',methods=['GET'])
# def get_producto(id):
#     producto=Producto.query.get(id)
#     return producto_schema.jsonify(producto)

    