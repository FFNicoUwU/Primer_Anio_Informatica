import os
import time

#=============VARIABLES=============
patente=""
marca=""
modelo=""
año_fabricacion = 0
tipo_vehiculo=""
observacion=""
fecha=""
#============LISTAS VARIABLES==========
lista_patente=[]
lista_marca=[]
lista_modelo=[]
lista_fabricacion=[]
lista_tipo=[]
lista_observacion=[]
lista_fecha=[]
lista_registro=[]
#==============CODIGO PRINCIPAL=============
while True:
    opcion_menu=str(input('''
    ----------Servicio Express----------
    1.- Registrar Automovil
    2.- Registro Mantenimiento
    3.- Consultar Mantenimiento
    4.- Salir
    ------------------------------------
    Elija una opción: '''))

    if opcion_menu=="1":
        os.system("cls")
        print("\n--------Registrar Automovil-----------")

        #PATENTE DEL AUTO
        patente=str(input("Ingrese la patente del vehiculo: ")).strip().upper()
        while not len(patente)==6:
            print("Error...Debe tener 6 caracteres")
            patente=str(input("Ingrese la patente del vehiculo: ")).strip().upper()
        lista_patente.append(patente)

        #MARCA DEL AUTO
        marca=str(input("Ingrese la marca del Vehiculo: ")).capitalize().strip()
        while not len(marca)>0:
            print("Error....No puede dejar vacio, ingrese la marca")
            marca=str(input("Ingrese la marca del Vehiculo: ")).capitalize().strip()
        lista_marca.append(marca)

        #MODELO DEL AUTO
        modelo=str(input("Ingrese el modelo del vehiculo: ")).strip().capitalize()
        while not len(modelo)>0:
            print("Error...No puede dejar en blanco, ingrese el modelo")
            modelo=str(input("Ingrese el modelo del vehiculo: ")).strip().capitalize()
        lista_modelo.append(modelo)
        #AÑO DE FABRICACION DEL AUTO
        while True:
            try:
                año_fabricacion=int(input("Ingrese el año de fabricacion del vehiculo: "))
                break
            except ValueError:
                print("Error...Solo deben ser numeros, ingrese la fecha nuevamente")
        while not 1900<=año_fabricacion<=2022:
            print("Error...Solo se puede en el rango de 1900 hasta 2022, ingrese nuevamente")
            año_fabricacion=str("ingrese el año de fabricación del Vehiculo: ")
        lista_fabricacion.append(año_fabricacion)

        #TIPO DE AUTO
        tipo_vehiculo=str(input("Ingrese el tipo de vehiculo (D;B;E;H): ")).upper().strip()
        while tipo_vehiculo not in ["D","B","E","H"]:
            print("Error...Solo puede poner (D:Diesel;B:Bencina;E:Electrico;H:Hibrido")
            tipo_vehiculo=str(input("Ingrese el tipo de vehiculo: ")).upper().strip()
        lista_tipo.append(tipo_vehiculo)

        op=str(input("¿Desea Agregar un comentario? S/N: ")).strip().upper()
        if op=="S":
            fecha=str(input("Ingrese la fecha dd/mm/aaaa: "))
            observacion=str(input("Ingrese la observación: "))
            obs= f'''
            --------Observación--------
            Fecha: {fecha}
            Observación: {observacion}
            '''
        else:
            obs="Sin observación"

        lista_observacion.append(obs)

        print("Guardando los datos del Vehiculo...")
        print("Espere porfavor...")
        time.sleep(1.5)
        print("El registro se ha guardado con exito")
        os.system("pause")
        os.system("cls")
    
    
    if opcion_menu=="2":
        os.system("cls")
        print("\n------Registro de Mantenimiento-------")
        patente=str(input("Ingrese patente: ")).strip().upper()
        while not len(patente)==6:
            print("Error...deben ser 6 caracteres")
            patente=str(input("Ingrese patente: ")).strip().upper()

        if patente in lista_patente:
            j = lista_patente.index(patente)
            print(f'''
            ----------Ficha De Mantenimiento--------
            Patente: {patente}
            Marca: {lista_marca[j]}
            Modelo: {lista_modelo[j]}
            Año de Fabricación: {lista_fabricacion[j]}
            Tipo de Vehiculo: {lista_tipo[j]}
            Observación:
            {lista_observacion[j]}
            ''')

            print("\n-------Nueva Observación--------")
            fecha=str(input("Ingrese la fecha: "))
            observacion=str(input("Ingrese la observación: "))
            obs= f'''
            -------Observación---------
            Fecha: {fecha}
            Observación: {observacion}
            '''+ lista_observacion[j]
            lista_observacion.pop(j)
            lista_observacion.insert(j, obs)
        
        else:
            print("La patente no esta registrada")
        
        print("Guardando los datos...")
        print("Espere....")
        time.sleep(1.5)
        print("Guardado con exito!!!")
        os.system("pause")
        os.system("cls")


    if opcion_menu=="3":
       os.system("cls")

       print("\n----------Consultar Mantenimiento---------") 
       patente=str(input("Ingrese patente: ")).strip().upper()
       while not len(patente)==6:
           print("Error...Son 6 caracteres, intentelo nuevamente")
           patente=str(input("Ingrese patente: ")).strip().upper()
       if patente in lista_patente:
           j= lista_patente.index(patente)
           print(f'''
           ----------Ficha De Mantenimiento--------
            Patente: {patente}
            Marca: {lista_marca[j]}
            Modelo: {lista_modelo[j]}
            Año de Fabricación: {lista_fabricacion[j]}
            Tipo de Vehiculo: {lista_tipo[j]}
            Observación:
            {lista_observacion[j]}
           ''')
          
       else:
           print("No esta registrado")


       print("Guardando los datos...")
       print("Espere un momento...")
       time.sleep(1.5)
       print("¡¡Guardado con exito!!")
       os.system("pause")
       os.system("cls")


    if opcion_menu=="4":
        seguro= str(input("¿Esta seguro de salir?: ")).upper()
        if seguro=="S":
            print('''
            Usted marco que si
            En unos segundos saldra de la aplicacion
            ''')
            time.sleep(1.5)
            os.system("pause")
            os.system("cls")
            
            break