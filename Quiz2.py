# Quizes
# Erick Iván Vizcarra Hernández
def find_threes(numbers):
	contador=0
	suma=0
	while(contador<len(numbers)):
		r=numbers[contador]
		contador=contador+1
		a=r/3
		b=int(a)
		if(b==a):
			suma=suma+r
	return suma
c=find_threes([0,4,2,6,9,8,3,12])
print(c)
