
# creando una lista (se pueden modificar)
lista = ['Giovanni Dazarola', 'Soy Gio', True, 1.85]

# creando una tupla (que no se puede modificar)
tupla = ('Giovanni Dazarola', 'Soy Gio', True, 1.85)

# esto es valido
# lista[2] = False

#esto no
# tupla[2] = False

# creando un conjusto (set) (no se accede a los elementios por indice,
# no almacena datos duplicados)

conjunto = {'Giovanni Dazarola', 'Soy Gio', True, 1.85}

#print(conjunto[3] -> no se puede acceder al elemento)

# creando un diccionario (dict) (key : value)
diccionario = {
    'nombre' : 'Giovanni Dazarola',
    'canal' : 'GioXdaZ TV',
    'esta emocionado' : True,
    'altura' : 1.85,
    'dato_duplicado': 'GioXdaZ TV'
}

print(diccionario['nombre'])