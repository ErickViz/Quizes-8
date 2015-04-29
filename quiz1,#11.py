#Erick Iván Vizcarra Hernández
import statistics

def numerosrandoms (x):
	b=open(x, "r")
	y=0
	c=0
	lista=[]
	for a in b:
		y=y+int(a)
		c=c+1
		lista.append(int(a))
	r=statistics.stdev(lista)
	print("numero de valores en total: ",c)
	print("El total de la suma de los valores: ",y)
	print("Medida aritmetica de los valores: ",(y/c))
	print("La division de los valores es: ",r)
numerosrandoms("numerosrandom.txt")
