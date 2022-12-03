# SCRIPT DE DIVISION DE ARCHIVOS Y REPARTO EN CARPETAS
# Abre un examen en un unico archivo y lo reparte en las CARPETAS
# Se debe ejecutar en el directorio compartido de OneDrive.
# folders.csv contiene en una columna los nombres de las carpetas de los alumnos
# y en  la otra el número de páginas que han empleado.

from PyPDF2 import PdfFileWriter, PdfFileReader
import csv
import os
import shutil
import sys

#el primer argumento es el nombre del pdf a trocear. El segundo es el nombre de archivo que queremos usar
if len(sys.argv) == 3:
    archivoOriginal = sys.argv[1]
    nombreArchivo=sys.argv[2]

    #abrimos el archivo original con descriptor infile
    infile = PdfFileReader(open(archivoOriginal, 'rb'))
    #Abre "archivo.pdf" y lo trocea en paginas
    # modifica el nombre en Funciones

    #abrimos el csv para sacar los nombres de las carpetas
    f = open('folders.csv')
    csv_f = csv.reader(f)
    nalumnos = sum(1 for row in csv_f)

    #abrimos el csv para sacar los los números de páginas que han usado cada uno
    f2 = open('folders.csv')
    csv_f2 = csv.reader(f2, delimiter=';')
    alumnos=[]
    hojas=[]
    filas=0
    puntero=-1

    for row in csv_f2:
      alumnos.append(row[0])
      hojas.append(row[1])
      filas=filas+1

    for i in range(nalumnos):
        outfile = PdfFileWriter()
        for j in range(int(hojas[i])):
            puntero=puntero+1;
            p = infile.getPage(puntero)
            outfile.addPage(p)
            indice=i*4+j
            cadena=alumnos[i]
        with open(cadena+nombreArchivo, 'wb') as f:
            outfile.write(f)
        shutil.move('./'+cadena+nombreArchivo, './'+cadena+'/'+cadena+nombreArchivo);
else:
    print("Error - Introduce los argumentos correctamente")
    print("Ejemplo: split.py 'archivo_escaneado.pdf' 'nombre_nuevo.pdf'")
