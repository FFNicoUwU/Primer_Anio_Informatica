import os
#-------variables--------
nombre=""
edad=0                #mayor o igual a 18
sexo=""              #sera F o M
valor_hora=0
hrs_trabajadas=0
sueldo_bruto=0          #valor hora X hrs trabajadas
dscto_pension=0         # 13% sueldo bruto
dscto_salud=0           # 7% sueldo bruto
liquido_pagar=0         # sueldo bruto menos dsctos

#---------------codigo principal------------------------
os.system("cls")
nombre=str(input("Ingrese su nombre: "))
edad=int(input("Ingrese su edad: "))
sexo=str(input("Ingrese su sexo: F/M ")).upper()

valor_hora=int(input("Ingrese el valor de su hora: "))
hrs_trabajadas=float(input("Ingrese sus horas trabajadas: "))

sueldo_bruto= valor_hora*hrs_trabajadas
dscto_pension= sueldo_bruto*0.13
dscto_salud=sueldo_bruto*0.07
liquido_pagar=(sueldo_bruto-dscto_pension)-dscto_salud

tiempo=0
if sexo=="F":
    tiempo=60-edad
else:
    tiempo=65-edad

os.system("cls")
print(f'''
      -------LIQUIDACION-------
      Nombre= {nombre}        Edad: {edad} años
      Sexo: {sexo}
      Valor Hora ${valor_hora}
      hrs.trabajadas: {hrs_trabajadas} horas
      
      Sueldo Bruto ${sueldo_bruto}
      Dscto Salud 7% ${dscto_salud}
      Dscto Pension 13% ${dscto_pension}
      Liquido Pagar ${liquido_pagar}
      
      Te faltad {tiempo} años para pensionarte
      ''')
