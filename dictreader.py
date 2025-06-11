import csv
with open('movie_metadata.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	colors = []
	colorIdx = []
	plots = []
	plotIdx = []
	i=0
	for row in reader:
		if row['color'] not in colors:
			i=i+1
			colors.append(row['color'])
			colorIdx.append(i)
		#else:
		#	print "Ya esta el color"
			
		if row['plot_keywords'] not in plots:
			plots.append(row['plot_keywords'])
		#else:
		#	print "Ya esta el plot"	
		
	print ("Lista de colors: ", colors)
	print ("Lista de colorsIdx: ", colorIdx)
	print ("Lista de plots: ", plots)
		#print(listColor, listPlot)