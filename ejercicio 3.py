mayor = 0
maximo = 5
 
for i in range(maximo):
    num = int(input('Digitar 5 numeros diferentes:'))
    if num > mayor:
        mayor = num
 
print(mayor)
