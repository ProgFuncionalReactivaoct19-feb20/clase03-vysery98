"""
	@vysery98
	Ejemplo de Higher-order functions
"""

def suma(a, b):
	return a+b

def producto(a, b):
	return a*b

# Función de Orden Superior / Higher-order functions
def disparador(f, a, b):
	print(f(a,b))

disparador(producto, 1, 10)
disparador(suma, 1, 10)