kg=input("Quantos kilos você pescou? ")
if( int(kg)>=50):
	print("Acima do limite")
	print(str(int(kg)-50) + " acima do peso")
	print("R$"+str((int(kg)-50)*4) + " você vai ter que pagar")
else:
	print("Ta suave")
