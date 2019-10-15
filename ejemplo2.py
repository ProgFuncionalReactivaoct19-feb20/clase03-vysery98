"""
	@vysery98
	Uso de .append
"""

datos = [1, 2, 10, 12, 13]

resultado = []

for i in datos:
	if i % 2 == 0:
		resultado.append(i)

print(resultado)