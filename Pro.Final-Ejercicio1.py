cont = 0; n = 0; entero = 0; i = 0
import random
print("***Programa que permite saber cuantos divisores exactos tiene un número entero"
,"dentro de un vector***")
print()
n = int(input("Ingrese el tamaño del vector:"))
#LLENAR EL VECTOR
A = [None] * n
for i in range (0, n):
    A[i] = (int)(random.randint(1, 20))

print("Vector = ",A," ")    
print()
print("Ingrese un número entero:")
entero = int(input())
        
#Determinar los divisores que hay en el vector
for i in range (n):
    if (entero%A[i] == 0):
        cont = cont + 1
            
if (cont !=1):
    print("=>El número tiene ",cont," divisores exactos en el vector.")
else:
    print("=>El número ",entero," tiene ",cont," divisor exacto en el vector.")