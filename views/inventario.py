from flask import Blueprint, render_template, request
from controllers.conexion import conectar_bd

inventario = Blueprint('inventario', __name__)

@inventario.route('/inventario', methods=['POST'])
def buscar_productos():
    conexion = conectar_bd()
    cursor = conexion.cursor()

    categoria = request.form.get('categoria')
    marca = request.form.get('marca')
    productos=request.form.get('productos')


    consulta = "SELECT p.nombre AS 'Nombre del Producto', p.precio AS 'Precio', IFNULL(SUM(c.cantidad), 0) AS 'Stock', cat.nombre AS 'Categoría', m.nombre AS 'Marca' FROM productos p LEFT JOIN compras c ON p.id_producto = c.id_producto LEFT JOIN categoria cat ON p.categoria = cat.id_categoria LEFT JOIN marca m ON p.marca = m.id_marca GROUP BY p.id_producto, p.nombre, p.precio, cat.nombre, m.nombre;"
    cursor.execute(consulta, (categoria, marca, productos))

    productos = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template('inevtario.html', productos=productos)
