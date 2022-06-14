import os 
import time 

#------- variables -------
patente = ""
lista_patente = []
marca = ""
lista_marca = []
modelo = ""
lista_modelo = []
año_fabricacion = 0
lista_año = []
tipo_vehiculo = ""
lista_tipo = []
observacion = ""
lista_observacion = []
fecha = ""
lista_fecha = []
lista_registro = []

while True:
    opcion_menu = str(input('''
    --------- ServiExpress ---------
    1- Registar automovil       
    2- Registro Mantenimiento   
    3- Consultar Automovil      
    4- Salir               
    --------------------------------
    Que opcion desea realizar: '''))
    
    if opcion_menu == "1":
        os.system("cls")
        
        print("------ Registrar automovil ------")
        
        #PATENTE DEL VEHICULO
        patente = str(input("Ingrese a patente del vehiculo: ")).upper().strip()
        while not len(patente)==6:
            print("ERROR...RECUERDE SOLO SE PUEDEN 6 CARACTERES!!!")
            patente = str(input("Ingrese a patente del vehiculo: "))
        lista_patente.append(patente)
        
        #AÑO DE FABRICACION
        while True:
            try:
                año_fabricacion = int(input("Ingrese el año de fabricacion del vehiculo: "))
                break
            except ValueError:
                print("ERROR...RECUERDE SOLO DEBEN SER NUMEROS!!!")
        
        while not 1900<=año_fabricacion<=2022:
            print("ERROR...RECUERDE SOLO SE PUEDE UN AÑO DEL RANGO ENTRE 1900 HASTA EL 2022!!!")
            año_fabricacion = int(input("Ingrese el año de fabricacion del vehiculo: "))
        lista_año.append(año_fabricacion)
        
        #Tipo vehiculo
        tipo_vehiculo = str(input("Ingrese el tipo vehiculo: EJ: D/B/E/H :")).upper().strip()
        while tipo_vehiculo not in ["D","B","E","H"]:
            print("ERROR...RECUERDE SOLO SE PUEDEN LOS DIGITOS [D,B,E,H] ")
            tipo_vehiculo = str(input("Ingrese el tipo vehiculo: ")).upper().strip()
        lista_tipo.append(tipo_vehiculo)
        
        #MARCA DEL VEHICULO
        marca = str(input("Ingrese la marca del vehiculo: ")).capitalize().strip()
        while not len(marca)>0:
            print("ERROR...RECUERDE NO LO PUEDE DEJAR VACIO!!!")
            marca = str(input("Ingrese la marca del vehiculo: ")).capitalize().strip()
        lista_marca.append(marca)
        
        #MODELO DEL VEHICILO
        modelo = str(input("Ingrese el modelo del vehiculo: ")).capitalize().strip()
        while not len(modelo)>0:
            print("ERROR.RECUERDE NO LO PUEDE DEJAR VACIO!!!")
            modelo = str(input("Ingrese el modelo del vehiculo: ")).capitalize().strip()
        lista_modelo.append(modelo)
        
        print("Guardando los datos...")
        print("Espere....")
        time.sleep(1.5)
        print("Guardado con exito!!!")
        os.system("pause")
        os.system("cls")
        
    if opcion_menu == "2":
        os.system("cls")
        
        print("------ Registro Manntenimiento ------")
        buscar_patente = str(input("Ingrese la patente del vehiculo ya registrado: ")).strip().upper()
        while buscar_patente not in (lista_patente):
            print("ERROR...LA PATENTE NO SE ENCUENTRA EN EL SISTEMA!!!")
            buscar_patente = str(input("Ingrese la patente del vehiculo ya registrado: ")).strip().upper()
        if buscar_patente in (lista_patente):
            print("Buscando en el sistema....")
            time.sleep(1.5)
            print("La patente se encuentra en el sistema!!!")
            time.sleep(1.5)
            os.system("cls")
            
            #OBSERVACION DEL VEHICULO
            print("------ Registro Manntenimiento ------")
            observacion = str(input("Ingrese la observacion del vehiculo: ")).strip()
            while not len(observacion)>0:
                print("ERROR...RECUERDE NO LO PUEDE DEJAR VACIO!!!")
                observacion = str(input("Ingrese la observacion del vehiculo: ")).strip()
            lista_observacion.append(observacion)
            
            #FECHA DE LA OBSERVACION
            fecha = str(input("Ingrese la fecha de la observacion: EJ: 01/01/2022 :")).strip()
            while not len(fecha)>0:
                print("ERROR...RECUERDE NO LO PUEDE DEJAR VACIO!!!")
                fecha = str(input("Ingrese la fecha de la observacion: EJ: 01/01/2022 :")).strip()
            lista_fecha.append(fecha)
            
            print("Guardando los datos...")
            print("Espere....")
            time.sleep(1.5)
            print("Guardado con exito!!!")
            os.system("pause")
            os.system("cls")
        
    if opcion_menu == "3":
        os.system("cls")
        
        print("------ Consultar Automovil ------")
        buscar_patente1 = str(input("Ingrese la patente del vehiculo a consultar: ")).upper().strip()
        while buscar_patente1 not in (lista_patente):
            print("ERROR...LA PATENTE NO SE ENCUENTRA EN EL SISTEMA!!!")
            buscar_patente1 = str(input("Ingrese la patente del vehiculo a consultar: ")).upper().strip()
        if buscar_patente1 in (lista_patente):
            print("Buscando en el sistema....")
            time.sleep(1.5)
            print("La patente se encuentra en el sistema!!!")
            print("Cargando atributos del vehiculo...")
            time.sleep(1.5)
            os.system("cls")
            
            print("------ Consultar Automovil ------")
            if observacion not in (lista_observacion):
                k=lista_patente.index(buscar_patente1)
                print(f" \n Patente del vehiculo: {lista_patente[k]} \n Año del vehiculo: {lista_año[k]} \n Tipo del vehiculo: {lista_tipo[k]} \n Marca del vehiculo: {lista_marca[k]} \n Modelo del vehiculo: {lista_modelo[k]} \n ")
                os.system("pause")
                os.system("cls")
            elif observacion in (lista_observacion):
                j=lista_patente.index(buscar_patente1)
                print(f" \n Patente del vehiculo: {lista_patente[j]} \n Año del vehiculo: {lista_año[j]} \n Tipo del vehiculo: {lista_tipo[j]} \n Marca del vehiculo: {lista_marca[j]} \n Modelo del vehiculo: {lista_modelo[j]} \n Observacion del vehiculo: {lista_observacion[j]} \n Fecha de la observacion: {lista_fecha[j]} \n ")
                os.system("pause")
                os.system("cls")
                
    if opcion_menu == "4":
        os.system("cls")
        
        salir = str(input("Esta seguro que desea salir? S/N: ")).upper().strip()
        while not len(salir)>0:
            print("ERROR...RECUERDE NO PUEDE DEJARLO VACIO!!!")
            salir = str(input("Esta seguro que desea salir? S/N: ")).upper().strip()
        if salir == "N":
            print("Volviendo...")
            time.sleep(1.5)
            os.system("pause")
            os.system("cls")
        elif salir == "S":
            print("Cerrando sesion....")
            time.sleep(1.5)
            print("Sesion cerrado con exito!!!")
            break