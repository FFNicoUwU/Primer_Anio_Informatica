import os
#-------VARIABLES-------
nombre=""        #str
peso=0           #int   Kilogramos       
estatura=0       #float metros  
imc=0
clasificacion=""


os.system("cls")

#-------CODIGO PRINCIPAL-------
nombre=str(input("Ingrese su nombre: "))
peso=int(input("Ingrese su peso: "))
estatura=float(input("Ingrese su estatura: "))

imc=peso/estatura**2

if imc < 18.5:
    clasificacion= "bajo peso"

if 18.5>= imc <= 24.9:
    clasificacion= "normal"

if 25 <= imc <=24.9:
    clasificacion= "Sobrepeso" 

if imc >=30:
    clasificacion= "Obeso"
    
    
os.system("cls")
print(f'''
      -----TICKET-----
      Nombre: {nombre}
      Peso: {peso} kg        Estatura: {estatura} cm.
      IMC: {imc}     Clasificacion: {clasificacion}
      ''')