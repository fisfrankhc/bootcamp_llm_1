

#2. DEFINICION DE CLASES
class Producto:
   def __init__(self, nombre: str, descripcion: str, precio: int, cantidad_stock: int, categoria: str):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad_stock = cantidad_stock
        self.__categoria = categoria
   
   def obtenerInformacionProducto(self):
      informacionproducto = f'El producto es {self.nombre}, tiene un precio de {self.precio}, cuenta con stock de {self.cantidad_stock}, y pertenece a la categoria de {self.__categoria} '
      return informacionproducto
   
   #EJERCICIO 4: ENCAPSULAMIENTO
   def get_categoria(self):
      return self.__categoria
   def set_categoria(self, categoria: str):
      self.__categoria = categoria
   def get_precio(self):
      return self.__precio
   def set_precio(self, precio: str):
      self.__precio = precio

   def aplicarDescuentoProducto(self, porcentaje: float):
      self.__precio = self.__precio - self.__precio * (porcentaje / 100)
      return round(self.precio, 2)  

class Categoria:
   def __init__(self, nombre, descripcion):
      self.nombre = nombre
      self.descripcion = descripcion

class Proveedor:
   def __init__(self, nombre, direccion, telefono, email):
      self.nombre = nombre
      self.direccion = direccion
      self.telefono = telefono
      self.email = email

class Venta:
   def __init__(self, producto, cantidad, fecha, total):
      self.producto = producto
      self.cantidad = cantidad
      self.fecha = fecha
      self.total = total

#3. HERENCIA Y POLIMORFISMO
class ProductoDigital(Producto):
   def __init__(self, nombre: str, descripcion: str, precio: int, cantidad_stock: int, categoria: str, url_descarga: str, tamanio_archivo: str):
      super().__init__(nombre, descripcion, precio, cantidad_stock, categoria)
      self.url_descarga = url_descarga
      self.tamanio_archivo = tamanio_archivo

   def obtenerUrlArchivo(self):
      urlfinal = f'http://localhost:8000/{self.categoria}/{self.nombre}.png'
      return urlfinal

   def obtenerInformacionDigital(self):
      informaciontotal = f'El producto es {self.nombre}, tiene un precio de {self.precio}, cuenta con stock de {self.cantidad_stock}, se puede descargar desde {self.url_descarga} y el tamaño del archivo es {self.tamanio_archivo}'
      return informaciontotal

   def aplicarDescuentoDigital(self, porcentaje: float):
      descuento_adicional = 5
      porcentaje_total = porcentaje + descuento_adicional
      self.precio = self.precio - self.precio * porcentaje_total/100
      return self.precio

   