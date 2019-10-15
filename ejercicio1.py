"""
	@vysery98
	
	Dado un conjunto de palabras, filtrar todas aquellas que sean 
	palíndromas

	Palabras: "oro", "pais", "ojo", "oso", "radar", "sol", "seres"
"""

conjPalabras = ["oro", "pais", "ojo", "oso", "radar", "sol", "seres"]

# reversed similar a map, poner: "".join
palindromas = filter(lambda x: x == "".join(reversed(x)), conjPalabras)

print(list(palindromas))

