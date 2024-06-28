from abc import ABC, abstractmethod
class EdadInvalidError(Exception):
    pass
class lab3(ABC):
      @abstractmethod	#indica que es un método abstracto y no voy a declarar un movimiento
      def cumplir_anos(self):
            pass

#EJERCICIO 1: DEFINICION DE CLASES Y OBJETOS
class Persona(lab3):
      def __init__(self, nombre: str, edad: int, ciudad: str):
            self.nombre = nombre
            self.__edad = edad      #ENCAPSULAMIENTO
            self.ciudad = ciudad
      #EJERCICIO 5: ENCAPSULAMIENTO
      def get_edad(self):
            return self.__edad
      def set_edad(self, edad: int):
            if edad >= 0:
                  self.__edad = edad
            else:
                  raise EdadInvalidError("La edad no puede ser negativa.")
            
      #EJERCICIO 2: METODOS
      def presentarse(self):
            return f'Hola, mi nombre es {self.nombre}, tengo {self.__edad} años y soy de {self.ciudad}'
      def cumplir_anos(self):
            self.__edad += 1  
      def cambiar_ciudad(self, ciudad: str):
            self.ciudad = ciudad
            
#EJERCICIO 3: HERENCIA
class Estudiante(Persona):
      def __init__(self, grado: str):
            self.grado = grado
      
      def estudiar(self):
            return f'El estudiante esta estudiando {self.grado}'
      
#EJERCICIO 4: POLIMORFISMO
class Animal:
      def hacer_sonido(self):
            print('Bienvenido a clase animal')
      
class Perro(Animal):
      def hacer_sonido(self):
            print('El perro hace Guauf')
      
class Gato(Animal):
      def hacer_sonido(self):
            print('El gato hace Miau')
      
def hacer_que_suenen(animales):
    for animal in animales:
        animal.hacer_sonido()