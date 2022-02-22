#Strings -->str
#Es un dato indexable
#String es un tipo de dato inmutable
#Inmutable quiere decir que no acepta la re asignacion
#Asignaciones de una unica linea
from traceback import print_tb


x='hola'
y = ' con todos'

#String de varias lineas
texto = '''Libro Quijote
Cervantes
En un pueblo de la mancha...
Ahi esta mi molino
'''
#print(texto)

texto2 ='''
Primera\t linea
Segunda \n linea
Tercera
'''
#print(texto2)

#Operaciones 
cadena1 = 'Python'
cadena2 = 'es un lenguaje de programacion'
#print(type(cadena2))
numero1= 8.5
print(type(numero1))
print(cadena1, cadena2,' interpretado', numero1)

#Concatenacion de Strings es un unir dos variables de tipo string en una sola expresion
print(cadena1 + cadena2 + 'y ademas tengo este numero'+ str(numero1))

cadena3 = cadena1 + cadena2
print(cadena3)

#Clases 
#Atributos
#Metodos-->Funciones
#Las instancias tienen los metodos 

#Formated Strings
nombre = 'Jeremy'
edad = 20
ira = 32.5
universidad = 'EPN'
#1. Basado en variables
print(f'1: Hola mi nombre es {nombre} y mi edad es {edad} y tengo una ira de {ira}')
#2. Llama al metodo de la clase String
print('2: Hola mi nombre es {} y mi edad es {} y tengo un ira de {}'.format(nombre,edad,ira))
#3. Llamada al metodo format pero indicando la posicion
print('3: Hola mi nombre es {0} y mi edad es {1} y tengo un ira de {2}'.format(nombre,edad,ira))
#Con repeticion
print('Mi nombre es {0} estudio en la {1} y ademas trabajo en {1}'.format(nombre,universidad))
#4. Formated string con reasignacion de variables
print('4: Hola mi nombre es {variableNombre} y mi edad es {variableEdad} y tengo un ira de {variableIra}'.format(variableNombre='Jeremy',variableEdad = edad, variableIra = ira))
#Objeto -> str
#Atributos
#metodo -> format

#2 Indexacion
# 'python'
#   |0|1|2|3|4|5|
cadenaTexto = 'Este es un curso de programacion muy buen curso'
print(cadenaTexto[0])
print(cadenaTexto[2])
#Range -> rango
print(len('Hola'))
#0 ->H
#1 ->o
#2 ->l
#3 ->a 
print(len(cadenaTexto)) #32
print(cadenaTexto[0])   #E
print(cadenaTexto[31])  #n
#Error ->print(cadenaTexto[32])  #error
#Error ->print(cadenaTexto[33])  #error
#Cuando yo utilizo los numeros negativos, empiezo a contar de atras hacia adelante 
#Cuando empiezas desde atas hacia adelante se empieza desde el -1
print(cadenaTexto[-1])  #n
print(cadenaTexto[-2])  #o
print(cadenaTexto[-32]) #Error
#Error print(cadenaTexto[-33]) #Error
print(cadenaTexto[1]+cadenaTexto[8]+cadenaTexto[13])
#Error -> cadenaTexto[0]='A'
#Recordemos que el string es inmutabke

letra = cadenaTexto[0]
print(letra)
letra = 'A'
print(letra)

#Indexacion en rangos
#[valorIncluido, valorExcluido]
#[0,2)
print(cadenaTexto[0:2])
print(cadenaTexto[0:10])
print(cadenaTexto[2:20])
print(cadenaTexto[2:20:2]) #Agregar un salto en caso de que se necesite
#Indice hasta el final 
print(cadenaTexto[2:])
#Desde el comienzo hasta el indice
print(cadenaTexto[:3]) 
#Necesito todo el contenido 
print(cadenaTexto[:]) 
print(cadenaTexto[::]) 

#Ejercicio: Invierta toda la variable cadenaTexto
print(cadenaTexto[::-1]) 
cadenaInvertida = cadenaTexto[::-1]
print(cadenaInvertida)

#Funciones en python
print(cadenaTexto.upper())
print(cadenaTexto.lower())
print(cadenaTexto.capitalize())
#Encontrar algo en tu cadena de texto
#en caso de encontrar nos devuelve el indice
print(cadenaTexto.find('curso'))
print('Animales: tigre'.find('tigre'))
#Si el substring que busco no existe python me devuelve -1 
print('Animales: tigre'.find('perro'))
cadenaTexto2 = 'Los ninos juegan en el parque'
#Validad si empiezo con...
print(cadenaTexto2.startswith('Los'))
print(cadenaTexto2.startswith('Las'))
#Validad si empiezo con...
print(cadenaTexto2.endswith('parque'))
print(cadenaTexto2.endswith('cine'))

print(cadenaTexto2.replace('ninos','ninas'))


