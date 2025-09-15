continuar= True

while continuar:
   
   numero = int(input("Qual tabuada?"))
   
   for i in range(1, 11):
      print(f"{numero} x {i} = {numero*i}")
     
   continuar = input('Deseja Continuar? (s/n)')
   continuar = True if continuar == 's' else False
     








    # usada para quando não se sabe quantas vezes se precisa de uma repetição