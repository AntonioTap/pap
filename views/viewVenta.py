from flask import render_template, request, jsonify
from datetime import datetime
from models import db, Producto, Cajero

# Lista temporal para almacenar los productos en la venta
productos_venta = []

def agregar_producto_venta():
    # Aquí obtienes la información del producto a agregar desde el formulario
    id_producto = request.form['id_producto']
    producto = Producto.query.get(id_producto)

    if producto:
        # Agregar el producto a la lista de productos en la venta
        productos_venta.append({'id': producto.id, 'nombre': producto.nombre, 'precio': producto.precio})
        return jsonify({'success': True, 'message': 'Producto agregado a la venta.'})
    else:
        return jsonify({'success': False, 'message': 'Producto no encontrado.'})

def eliminar_producto_venta(id_producto):
    # Remover el producto de la lista de productos en la venta
    for producto in productos_venta:
        if producto['id'] == id_producto:
            productos_venta.remove(producto)
            return jsonify({'success': True, 'message': 'Producto eliminado de la venta.'})
    
    return jsonify({'success': False, 'message': 'Producto no encontrado en la venta.'})

def realizar_venta():
    # Calcular el total de la venta sumando los precios de los productos en la lista productos_venta
    total_venta = sum(producto['precio'] for producto in productos_venta)

    # Obtener la fecha y hora actual
    fecha_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Obtener el nombre del cajero (en este caso, usaremos un valor fijo)
    nombre_cajero = "Nombre del Cajero"  # Debes implementar la obtención del nombre del cajero

    # Actualizar inventario y otros procesos de la base de datos (Debes implementar esta parte)

    # Limpiar la lista de productos en la venta después de realizar la venta
    productos_venta.clear()

    # Renderizar la plantilla de detalles de venta y pasar los valores como argumentos
    return render_template('venta.html', nombre_cajero=nombre_cajero, productos_venta=productos_venta, total_venta=total_venta, fecha_hora=fecha_hora)
