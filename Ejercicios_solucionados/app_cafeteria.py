import os
import time
#-------------------VARIABLES GLOBALES------------------
opcion_menu= 0
nombre_cafe=""
precio_cafe= 0
cantidad_cafe= 0

opcion_agregado= "N"    # S o N
opcion_menu_agregado= 0 
nombre_agregado=""
precio_agregado= 0
total= 0

#-------------------CODIGO PRINCIPAL---------------------
os.system("cls")

opcion_menu=int(input(f'''
    N°   Producto      Precio

    1    Espresso      $750
    2    Cappuccino    $850
    3    Latte         $800
    4    Mocha         $830
    Eliga una opcion: '''))

if opcion_menu==1:
    nombre_cafe="Espresso"
    precio_cafe= 750

if opcion_menu==2:
    nombre_cafe="Cappuccino"
    precio_cafe= 850

if opcion_menu==3:
    nombre_cafe="Latte"
    precio_cafe= 800

if opcion_menu==4:
    nombre_cafe="Mocha"
    precio_cafe= 830

cantidad_cafe= int(input(f'''
Ingrese la cantidad de {nombre_cafe} que desea comprar: '''))

opcion_agregado= str(input('''
Desea agregar un agregado a su cafe?
Elija S/N: ''')).upper()
if opcion_agregado=="S":
    print('''
    ---------------MENU AGREGADOS----------
    1.- Leche         $300
    2.- Chocolate     $200
    3.- Ambos         $500

    ''')
opcion_menu_agregado= int(input("Ingrese la opcion de agregado que desea: "))
if opcion_menu_agregado==1:
    nombre_agregado="Leche"
    precio_agregado= 300

if opcion_menu_agregado==2:
    nombre_agregado="Chocolate"
    precio_agregado= 200

if opcion_menu_agregado==3:
    nombre_agregado="Ambos"
    precio_agregado= 500


total=(precio_cafe+ precio_agregado)* cantidad_cafe


time.sleep(3)
os.system("cls")

if opcion_agregado.upper()=="S":
    print(f'''
    --------------TICKET DE COMPRA--------------
    Tipo de cafe:{nombre_cafe}    ${precio_cafe} C/U
    Agregados: {nombre_agregado}  ${precio_agregado}
    Cantidad: {cantidad_cafe} 
    Total compra: ${total}
    ''') 

else:
        print(f'''
    --------------TICKET DE COMPRA--------------
    Tipo de cafe:{nombre_cafe}    ${precio_cafe}
    Cantidad: {cantidad_cafe}
    Total compra: ${total}
    ''')