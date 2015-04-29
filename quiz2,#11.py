#Erick Iván Vizcarra Hernández

def banana(x):
	a=open(x, "r")
	c=0
	n=0
	for i in a:
		b=i.lower()
		z=b.find("banana")
		while z!=(-1):
			n=n+1
			z=b.find("banana",(z+1))
	return(n)
f=banana("banana.txt")
print("La palabra banana esta escrita ", f," veces.")
