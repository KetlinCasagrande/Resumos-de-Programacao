idade =int (input('insira a sua idade'))
if idade < 18:
    print('você é menor de idade.')

elif 18<= idade<60:
    print('Você é adulto.')

elif idade==60:
    print (' Parabéns, você acaba de entrar na melhor idade!')

else:
    print('Já é idoso.')

