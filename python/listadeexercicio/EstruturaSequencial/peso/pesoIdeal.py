sexo=input("m/f? ")
if(sexo=="m"):
	h=input("Qual é a sua altura? ")
	peso = (72.7*float(h))-58
	print("O seu peso ideal é: " + str(int(peso)))
elif (sexo=="f"):
	h=input("Qual é a sua altura? ")
	peso = (62.1*float(h))-44.7
	print("O seu peso ideal é: " + str(int(peso)))
