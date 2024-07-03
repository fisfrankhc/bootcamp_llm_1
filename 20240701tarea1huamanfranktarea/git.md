# LINK GIT
https://github.com/fisfrankhc/bootcamp_llm_1/tree/master


# CLASES.py
Define las clases creadas para el desarrollo de la tarea 1

## class Producto
```
def __init__(self, nombre: str, descripcion: str, precio: int, cantidad_stock: int, categoria: str)
def obtenerInformacionProducto(self):
def get_categoria(self):
def set_categoria(self, categoria: str):
def get_precio(self):
def set_precio(self, precio: str):
def aplicarDescuentoProducto(self, porcentaje: float):
```

## class Categoria:
```
def __init__(self, nombre, descripcion):
```

## class Proveedor:
```
def __init__(self, nombre, direccion, telefono, email):
```

## class Venta:
```
def __init__(self, producto, cantidad, fecha, total):
```

## class ProductoDigital(Producto):
```
def __init__(self, nombre: str, descripcion: str, precio: int, cantidad_stock: int, categoria: str, url_descarga: str, tamanio_archivo: str):
def obtenerUrlArchivo(self):
def obtenerInformacionDigital(self):
def aplicarDescuentoDigital(self, porcentaje: float):
```


# main.py
Describe a los objetos de las instancias correspondientes



