import os
import time
#----------VARIABLES------------
opcion_menu= 0 
nombre_mascarilla=""
precio_mascarilla= 0
cantidad_mascarillas= 0
delivery=""

misma_comuna= 0
total= 0

#------------CODIGO PRINCIPAL-----------
os.system("cls")

opcion_menu=int(input(f'''
    Producto                    Precio
1.- Mascarilla simple             $1000
2.- Mascarilla con diseño         $1300

Elija su opcion porfavor: '''))

if opcion_menu==1:
    nombre_mascarilla="Mascarilla simple"
    precio_mascarilla= 1000

if opcion_menu==2:
    nombre_mascarilla="Mascarilla con diseño"
    precio_mascarilla= 1300

cantidad_mascarillas=int(input(f'''
Ingrese la cantidad de {nombre_mascarilla} que desea comprar: '''))



total=precio_mascarilla * cantidad_mascarillas

os.system("cls")

if total> 15000:
    print(f'''
    ------------TICKET-----------
    Nombre producto: {nombre_mascarilla}
    Cantidad: {cantidad_mascarillas}
    Precio unitario: {precio_mascarilla}
    Cargo delivery: Sin cargos
    Total a pagar: {total}
    ''')

else:
    delivery=str(input('''
    El encargo es de la misma comuna?
    Seleccione S/N: ''')).upper()

    if delivery=="S":
        misma_comuna= 1000
        print(f'''El precio del delivery seria: {misma_comuna}''')

    else:
        misma_comuna= 3000
        print(f'''El precio del delivery seria: {misma_comuna}''')



    if delivery.upper()=="S":
        print(f'''
        ------------TICKET-----------
        Nombre producto: {nombre_mascarilla}
        Cantidad: {cantidad_mascarillas}
        Precio unitario: ${precio_mascarilla}
        Cargo delivery: ${misma_comuna}
        Total a pagar: ${total+ misma_comuna}

        ''')

    else: 
        print(f'''
        -----------TICKET-------
        Nombre producto: {nombre_mascarilla}
        Cantidad: {cantidad_mascarillas}
        Precio unitario: ${precio_mascarilla}
        Cargo delivery: ${misma_comuna}
        Total a pagar: ${total+ misma_comuna}
    
        ''')




