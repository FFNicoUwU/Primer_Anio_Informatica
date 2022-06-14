import os
#------------ VARIABLES ------------
opcion_menu=""
rut=""
lista_rut=[]
nombre=""
lista_nombres=[]
direccion=""
lista_direcciones=[]
comuna=""
lista_comunas=[]
correo=""
lista_correos=[]
edad=0    #----> número entero entre 0 y 110
lista_edades=[]
genero=""   #---> F o M
lista_generos=[]
celular=""
lista_celulares=[]
tipo=""    #----> Premium – Gold – Silver 
lista_tipos=[]
suscripcion=""
lista_suscripciones=[]
#------------ CÓDIGO PRINCIPAL ------------

while True:
    os.system("cls")
    opcion_menu=str(input('''
    ---------MENÚ---------
    1.- Registrar Cliente
    2.- Suscripcion
    3.- Consultar datos cliente
    4.- Salir                      
    
    Elija opción: '''))
    
    if opcion_menu=="1":
        os.system("cls")
        print("\n--Registrar cliente-------")
        rut= str(input("Ingrese rut: ")).strip()
        while not len(rut)>0:
            print("Error...no puede ser vacio")
            rut= str(input("Ingrese rut: ")).strip()
        # dentro del rango de 4000000 y 99999999
        rut_num = int(rut)   #convierte a int el str
        while not 4000000<=rut_num<=99999999:
            print("Error fuera de rango 4MM a 99MM")
            rut= str(input("Ingrese rut: ")).strip()
            rut_num = int(rut)
        lista_rut.append(rut)
        
        nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        while not len(nombre)>0:
            print("Error...no puede ser vacio")
            nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        lista_nombres.append(nombre)
        
        direccion=str(input("Ingrese dirección: ")).strip()
        while not len(direccion)>0:
            print("Error...no puede ser vacio")
            direccion=str(input("Ingrese dirección: ")).strip()
        lista_direcciones.append(direccion)
        
        comuna=str(input("Ingrese comuna: ")).strip().capitalize()
        while not len(comuna)>0:
            print("Error...no puede ser vacio")
            comuna=str(input("Ingrese comuna: ")).strip().capitalize()
        lista_comunas.append(comuna)    
        
        correo=str(input("Ingrese correo: ")).strip().lower()
        while not "@" in correo:
            print("Error correo debe tener arroba!")
            correo=str(input("Ingrese correo: ")).strip().lower()
        lista_correos.append(correo) 
         
        edad = int(input("Ingrese edad: "))    
        while not 0<=edad<=110:
            print("Error, fuera rango[0 a 110] ")
            edad = int(input("Ingrese edad: "))
        lista_edades.append(edad)    
        
        genero=str(input("Ingrese genero: F/M ")).strip().upper()
        while not genero in ["F", "M"]:
            print("Error, debe ser F o M")
            genero=str(input("Ingrese genero: F/M ")).strip().upper()
        lista_generos.append(genero)    
        
        celular=str(input("Ingrese celular: ")).strip()
        while not len(celular)>0:
            print("Error, no puede ser vacio!!")
            celular=str(input("Ingrese celular: ")).strip()
        lista_celulares.append(celular)    
        
        tipo=str(input("Ingrese tipo: ")).strip().capitalize()
        while tipo not in ["Premium","Gold","Silver"]:
            print("Error, es Premium – Gold – Silver ")
            tipo=str(input("Ingrese tipo: ")).strip().capitalize()
        lista_tipos.append(tipo)
        
        suscripcion="suscrito"
        lista_suscripciones.append(suscripcion)    
                    
        os.system("pause")
        
    if opcion_menu=="2":
        os.system("cls")
        os.system("pause")
        
    if opcion_menu=="3":
        os.system("cls")
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
        
