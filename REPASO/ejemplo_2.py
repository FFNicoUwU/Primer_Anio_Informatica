import os     #-->importo el sistema operativo

os.system("cls")    #limpia la pantalla
nombre= str(input("Ingrese nombre: "))
edad= int(input("Ingrese edad: "))

#print en bloque
os.system("cls")
print(f'''
      {nombre}       {edad} años
      
      ''')