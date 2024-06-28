
import clases

#1.3 Crear tres objetos de la clase Persona con diferentes valores de atributos.
persona1 = clases.Persona('PEDRO', 18, 'LIMA')
persona2 = clases.Persona('JUAN', 22, 'CUZCO')
persona3 = clases.Persona('MIGUEL', 26, 'AREQUIPA')

#1.4 Acceder y modificar los atributos de los objetos.
print(persona1.nombre)
print(persona2.ciudad)
persona1.nombre = 'DAVID'
persona2.set_edad(50)
print('Nuevo nombre de persona1: ' + persona1.nombre)
print('set_edad => Nueva edad de la persona2: ' + str(persona2.get_edad()))

#2.1 y 2.4 Agregar un método llamado presentarse a la clase Persona que imprima un saludo con el nombre y la edad de la persona.
print(persona2.presentarse())

#2.2 y 2.4 Implementar un método cumplir_años que incremente la edad de la persona en uno.
persona2.cumplir_anos()
print('cumplir_años => Nueva edad de persona2: ' + str(persona2.get_edad()))

#2.3 y 2.4 Crear un método cambiar_ciudad que actualice la ciudad de residencia de la persona.
persona1.cambiar_ciudad('TARAPOTO')
print(persona1.presentarse())


#3.4 Crear un objeto de la clase Estudiante, y llamar a los métodos heredados y específicos de la clase.
estudiante1 = clases.Estudiante('UNIVERSIDAD')
print(estudiante1.estudiar())


#4.4 Crear objetos de las clases Perro y Gato, agregarlos a una lista y llamar a la función hacer_que_suenen
perro1 = clases.Perro()
perro2 = clases.Perro()
gato1 = clases.Gato()
gato2 = clases.Gato()

lista_animales = [perro1, gato1, perro2, gato2]
clases.hacer_que_suenen(lista_animales)