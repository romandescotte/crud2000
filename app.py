from flask import Flask ,jsonify,request
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)
CORS(app)

app.config.from_object('config')
# configuro la base de datos, con el nombre el usuario y la clave



db= SQLAlchemy(app)
ma=Marshmallow(app)

# defino la tabla
class Producto(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    precio=db.Column(db.Integer)
    stock=db.Column(db.Integer)
    

    def __init__(self,nombre,precio,stock):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.precio=precio
        self.stock=stock

db.create_all()  # crea las tablas
#  ************************************************************
class ProductoSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','precio','stock')
producto_schema=ProductoSchema()            # para crear un producto
productos_schema=ProductoSchema(many=True)  # multiples registros

@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos=Producto.query.all()
    result=productos_schema.dump(all_productos)
    return jsonify(result)

@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=Producto.query.get(id)
    return producto_schema.jsonify(producto)

# programa principal
if __name__=='__main__':  
    app.run(debug=True, port=5000)  
