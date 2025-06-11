 #!/usr/bin/python
 # -*- coding: iso-8859-15 -*-
import csv, operator
with open('movie_metadata.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo)
    row = next(entrada)
    for row in entrada:
    	lista = list(row)
    	print(lista)  # Cada línea se muestra como una lista de campos
