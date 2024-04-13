cadena1 = 'Hola, soy Gio'
cadena2 = 'Bienvenido Gio'
cadena3 = '5661365165'
cadena4 = 'Hola,Que,Tal,Estas'

# convierte a mayusculas
mayusc = cadena1.upper() 

# convierte a minusculas
minusc = cadena1.lower()

# primera letra en mayuscula
primera_letra_mayusc = cadena1.capitalize()

# busca una cadena dentro de otra cadena
# si no hay coincidencia retorna -1
busqueda_find = cadena1.find('g')

# busca una cadena dentro de otra cadena
# si no hay una coincidencia lanza una excepcion
busqueda_index = cadena3.index('5')

# consulta si es numerico devuelve True, de lo contrario devuelve False
es_numerico = cadena3.isnumeric()

# consulta si es alphanumerico devuelve True, de lo contrario devuelve False
es_alpha = cadena3.isalpha()

# cuenta las coincidencias de una cadena dentro de otra cadena
# devuelve la cantidad de veces que coincida
contar_coincidencia = cadena1.count('i')

# cuenta cuantos caracteres contiene una cadena
contar_caracteres = len(cadena1)

# verifica si una cadena comienza con otra cadena dada
# si es asi devuelve True
empieza_con = cadena1.startswith('h')

# verifica si una cadena termina con otra cadena dada
# si es asi devuelve True
termina_con = cadena1.endswith('o')

# reemplaza una parte de una cadena por otra
cadena_nueva = cadena2.replace('Bienvenido', 'Saludos')

# separa en cadenas una cadena que le pasemos
cadena_nueva_2 = cadena2.split()

# ejemplo
cadena_nueva_3 = cadena4.replace(',', ' ').capitalize()

print(cadena_nueva_2[0])
