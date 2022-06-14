import time
import os
#---------VARIABLES-----------
opcion_menu=""
codigo=""
lista_codigos=[]
nombre=""
lista_nombres=[]
precio=0
lista_precios=[]
pais_origen=""
lista_pais_origen=[]
estilo=""
lista_estilos=[]
avb=0
lista_avb=[]
observacion=""
lista_observaciones=[]

#---------CÓDIGO PRINCIPAL-----------
while True:
    os.system("cls")
    opcion_menu=str(input('''
    -------MENÚ-------
    1.- Registrar cerveza
    2.- Listar cervezas
    3.- Buscar cerveza por código 
    4.- Eliminar registro cerveza
    5.- Modificar registro cerveza
    6.- Buscar cervezas por estilo
    7.- Ingresar observaciones a cerveza 
    8.- Salir
                      
    Ingrese opción:   '''))
    
    if opcion_menu=="1":        
        os.system("cls")
        print("\n-----REGISTRAR CERVEZA---------")
        codigo=str(input("Ingrese código: ")).strip().upper()
        while not len(codigo)==3:
            print("Error..debe ser 3 caracteres")
            codigo=str(input("Ingrese código: ")).strip().upper()
        lista_codigos.append(codigo)    
        
        nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        while not len(nombre)>0:
            print("Error..no puede ser vacio")
            nombre=str(input("Ingrese nombre: ")).strip().capitalize()
        lista_nombres.append(nombre)
        
        precio=int(input("Ingrese precio $"))
        while not precio>0:
            print("Error..debe ser mayor a cero")
            precio=int(input("Ingrese precio $"))
        lista_precios.append(precio)    
        
        pais_origen=str(input("Ingrese país origen: ")).strip().capitalize()
        while not len(pais_origen)>0:
            print("Error..no puede ser vacio")
            pais_origen=str(input("Ingrese país origen: ")).strip().capitalize()
        lista_pais_origen.append(pais_origen)    
            
        estilo=str(input("Ingrese estilo: ")).strip().lower()
        while estilo not in ["frutal","ale", "amber"]:
            print("Error..solo permite: frutal, ale o amber")
            estilo=str(input("Ingrese estilo: ")).strip().lower()
        lista_estilos.append(estilo)    
            
        avb=float(input("Ingrese avb:  "))
        while not avb>=0:
            print("Error..no puede ser negativo")
            avb=float(input("Ingrese avb:  "))
        lista_avb.append(avb)    
        
        op=str(input("¿Desea agregar observación? S/N")).strip().upper()
        if op=="S":
            fecha=str(input("Ingrese fecha dd/mm/aaaa:  "))
            observacion=str(input("Ingrese observacion: "))
            obs= f'''
                ------------OBS-----------
                Fecha: {fecha}
                Observación: {observacion}
                 '''
        else:
            obs="Sin observación"    
        lista_observaciones.append(obs)    
        os.system("pause")
        
    if opcion_menu=="2":
        os.system("cls")
        print("\n----------LISTAR----------")
        for k in range(len(lista_nombres)):
            print(f'''
            {lista_nombres[k]}  {lista_avb[k]}%      
                  ''')
        os.system("pause")
        
    if opcion_menu=="3":
        os.system("cls")
        print("\n-----Buscar cerveza por código----")
        codigo=str(input("Ingrese código: ")).strip().upper()
        while not len(codigo)==3:
            print("Error..debe ser 3 caracteres")
            codigo=str(input("Ingrese código: ")).strip().upper()
        
        if codigo in lista_codigos:
            j = lista_codigos.index(codigo)
            print(f'''
            ----------Ficha Cerveza----------
            Codigo: {codigo}
            Nombre: {lista_nombres[j]}    AVB:{lista_avb[j]}%
            Pais Origen: {lista_pais_origen[j]}
            Estilo: {lista_estilos[j]}
            Precio ${lista_precios[j]}
            Observaciones:
            {lista_observaciones[j]}
                  ''')
        else:
            print("NO ESTA REGISTRADO!!")
           
        
        os.system("pause")
        
    if opcion_menu=="4":
        os.system("cls")
        print("\n------ELiminar un registro-------")
        codigo=str(input("Ingrese código: ")).strip().upper()
        while not len(codigo)==3:
            print("Error..debe ser 3 caracteres")
            codigo=str(input("Ingrese código: ")).strip().upper()
            
        if codigo not in lista_codigos:
            print("EL código no esta registrado")
        else:
            # obtenemos la posición a ELIMINAR
            j = lista_codigos.index(codigo)
            op = str(input(f'''
            Esta a punto de eliminar el registro de la 
            cerveza  {lista_nombres[j]}.
            ¿Estas seguro de borrar? S/N    ''')).upper()
            if op=="S":
                lista_codigos.pop(j)
                lista_nombres.pop(j)
                lista_precios.pop(j)
                lista_avb.pop(j)
                lista_pais_origen.pop(j)
                lista_estilos.pop(j)
                lista_observaciones.pop(j)
            
        os.system("pause")
        
    if opcion_menu=="5":
        os.system("cls")
        print("\n-----MODIFICAR REGISTRO CERVEZA---------")
        codigo=str(input("Ingrese código: ")).strip().upper()
        while not len(codigo)==3:
            print("Error..debe ser 3 caracteres")
            codigo=str(input("Ingrese código: ")).strip().upper()
        
        if codigo not in lista_codigos:
            print("NO esta el registro!!!!")    
        else:
            # averiguamos la posición
            j = lista_codigos.index(codigo)
            print("\n Cargamos la nueva información:")
            nombre=str(input("Ingrese nombre: ")).strip().capitalize()
            while not len(nombre)>0:
                print("Error..esta casilla no puede estar vacia")
                nombre=str(input("Ingrese nombre: ")).strip().capitalize()
            lista_nombres[j]=nombre
            
            precio=int(input("Ingrese precio $"))
            while not precio>0:
                print("Error..debe ser mayor a cero")
                precio=int(input("Ingrese precio $"))
            lista_precios[j]= precio   
            
            pais_origen=str(input("Ingrese país origen: ")).strip().capitalize()
            while not len(pais_origen)>0:
                print("Error..no puede ser vacio")
                pais_origen=str(input("Ingrese país origen: ")).strip().capitalize()
            lista_pais_origen[j]=pais_origen
                
            estilo=str(input("Ingrese estilo: ")).strip().lower()
            while estilo not in ["frutal","ale", "amber"]:
                print("Error..solo permite: frutal, ale o amber")
                estilo=str(input("Ingrese estilo: ")).strip().lower()
            lista_estilos[j]=estilo
                
            avb=float(input("Ingrese avb:  "))
            while not avb>=0:
                print("Error..no puede ser negativo")
                avb=float(input("Ingrese avb:  "))
            lista_avb[j]=avb  
            
            op=str(input("¿Desea agregar observación? S/N")).strip().upper()
            if op=="S":
                fecha=str(input("Ingrese fecha dd/mm/aaaa:  "))
                observacion=str(input("Ingrese observacion: "))
                obs= f'''
                    ------------OBS-----------
                    Fecha: {fecha}
                    Observación: {observacion}
                    '''
            else:
                obs="Sin observación" 
            
            lista_observaciones[j]=obs
            
        os.system("pause")
        
    if opcion_menu=="6":
        os.system("cls")
        print("\n-----Buscar cervezas por estilo--------")
        estilo=str(input("Ingrese estilo: ")).strip().lower()
        while estilo not in ["frutal","ale", "amber"]:
            print("Error..solo permite: frutal, ale o amber")
            estilo=str(input("Ingrese estilo: ")).strip().lower()
        
        print(f"----Cervezas tipo: {estilo.upper()}----")
        for k in range(len(lista_codigos)):
            if estilo== lista_estilos[k]:
                print(f'''
                {lista_nombres[k]}  {lista_avb[k]}%      
                    ''')            
            
        os.system("pause")
        
    if opcion_menu=="7":
        os.system("cls")
        print("\n--------INGRESAR OBSERVACIÓN--------")
        codigo=str(input("Ingrese código: ")).strip().upper()
        while not len(codigo)==3:
            print("Error..debe ser 3 caracteres")
            codigo=str(input("Ingrese código: ")).strip().upper()
        
        if codigo in lista_codigos:
            j = lista_codigos.index(codigo)
            print(f'''
            ----------Ficha Cerveza----------
            Codigo: {codigo}
            Nombre: {lista_nombres[j]}    AVB:{lista_avb[j]}%
            Pais Origen: {lista_pais_origen[j]}
            Estilo: {lista_estilos[j]}
            Precio ${lista_precios[j]}
            Observaciones:
            {lista_observaciones[j]}
                  ''')
            
            print("\n-----NUEVA OBSERVACIÓN---------")
            fecha=str(input("Ingrese fecha dd/mm/aaaa:  "))
            observacion=str(input("Ingrese observacion: "))
            obs= f'''
                ------------OBS-----------
                Fecha: {fecha}
                Observación: {observacion}
                 ''' + lista_observaciones[j]
            lista_observaciones.pop(j)
            lista_observaciones.insert(j, obs)
        else:
            print("NO ESTA REGISTRADO!!")
                        
        os.system("pause")
        
    if opcion_menu=="8":
        seguro= str(input("¿Esta seguro de salir?: ")).upper()
        if seguro=="S":
            print('''
            Usted marco que si
            En unos segundos saldra de la aplicacion
            ''')
            time.sleep(3)
            break
        
# Propuesto....listar las cervezas desde la de mayor
# grado alcoholico a la menor...nombre - avb        