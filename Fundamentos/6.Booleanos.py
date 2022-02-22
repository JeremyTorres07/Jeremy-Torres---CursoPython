##Booleanos
#Dos tipos
#False y True

from re import A


variable1 = True

variable2 = False

print(type(variable1))

print(variable1.bit_length())

##Operadores
#Asignacion = 
#Aritmeticos =
#Strings + -> concatenacion

#Asignacion Complementarios
x = 4
x+=5 #le sumo 5
print(x)
x**=2
print(x)

#Operadores Logicos

#Conjuncion -> y
print(variable1 and variable2)
print(True and True)
print(False and False)

#Disyuncion -> or
print ('OR')
print(variable1 or variable2)
print(False or False)

#Negacion -> not
print('Not')
print(not variable1)
print(not variable2)

#Ejemplo 

#Operadores bit a bit
#AND
print('3: ',True & True) #3. Tomar el truly or falsy y hacer la operacion and
#Operador xor
print('1: ',4 ^ 5)    #1. convertir a binario y de ahi hacer la ejecucion
#xor
print('4: ',4 | False)
#not
print(~False)
#Desplazamiento de bit a bit hacia la derecha
print(True>>False)
#Desplazamiento de bit a bit hacia la izquierda
print(True<<False)

#Operadores Bit a bit
#Bases 10 -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#Binario -> 0, 1
#1 Byte -> 8 bits

#10101010 -> 1 byte
#2^{7}2^{6},2^{5},2^{4},2^{3},2^{2}2^{1},2^{0}

#Computadora representame el numero 3 en un byte
# 00000011 -> 3(base10)
#Computadora representame el numero 5 en un byte
# 00000101 -> 5(base10)

#   101
# & 000
#  -----
#   000

#  1101
#& 1001
#  -----
#  1001  


#Ejemplo de los operadores bit a bit 
var1 = 2   #1 0 
var2 = 3   #1 1
var3 = 5    #1 0 1

print(var1 | var2)
#var1 -> 1 0
#var2 -> 1 1
#       ------
#        11   -> 3 (base10) 
# 
print(var1 ^ var2)
#var1 -> 1 0
#var2 -> 1 1
#       ------
#        01   -> 1 (base10)   

print(~var1)
#var1 ->~00000010
#        11111101

print(var1>>var2)
#10
#11
#0
print(var1<<var2)
print(True&True)
#      1 & 1
#      1 -> True

#Operadores de Pertenencia
#Identidad