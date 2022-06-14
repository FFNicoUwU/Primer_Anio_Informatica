import os
from statistics import mode 

#-------------------VARIABLES GLOBALES------------------
patente=""
marca=""
modelo=""
año_fabricacion=0
tipo_vehiculo="" #bencina,diesel,electrico,hibrido.
registro=""
opcion_menu=""
op=""
observaciones=""
registros=""
fecha=""

#-------------------------LISTAS----------------------
lista_patente=[]
lista_marca=[]
lista_modelo=[]
lista_año_fabricacion=[]
lista_tipo_vehiculo=[]
lista_registro=[]
lista_observaciones=[]

#-------------------CODIGO PRINCIPAL-------------------
while True:
    os.system("cls")
    opcion_menu=str(input('''
    --------------Menú----------------
    1.- Registrar Automovil
    2.- Registrar Mantenimiento
    3.- Consultar Automovil
    4.- Salir
    ----------------------------------

    Elija una opcion: '''))

    if opcion_menu=="1":
        os.system("cls")
        print("\n ---------Registrar Automovil----------")

        patente=str(input("Ingrese su pantente del vehiculo: ")).strip().upper()
        while not len(patente)==6:
            print("Error.....su patente no debe de tener mas de 6 caracteres")
            patente=str(input("Ingrese su pantente del vehiculo: ")).strip().upper()
            lista_patente.append(patente)

        marca=str(input("Ingrese la marca del vehiculo: ")).strip().upper()
        while not len(marca)>0:
            print("Error..... Intentelo nuevamente")
            marca=str(input("Ingrese la marca del vehiculo: ")).strip().upper()
            lista_marca.append(marca)

        modelo=str(input("Ingrese el modelo del vehiculo: ")).strip().capitalize()
        while not len(modelo)>0:
            print("Error..... Intentelo nuevamente")
            modelo=str(input("Ingrese el modelo del vehiculo: ")).strip().capitalize()
            lista_modelo.append(modelo)
        
        año_fabricacion=int(input("Ingrese el año de fabricacion: "))
        while not 1900<=año_fabricacion or año_fabricacion>=2022:
            print("Error... El rango de años es desde 1900 hasta 2022")
            año_fabricacion=int(input("Ingrese el año de fabricacion: "))
            lista_año_fabricacion.append(año_fabricacion)
        
        tipo_vehiculo=str(input("Ingrese tipo de vehiculo:")).strip().upper()
        while tipo_vehiculo not in ["B","D","E","H"]:
            print("Error....Solo se permite B (Bencina),D (Diesel),E (Eléctrico) o H (Híbrido)")
            tipo_vehiculo=str(input("Ingrese tipo de vehiculo:")).strip().upper()
            lista_tipo_vehiculo.append(tipo_vehiculo)

        os.system("pause")
        os.system("cls")

        print(f'''
        =============Ficha de Registro==========
        Patente: {patente}
        Marca: {marca}      Modelo: {modelo}
        Año de Fabricación: {año_fabricacion}
        Tipo de Vehiculo: {tipo_vehiculo}
        ========================================

        ''')
        os.system("pause")


    if opcion_menu=="2":
        os.system("cls")
        print("\n----------Registrar Mantenimiento----------")
        patente=str(input("Ingrese la patente del vehiculo: ")).strip().upper()
        while not len(patente)==6:
            print("Error....Deben ser de 6 caracteres")
            patente=str(input("Ingrese la patente del vehiculo: ")).strip().upper()
        
        if patente in lista_patente:
            j=lista_patente.index(patente)
            print(f'''
            ========Ficha Mantenimiento==========
            Patente: {patente}
            Marca: {lista_marca[j]}   Modelo: {lista_modelo[j]}
            Año de Fabricacion: {lista_año_fabricacion[j]}
            Tipo de Vehiculo: {lista_tipo_vehiculo[j]}
            Observaciones:
            {lista_observaciones[j]}
            ''')

            print("\n------Nueva Observación-------")
            fecha=str(input("Ingrese la fecha de la observación dd/mm/aaaa: "))
            observaciones=str(input("Ingrese la observación: "))
            obs= f'''
                =====Observación=======
                Fecha: {fecha}
                Observación: {observaciones}
                '''+ lista_observaciones[j]
            lista_observaciones.pop(j)
            lista_observaciones.insert(j,obs)
        
        else:
            print("La patente no esta registrada")
        
        os.system("pause")

    if opcion_menu=="3":
        os.system("cls")
        print("\n  -------- CONSULTAR AUTOMOVIL --------")
        patente=str(input("Ingrese patente: ")).strip().upper()
        while not len(patente)==6:
            print("¡Error!, su patente debe tener 6 caracteres")
            patente=str(input("Ingrese su patente: ")).strip().upper()
        if patente in lista_patente:
            j=lista_patente.index(patente)
            print(f'''
            =====================Ficha de Registro=================
            Patente: {patente}   
            Marca: {lista_marca[j]}     Modelo: {lista_modelo[j]}
            Año de Fabricación: {lista_año_fabricacion[j]}
            Tpo: {lista_tipo_vehiculo[j]}
            Observación:\n {lista_observaciones[j]}
            =======================================================
            ''')
        
        else:
            print("El auto no esta registrado :(")
        
        os.system("pause")

    if opcion_menu=="4":
        seguro= str(input("¿Esta seguro de salir?: ")).upper()
        if seguro=="S":
            print('''
            Usted marco que si
            En unos segundos saldra de la aplicacion
            ''')
            os.system("pause")
            break




