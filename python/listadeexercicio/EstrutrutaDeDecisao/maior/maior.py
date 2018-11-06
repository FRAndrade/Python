lista=[]
for cont in range(3):
	a=input("Digite o " + str(cont+1) + "º número ")
	lista.append(a)
print("O maior numero é: "+str(max(lista)))
