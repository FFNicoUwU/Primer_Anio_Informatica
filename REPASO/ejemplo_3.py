import os
import math
#solicitar al usuario 3 notas(float)
#y calcular el promedio... imprimir datos!!

nota1=float(input('Ingrese nota 1: '))
nota2=float(input('Ingrese nota 2: '))
nota3=float(input('Ingrese nota 3: '))

suma=nota1+nota2+nota3

promedio=suma/3

if promedio>=4:
    estado=("APROBADO")
else:
    estado=("REPROBADO")

x=math.trunc(promedio)


if x>= 4:
    print(f'''
          -----------TICKET---------
          NOTA1: {nota1} NOTA2: {nota2} NOTA3: {nota3}
          Promedio:{x}       ESTADO:{estado}
          ''')