cont = 0 
lista = []
while(cont<4):
	a = input("Fala o sua " + str(cont) + "º nota: ")
	lista.append(a)
	cont= cont + 1

media=0
for cont in lista:
	media = media + int(cont)
print(int(media/4))
