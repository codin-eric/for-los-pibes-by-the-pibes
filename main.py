'''
Coding-eric video 10
for the people by the people
'''
import random

numeros = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# for num in numeros:
# 	print(num)

# for i in range(10):
# 	print(i)
# else:
# 	print("no hay mas numeros")

# tabla2 = [(i+1)*2 for i in range(10)]

# print(tabla2)

alumnos = []

for i in range(30):
	notas = [random.randint(1, 10) for i in range(3)]
	alumnos.append(notas)


promedios = []
for i in range(30):
	notas = alumnos[i]
	suma = 0
	for nota in notas:
		suma = nota + suma
	promedios.append(suma / 3) 

print(promedios)