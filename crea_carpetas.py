# SCRIPT CREACIÓN DE CARPETAS
# Crea las carpetas para compartir con los alumnos
import csv
import os
import shutil
import sys

#el primer argumento es el nombre del csv para crear las carpetas
if len(sys.argv) == 2:
    archivoCSV = sys.argv[1]

    #Abre "archivo.pdf" y lo trocea en paginas
    # modifica el nombre en Funciones
    #abrimos el csv para sacar nombres de carpetas
    f2 = open('folders.csv')
    csv_f = csv.reader(f2, delimiter=';')
    alumnos=[]
    nalumnos=0
    puntero=-1

    for row in csv_f:
      alumnos.append(row[0])
      nalumnos=nalumnos+1

    for i in range(nalumnos):
        os.mkdir(alumnos[i])
else:
    print("Error - Introduce los argumentos correctamente")
    print("Ejemplo: crear_carpetas.py 'folders.csv'")
