#Enteros -> int
#Conversion de datos

#Importacion
import math


num1 = input('Ingresa un numero') #num es tipo String
print(type(num1))
num1 = int(num1) # Conversion de a entero
print(num1+20)

#En una sola lina de codigo, tomo la entrada de input y la convierto a entero
num2 = int(input('Ingrese otro numero>'))
print (num2+2)

#
num3= int(True)
#True -->1
#False -->0
print(num3)

#Operadores numericos 
a,b=2,3


# suma
print('\n\tOperaciones con numeros\n')
print('Suma: ',a+b)
#Resta
print('Resta: ',a-b)
#Multiciplicacion
print('Multiplicacion: ',a*b)
#Division
print('Division: ',a/b)
#Division de dos numeros siempre sera un numero flotante
#print(int(10/3))

#Potencia
print('Potencia',2**3)

# Modulo
print('Modulo',a%b)

#Division entera
print('Division entera',10//3)

#Raiz
print('Raiz con potencia',64**(1/2))
print('Raiz cuadrada', math.sqrt(64))

#Floats
numeroFlotante = float(input('Ingresa un numero decimal: '))
print(numeroFlotante)

#Operadores son los mismos que los enteros





