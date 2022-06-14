from multiprocessing.sharedctypes import Value
import os
import time

#------------VARIABLES GLOBALES--------------
rut=""
nombre=""
direccion=""
correo=""
edad=0
sexo=""  #F O M
registros=""
fecha=""
ps=""
#-----------LISTAS VARIABLES-----------------
lista_rut=[]
lista_nombre=[]
lista_correo=[]
lista_direccion=[]
lista_edad=[]
lista_sexo=[]
lista_registro=[]
lista_fecha=[]
lista_ps=[]
#----------------CODIGO PRINCIPAL-------------
while True:
    opcion_menu=str(input('''
    ----------Centro Medico DuocUC----------
    1.- Registrar Paciente
    2.- Atención Paciente
    3.- Consultar Datos Paciente
    4.- Salir
    ------------------------------------
    Elija una opción: '''))
    
    
    if opcion_menu=="1":
        os.system("cls")
        
        #RUT DEL PACIENTE
        while True:
            try:
                rut= int(input("Ingrese su rut: "))
                while not 5000000 < rut <= 99999999:
                    print("El rut ingresado no es válido")
                    rut= int(input("Ingrese su rut: "))
                lista_rut.append(rut)
                break
            except: 
                print("El formato es numerico sin puntos ni guion")
        
        #NOMBRE DEL PACIENTE
        nombre=str(input("Ingrese el nombre del Paciente: "))
        while not len(nombre)>0:
            print("Error...No puede estar en blanco, intente nuevamente")
            nombre=str(input("Ingrese el nombre del Paciente: ")).strip().capitalize()
        lista_nombre.append(nombre)
        
        #DIRECCION DEL PACIENTE
        direccion=str(input("Ingrese la dirección del Paciente: ")).strip().capitalize()
        while not len(direccion)>0:
            print("Error...No puede estar en blanco,intente nuevamente")
            direccion=str(input("Ingrese la dirección del Paciente: ")).strip().capitalize()
        lista_direccion.append(direccion)
        
        #CORREO DEL PACIENTE
        correo=str(input("Ingrese el correo del Paciente: ")).strip()
        while not "@" in correo:
            print("Error... Debe de colocar el @")
            correo=str(input("Ingrese el correo del Paciente: ")).strip()
        lista_correo.append(correo)
        
        #EDAD DEL PACIENTE
        while True:
            try:
                edad=int(input("Ingrese la edad del paciente: "))
                while not 0 < edad <= 110:
                    print("Error...La edad ingresada no es correcta")
                    edad=int(input("Ingrese la edad del paciente: "))
                lista_edad.append(edad)
                break
            except:
                "Tiene que ser un numero entero"
        
        #SEXO DEL PACIENTE
        sexo=str(input("Ingrese el sexo del Paciente F/M: ")).strip().upper()
        while sexo not in ["F","M"]:
            print("Error... Solo puede colocar F si es Femenino y M si es Masculino")
            sexo=str(input("Ingrese el sexo del Paciente F/M: ")).strip().upper()
        lista_sexo.append(sexo)
        #PS DEL PACIENTE
        ps=str(input("Cuenta con ISAPRE o FONASA? I/F: ")).strip().upper()
        while ps not in ["I","F"]:
            print("Error... Solo se puede colocar I si es Isapre o F si es Fonasa")
            ps=str(input("Cuenta con ISAPRE o FONASA? I/F: ")).strip().upper()
        lista_ps.append(ps)
        
        #REGISTRO DEL PACIENTE
        op=str(input("¿Desea Agregar un Registro? S/N: ")).strip().upper()
        if op=="S":
            fecha=str(input("Ingrese la fecha dd/mm/aaaa: "))
            registros=str(input("Ingrese el registro: "))
            obs= f'''
            --------Registro Medico--------
            Fecha: {fecha}
            Registro: {registros}
            '''
        else:
            obs="Sin registro"
        
        lista_registro.append(obs)
        
        print("Guardando los datos del paciente...")
        print("Espere porfavor...")
        time.sleep(1.5)
        print("El registro se ha guardado con exito")
        os.system("pause")
        os.system("cls")
        
        
    if opcion_menu=="2":
        os.system("cls")
        
        print("\n--------Atención Del Paciente---------")
        while True:
            try:
                rut= int(input("Ingrese su rut: "))
                while not 5000000 < rut <= 99999999:
                    print("El rut ingresado no es válido")
                    rut= int(input("Ingrese su rut: "))
                break
            except: 
                print("El formato es numerico sin puntos ni guion")
            
        if rut in lista_rut:
            j=lista_rut.index(rut)
            print(f'''
            =========Ficha Paciente=======
            Rut: {rut}
            Nombre:{lista_nombre[j]}
            Edad:{lista_edad[j]}
            Sexo: {lista_sexo[j]}
            Dirección: {lista_direccion[j]}
            Correo: {lista_correo[j]}
            PS: {lista_ps[j]}
            Registros: 
            {lista_registro[j]}
            ''')
            
            print("\n--------Nuevo Registro------")
            fecha=str(input("Ingrese la fecha: "))
            registros=str(input("Ingrese el registro: "))
            obs=f'''
            Fecha: {fecha}
            Registro: {registros}
            '''+ lista_registro[j]
            lista_registro.pop(registros)
            lista_registro.insert(j, obs)
        
        else:
            print("El Rut no esta registrado")
        
        print("Guardando los datos...")
        print("Espere....")
        time.sleep(1.5)
        print("Guardado con exito!!!")
        os.system("pause")
        os.system("cls")

    if opcion_menu=="3":
        os.system("cls")

        print("\n--------Consultar Paciente----------")
        while True:
            try:
                rut= int(input("Ingrese su rut: "))
                while not 5000000 < rut <= 99999999:
                    print("El rut ingresado no es válido")
                    rut= int(input("Ingrese su rut: "))
                break
            except: 
                print("El formato es numerico sin puntos ni guion")
        
        if rut in lista_rut:
            j=lista_rut.index(rut)
            print(f'''
            =========Ficha Paciente=======
            Rut: {rut}
            Nombre:{lista_nombre[j]}
            Edad:{lista_edad[j]}
            Sexo: {lista_sexo[j]}
            Dirección: {lista_direccion[j]}
            Correo: {lista_correo[j]}
            PS: {lista_ps[j]}
            Registros: 
            {lista_registro[j]}
            ''')
        else:
            print("El rut ingresado no esta registrado")
        os.system("pause")

    if opcion_menu=="4":
        os.system("cls")
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
        