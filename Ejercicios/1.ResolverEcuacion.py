#Programa que permita resolver una ecuacion de segundo grado
#ax^{2}+bx+c=0  //a,b y c son numeros enteros
#Ingrese los valores de a, b y c
#Imprimir en consola la ecuacion de segundo grado
#Mostrar las dos soluciones en consola

import math

print('Ingrese los valores correspondientes de a, b y c: ')

a = int(input('Ingrese el valor de a= '))
b = int(input('Ingrese el valor de b= '))
c = int(input('Ingrese el valor de c= '))

print('a: ',a)
print('b: ',c)
print('c: ',b)

print('La ecuacion de segrundo grado es: ')
print(a,'x^2 +',b,'x +',c,'=0')

x1 = ((-1*b) + math.sqrt((b**2)+(4*a*c))) / (2*a)
x2 = ((-1 *b) - math.sqrt((b**2)+(4*a*c))) / (2*a)
 

print('La solucion de la ecuacion de segundo grado es: ')
print ('x1= ', x1,'\tx2= ',x2)



#