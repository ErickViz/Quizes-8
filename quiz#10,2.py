#ErickIvánVizcarra
def dotProduct(v1, v2):
	if (len(v1) != len(v2)):
		print ("ERROR. The vectors have different sizes.")
		return (-1)
	else:
		w = 0
		for (c, d) in zip(v1, v2):
			w = w + (c * d)
		return w

v1 = []
v2 = []
cont = "y"
print ("FIRST VECTOR")
while (cont == "y"):
	c = int(input("Put a value for the first vector:"))
	v1.append(c)
	cont = input("Would you like to continue?: y/n:")
	if (cont != "y"):
		print ("SECOND VECTOR")
		cont1 = "y"
		while (cont1 == "y"):
			d = int(input("Put a value for the second vector:"))
			v2.append(d)
			
			cont1 = input("Would you like to continue?: y/n:")
z = dotProduct(v1, v2)
