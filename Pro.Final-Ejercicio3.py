#Angel Piedra
#Construir una función que reciba como parámetro una matriz 3x4 entera y
#retorne la cantidad de números primos almacenados en la matriz
import random	
n = 0; cont = 0; b = ""	
print("***Programa para encontrar cuantos numeros primos tiene una matriz***")
#Llenar la matriz  y presentarla
print("La matriz es:")
A=[[0 for x in range(4)] for y in range(4)]
for i in range (0,3):
    for j in range (0,4):
        A[i][j]=(int)(random.randint(1,30))
        b += str(A[i][j]) + '\t'
    print(b)
    b = ""	
#Verificar números primos
print()
for i in range (0, 3):
	for j in range (0, 4):
		n = 2
		while (A[i][j] % n != 0) and (A[i][j] > n):
			n = n + 1
		if (A[i][j] == n):
			print(">El ",n," es un número primo.")
			cont = cont + 1
print()			
print("==>Hay ",cont," números primos en la matriz")