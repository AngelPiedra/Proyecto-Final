#Angel Piedra
#Escriba un algoritmo para ordenar una matriz de tamaño n × m de menor a
#mayor con el siguiente proceso: guarde primero por filas, de la 1 a la N, la
#matriz en un vector de tama˜no mn y luego ordene el vector. Finalmente copie
#de nuevo el vector en la matriz.
import random
n = 0; m = 0; aux = 0; b = ""
print("*****Programa para convertir una matriz en un vector y",
" viseversa, y ordenar los elementos de menor a mayor*****")
print("Ingrese el tamaño de la matriz:")
print("Ingrese el número de filas:")
n = int(input())
print("Ingrese el número de columnas:")
m = int(input())
#Llenar matriz
print()
print("Matriz sin ordenar")
A=[[0 for x in range(m)] for y in range(n)]
for i in range (0,n):
    for j in range (0,m):
        A[i][j]=(int)(random.randint(1,50))
        b += str(A[i][j]) + '\t'
    print(b)
    b = ""       
#Convertir de matriz a vector 
print()
print("Matriz convertida en vector:")
print()
print("Desordenado = [  ", end ="")
z = n*m
B=[0 for x in range(z)]
d = 0
for i in range (0, n):
    for j in range (0, m):
        B[d] = A[i][j]
        d = d + 1          
for i in range (0, d):
    print(B[i],"  ", end = "")
print("]")      
#Ordenar vector de menor a mayor
for i in range (0, (z-1)):
    for j in range (0, (z-1)):
        if (B[j] > B[j+1]):
            aux = B[j]
            B[j] = B[j+1]
            B[j+1] = aux
print()    
print("Ordenado = [  ", end ="")
for i in range(0, z):
    print(B[i],"  ", end ="")
print("]")        
#Convertir vector a matriz
C=[[0 for x in range(m)] for y in range(n)]
r = 0
for i in range (0, n):
    for j in range (0, m):
        C[i][j] = B[r]
        r = r + 1
print()
print("Matriz ordenada")
for i in range (0, n):
    for j in range (0, m):
        b += str(C[i][j]) + '\t'
    print(b)
    b = ""       