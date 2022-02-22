#Ejercicio 3
#Validar si los siguientes enlaces son correctos
#https:// y terminar con .com


link1 = 'https://www.epn.edu.ec.ecuador'
link2 = 'https://modemat.com'
link3 = 'http:/fis.edu.lat.com'

print('https://www.epn.edu.ec.ecuador \n')
print('Empieza con https:// \t',link1.startswith('https://'))
print('termina con .com \t',link1.endswith('.com') )

print('\n https://modemat.com ')
print('Empieza con https:// \t',link2.startswith('https://'))
print('termina con .com \t',link2.endswith('.com'))

print('\n http:/fis.edu.lat.com \n')
print('Empieza con https:// \t',link3.startswith('https://'))
print('termina con .com \t',link3.endswith('.com'))


