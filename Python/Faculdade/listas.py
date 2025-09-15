numeros = [10, 20, 30, 17, 58, 3, 7]
#print (numeros[3])

carros =['Pálio', 'Gol', 'Virtus', 'Onix', 'Ka']
print( '1 ->', carros)

carros.append('Kombi')
print('2 ->', carros)

carros.remove ('Ka')
print('3 ->', carros)

del carros[3]
print ('4 ->', carros)

carros = sorted(carros)
print('5 ->', carros)

for carro in carros:
    print(carro)
