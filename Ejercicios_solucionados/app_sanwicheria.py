import os
import time 
#----------VARIABLES GLOBALES----------
opcion_menu= 0

cantidad_churrasco= 0
cantidad_completo= 0
cantidad_vegetariano= 0
cantidad_barros_luco= 0

precio_churrasco= 1500
precio_completo= 1000
precio_vegetariano= 1200
precio_barros_luco= 3000 

cantidad_total= 0
codigo_descuento= False

#---------------CODIGO PRINCIPAL---------------
os.system("cls")

print(f'''
    Producto     Precio

    Churrasco    $1500
    Completo     $1000
    Vegetariano  $1200
    Barros Luco  $3000


''')

cantidad_churrasco=int(input("Ingrese la cantidad de churrascos que desea: "))
cantidad_completo=int(input("Ingrese la cantidad de completos que desea: "))
cantidad_vegetariano=int(input("Ingrese la cantidad de vegetarianos que desea: "))
cantidad_barros_luco=int(input("Ingrese la cantidad de Barros Luco que desea: "))

cantidad_total= precio_churrasco*cantidad_churrasco + precio_completo*cantidad_completo + precio_vegetariano*cantidad_vegetariano + precio_barros_luco*cantidad_barros_luco

os.system("cls")

print("Su pedido consta de:  ")

if cantidad_churrasco>0:
    print(f'''
    Cantidad de Churrasco: {cantidad_churrasco}
    Valor: ${cantidad_churrasco*precio_churrasco}
    ''')
if cantidad_completo>0:
    print(f'''
    Cantidad de Completos: {cantidad_completo}
    Valor Total: ${cantidad_completo*precio_completo}
    ''')
if cantidad_vegetariano>0:
    print(f'''
    Cantidad de Vegetarianos: {cantidad_vegetariano}
    Valor Total: ${cantidad_vegetariano*precio_vegetariano}
    ''')
if cantidad_barros_luco>0:
    print(f'''
    Cantidad de Barros Luco: {cantidad_barros_luco}
    Valor Total: ${cantidad_barros_luco*precio_barros_luco}
    ''')

print(f'''
Total a pagar: ${cantidad_total}
    
''')

codigo=int(input('''
    Posee codigo de Descuento?
    1.-Si
    2.-No
    '''))

if codigo==1:
    codigo_descuento=True

if codigo_descuento:
    monto_descuento= cantidad_total*0.1

cantidad_total= cantidad_total - monto_descuento

os.system("cls")

print("Su pedido consta de:  ")

if cantidad_churrasco>0:
    print(f'''
    Cantidad de Churrasco: {cantidad_churrasco}
    Valor: ${cantidad_churrasco*precio_churrasco}
    ''')
if cantidad_completo>0:
    print(f'''
    Cantidad de Completos: {cantidad_completo}
    Valor Total: ${cantidad_completo*precio_completo}
    ''')
if cantidad_vegetariano>0:
    print(f'''
    Cantidad de Vegetarianos: {cantidad_vegetariano}
    Valor Total: ${cantidad_vegetariano*precio_vegetariano}
    ''')
if cantidad_barros_luco>0:
    print(f'''
    Cantidad de Barros Luco: {cantidad_barros_luco}
    Valor Total: ${cantidad_barros_luco*precio_barros_luco}
    ''')

if codigo_descuento==True:
    print(f"Descuento del 10%: ${monto_descuento}")

print(f'''
    Total a pagar: ${cantidad_total}

''')

delivery=input('''
¿Desea delivery? S/N
Elija porfavor: ''')
while not len(delivery)>0:
    print("Error... Elija una opcion porfavor")
    delivery=input('''
    ¿Desea delivery? S/N
    Elija porfavor: ''')

if delivery.upper()=="S":
    cantidad_total=cantidad_total+ 1500
    print("El costo del delivery es de $1500")

print(f'''
----------------------------------------
    Total a pagar: {cantidad_total}
----------------------------------------

''')

