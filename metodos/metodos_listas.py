# creando una lista con list()
lista = list(['hola', 'Gio', 32])

# devuelve la cantidad de elemntos de la lista
cantidad_elementos = len(lista)

# agrega elementos a la lista con append
lista.append(88)

# agraga un elemento a la lista en un indice especifico
lista.insert(2, 64)

# agrega varios elementos a la lista
# en forma de lista
lista.extend([55, True])

# elimina un elemento de la lista por el indice
lista.pop(0) # -1 para eliminar el ultimo elemento de la lista

# remueve un elemento de la lista por su valor
lista.remove('Gio')

# elimina todos los elementos de la lista
# lista.clear()

# ordena la lista de forma ascendente 
# (con parametro reverse=True, la ordena de forma descendente)
# lista.sort()

# invierte los elementos de una lista
lista.reverse()

# verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(88)

print(elemento_encontrado)