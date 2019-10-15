"""
	@vysery98

	Dada las siguientes placas, filtrar aquellas que pertenecen a las provincias de :

	Loja, Pichincha, Esmeraldas, Azuay, Imbabura

	Placas: lba-001, gma-002, azx-003, ess-004,  oro-100, mab-001, iaj-002
"""

placas = ["lba-001", "gma-002", "azx-003", "ess-004",  "oro-100", "mab-001", "iaj-002"]

def es_valido (x):

	placasValidas = ["l", "p", "e", "a", "i"]

	# x[0] toma unicamente el primer caracter de la placa y las compara con placasValidas
	if x[0] in placasValidas:
		return True
	else:
		return False

resultado = filter(es_valido, placas)

# Presenta unicamente aquellas que cumplan con la condicion de ser de las provincias mencionadas previamente
print(list(resultado))