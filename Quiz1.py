#Quiz1.py
#Erick Iván Vizcarra Hernández
def triangles(x):
	contador2=1
	contador=0
	while(contador!=x):
		a= "T"
		a=a*contador2
		contador=contador+1
		print(a)
		contador2=contador2+1
	if(x==contador):
		contador2= x
		contador= x-1
		while(contador!=0):
			a="T"
			contador2=contador2-1
			contador=contador-1
			a=a*contador2
			print(a)
x=int(input("Dame un numero: "))
r=triangles(x)
