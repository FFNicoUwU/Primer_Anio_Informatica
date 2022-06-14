print("Centro Medico Duoc: 1.Registrar Paciente ~ 2.Datos del Paciente ~ 3.Atencion Paciente ~ 4. Salir")

opcion = input("Elige una opcion: ")

if opcion == "1":
    print ("Atencion al Paciente")
    with open("ejemplo.csv","a") as archivo:
        
        rut = input("Rut: ")
        edad = input("Edad: ")
        sexo = input("Sexo: ")
        ps = input("Ps: ")
        correo = input("Correo: ")
        print ("Rut del paciente: " ,rut ,",edad: " ,edad,", sexo del paciente:",sexo, ",ps del paciente:",ps, "correo:", correo)

        archivo.write(rut+ "," +edad+ "," +sexo+ "," +ps+ "," +correo+"\n")
        archivo.close()
elif opcion == "2":
    print ("Datos del Paciente")
    with open("ejemplo.csv","r") as archivo:
        
        print (archivo.read())
        archivo.close()
elif opcion == "3":
    with open("ejemplo.csv","a") as archivo:
        
        archivo.truncate(0)
        print ("Atencion Paciente")
        archivo.close()
        
elif opcion == "4":
    with open("ejemplo.csv", "a") as archivo:
        
        archivo.truncate(0)
        print("Vuelva Pronto")
        archivo.close()

else:
    print("Debes de elegir una opcion")
