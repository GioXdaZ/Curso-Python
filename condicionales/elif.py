ingreso_mesual = 12000
gasto_mensual = 12000

# if anidados y else if (elif)

if ingreso_mesual > 10000:
    if ingreso_mesual - gasto_mensual <= 0:
        print('estas en banca rota')
    elif ingreso_mesual - gasto_mensual > 3000:
        print('estas bien economicamente')
    else:
        print('estas gastando demasiado')

elif ingreso_mesual > 1000:
    print('estas bien economicamente en latinoamerica')


else:
    print('eres pobre')