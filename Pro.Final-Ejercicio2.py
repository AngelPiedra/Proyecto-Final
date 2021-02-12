#Angel Piedra
#Leer dos matrices 4x6 enteras y determinar si el número mayor de una
#matriz se encuentra en la misma posición exacta en la otra matriz.
import random
mayor0 = 0; mayor1 = 0; posAi = 0; posAj = 0; posBi = 0; posBj = 0; posicion = 0
n = 4; m = 6; b = ""; d = ""
print()
print("Matriz A")
A=[[0 for x in range(m)] for y in range(n)]
for i in range (0,n):
    for j in range (0,m):
        A[i][j]=(int)(random.randint(1,30))
        b += str(A[i][j]) + '\t'
    print(b)
    b = ""
#Determinar el número mayor de la matriz A
for i in range (0, n):
	for j in range (0, m):  
		if (A[i][j] > mayor0):
			mayor0 = A[i][j]			
#Imprimir la posición del número mayor de la matriz A
for i in range (0, n):
	for j in range (0, m):
		if (mayor0 == A[i][j]):
			print ("=>El numero mayor de la matriz A es ",mayor0," en la",
			" posición [",i,"][",j,"]")
			posAi = i
			posAj = j
#MATRIZ B
print()
print("Matriz B")
B=[[0 for x in range(m)] for y in range(n)]
for i in range (0,n):
    for j in range (0,m):
        B[i][j]=(int)(random.randint(1,30))
        d += str(B[i][j]) + '\t'
    print(d)
    d = ""
#Determinar el número mayor de la matriz B
for i in range (0, n):
	for j in range (0, m):
		if (B[i][j] > mayor1):
			mayor1 = B[i][j]
#Imprimir la posición del número mayor de la matriz B
for i in range (0, n):
	for j in range (0,m ):
		if (mayor1 == B[i][j]):
			print("=>El numero mayor de la matriz B es ",mayor1,
			" en la posición [",i,"][",j,"]")
			posBi = i
			posBj = j
#Verificar si los números mayores de las matrices son iguales y 
#coinciden en sus posiciones
if (mayor0 == mayor1):
	if (posAi == posBi) & (posAj == posBj):
		print ("==>Los números mayores de las matrices son iguales ",
		"y coinciden en su posición")
	else:
		print ("==>Los números mayores de las matrices son iguales ",
		"pero no coinciden en su posición")
else:
	print ("==>Los números mayores de las matrices no son iguales")