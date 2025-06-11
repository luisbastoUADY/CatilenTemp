 #!/usr/bin/python
 # -*- coding: iso-8859-15 -*-
import csv, operator
csvarchivo = open('movie_metadata.csv')  # Abrir archivo csv
entrada = csv.reader(csvarchivo)  # Leer todos los registros
reg = next(entrada)  # Leer registro (lista)
print(reg)  # Mostrar registro
color  = next(entrada)  # Leer campos por separado (variables)
print(color)  # Mostrar campos
plot_keywords = next(entrada)
print(plot_keywords)  # Mostrar campos
#del color, entrada  # Borrar objetos
csvarchivo.close()  # Cerrar archivo
del csvarchivo  # Borrar objeto