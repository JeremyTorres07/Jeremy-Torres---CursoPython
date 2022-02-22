#Capicuas
#Palindromo

#Solicitar que ingrese por teclado un texto le vamos a indicar si lo ingresado es o no un palindromo

print('\tIdentificador de palindromos')
texto = str(input('Por favor ingrese una cadena de texto: '))
print('\nPalabra de izquierda a derecha:'+texto)
print('Palabra de derecha a izquierda:'+texto[::-1]+'\n')
if texto == texto[::-1]:
    print('Ingresaste un palindromo!!!')
elif texto.lower() == texto[::-1].lower():
    print('Palindromo pero ignorando las mayusculas')
elif texto.replace(' ','') == texto[::-1].replace(' ',''):
    print('Palindromo pero ignorando los espacios')
elif texto.lower().replace(' ','') == texto[::-1].lower().replace(' ',''):
    print('Palindromo ignorando las mayusculas y los espacios')
else:
    print('No ingresaste un palindromo')