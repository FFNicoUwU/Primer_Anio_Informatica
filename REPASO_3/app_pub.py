import os
#---------VARIABLES---------
opcion_menu=0  # seleccion del usuario
nombre_producto=""  
precio_producto=0
cantidad=0
total=0
es_happy="N"    # "N" o "S"


#---------CODIGO PRINCIPAL---------
os.system("cls")
opcion_menu=int(input('''
    N°	producto	precio
    1	Vodka tónica	$5500
    2	Ron cola        $5000
    3	Cerveza	        $2000
    4	Bebida	        $1500
    Elije opcion:   '''))

if opcion_menu==1:
    nombre_producto="Vodka Tonica"
    precio_producto=5500
if opcion_menu==2:
    nombre_producto="Ron"
    precio_producto=5000
if opcion_menu==3:
    nombre_producto="Cerveza"
    precio_producto=2000
if opcion_menu==4:
    nombre_producto="Bebida"
    precio_producto=1500

cantidad=int(input(f'''
    ¿Cuantos {nombre_producto} quieres?
    '''))
sub_total=precio_producto* cantidad

os.system("cls")
print(f"Subtotal ${sub_total}")

os.system("cls")
es_happy=str(input("Es Happy Hour?")).upper()
if es_happy=='S':
    total=sub_total/2
    print(f'''
          ------Boleta-------
  Nombre del producto: {nombre_producto}
  Precio: ${precio_producto}
  Cantidad: {cantidad}
  Subtotal: {sub_total}
  Dscto por Happy Hour: ${total}
  Total a pagar: ${total}
  
  MUCHAS GRACIAS POR PREFERIRNOS
  ''') 

else: 
    print(f'''
          ------Boleta-------
  Nombre del producto: {nombre_producto}
  Precio: ${precio_producto}
  Cantidad: {cantidad}
  Total a pagar: ${sub_total}
  
  MUCHAS GRACIAS POR PREFERIRNOS''')
