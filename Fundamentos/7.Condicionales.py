#Si, sino, entonces
#if, else,y elif

variable1 = True
variable2 = False

#Operador de comparacion


#print(1==1)
#print('hola'=='hola')
#print('Hola'=='hola')

if variable1 and variable2 == True:
    print('La expresion es verdadera')
else:
    print('La expresion es falsa')

#Comprobaciones 

texto = 'Jeremy'
#Python se puede omitir la comparacion a verdadero
#print('hola'=='hola')
#if texto.startswith('J')==Trye
#es igual a escribir
if texto.startswith('J'):
    print('tu nombre empieza con J')
elif texto.startswith('B'):
    print('tu nombre empieza con B')

else: 
    print('Tu nombre no empieza con la letra J')

#Otro tipo de comparaciones
print(10>=10)
print(20<=30)
print(500!=200)
print(200!=200)
print('Jeremy'!='Fer')

x = 10
print(0< x <12)
print(4<5<8<200)

print('A' > 'B')
print('oso' <= 'oso')

