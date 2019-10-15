"""
	@vysery98

	Dadas las siguiente ciudades, filtrar aquellas que tienen un número par como longitud en sus caracteres.

	Loja, Pichincha, Guayaquil, Zamora, Ibarra, Manabi, Machala,  Portoviejo, Macas
"""

ciudades = ["Loja", "Pichincha", "Guayaquil", "Zamora", "Ibarra", "Manabi", "Machala",  "Portoviejo", "Macas"]

# Funcion para determinar que ciudades tiene numero par como longitud en caracteres
def long_par (x):

	# len determina la longitud de una cadena
	if len(x) % 2 == 0:
		return True
	else:
		return False

resultado = filter(long_par, ciudades)

# Presenta unicamente los validos
print(list(resultado))