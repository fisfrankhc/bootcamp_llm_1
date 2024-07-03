import clases

#PRODUCTO
producto1 = clases.Producto(
    'Manzana',
    'Fruta roja',
    7.20,
    50,
    'Frutas'
)
result = producto1.get_categoria()
print(result)
producto1.set_categoria('FRUTAS Y VERDURAS')
result1 = producto1.get_categoria()
print(result1)
producto1.set_precio(7.50)
result2 = producto1.get_precio()
print(result2)
result3 = producto1.aplicarDescuentoProducto(5)
print(result3)

#PRODUCTO DIGITAL
digital = clases.ProductoDigital(
    nombre='Curso Python',
    descripcion='Curso completo de Python',
    precio=49.99,
    cantidad_stock=100,
    categoria='Cursos',
    url_descarga='http://example.com/descargar/python',
    tamanio_archivo='1GB'
)
# Llamada al método obtenerInformacion
print(digital.obtenerInformacionDigital())
# Aplicar un descuento del numero mas 5%
digital.aplicarDescuentoDigital(20)
print(digital.aplicarDescuentoDigital(20))
digital2 = clases.ProductoDigital.obtenerInformacionProducto(producto1)
print(digital2)