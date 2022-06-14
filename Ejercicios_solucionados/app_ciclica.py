import os 
import time 

#--------------VARIABLES GLOBALES--------------
opcion_menu= ""

lista_nombres=[]    #siempre lo que es lista va con corchetes []
lista_edades= []
lista_run= []

nombre= ""
edad= 0
run= ""

os.system("cls")
#--------------CODIGO PRINCIPAL----------------

while True:
    opcion_menu=str(input('''
    -----------MENU---------
    
    1.- Registrar Usuario 
    2.- Lista de Usuarios
    3.- Buscar Usuario por RUN
    4.- Salir
    
    Elija una opcion porfavor: '''))
    
    if opcion_menu=="1":
        os.system("cls")
        
        print("Registrar usuario")
        
        nombre=str(input('''
        Ingrese su nombre: ''')).strip().capitalize()
        while not len(nombre)>0:
            print("Error... Porfavor ingrese su nombre")
            nombre=str(input("Ingrese su nombre porfavor: ")).strip().capitalize()
        lista_nombres.append(nombre)
        
        edad=int(input('''
        Ingrese su edad: '''))
        while not 18<=100:
            print("Error... Fuera del rango [18-100]")
            edad=int(input("Ingrese su edad: "))
        lista_edades.append(edad)
        
        run=str(input('''
        Ingrese su RUN: ''')).strip()
        #el len cuenta la cantidad de caracteres, si no cuenta los caracteres se crea un bucle de error hasta que ponga los datos que se piden 
        while not len(run)>0:
            print("Error... no puede estar vacio")
            run= str(input("Ingresa run: ")).strip()
        lista_run.append(run)
        
        print(f'''
        Nommre: {lista_nombres}
        Edad: {lista_edades} años
        RUN: {lista_run}
        ''')
        os.system("pause")
        
    if opcion_menu=="2":
        os.system("cls")
        
        print("\n Lista de Usuarios")
        
        for k in range(len(lista_nombres)):
            print(f'''
        Nombre: {lista_nombres[k]}   Edad: {lista_edades[k]} años   RUN: {lista_run[k]}
        ''')
        os.system("pause")
        
    if opcion_menu=="3":
        os.system("cls")
        run=str(input("Ingrese el RUN: ")).strip()
        
        if run not in lista_run:
            print("NO ESTA")
        else:
            k = lista_run.index(run)
            print(f'''
            Nombre: {lista_nombres}
            Edad: {lista_edades}
            RUN: {lista_run}
            ''')
        
        
        
        
    if opcion_menu=="4":
        seguro= str(input("¿Esta seguro de salir?: ")).upper()
        if seguro=="S":
            print('''
            Usted marco que si
            En unos segundos saldra de la aplicacion
            ''')
            os.system("pause")
            break