diccionario ={
    "nombre" : 'Gio',
    "apellido" : 'Daz',
    "subs" : 1000000
}

# devuelve un objeto dict_keys
claves = diccionario.keys()

# obteniendo un elemento con get()
valor_keys = diccionario.get('nombre')

# eliminando todo del diccionario
# diccionario.clear()

#elimina un elemento del diccionario
diccionario.pop('subs')

#obtiene un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)