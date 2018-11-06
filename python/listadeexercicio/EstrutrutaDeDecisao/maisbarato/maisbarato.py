lista=[]
for cont in range(3):
	a=input("Digite o " + str(cont+1) + "º produto ")
	lista.append(a)
print("O mais barato é aquele que possui o preço de: R$"+str(min(lista)))
