def LABIV():
	quente = 40
	frio = 10
	atual = int(input("Digite a temperatura atual:"))

	if(atual == frio):
		print("FRIO")
	elif(atual == quente):
		print("QUENTE")
	else:
		if(atual>frio and atual<quente):
			print("NORMAL")
		else:
			print("TEMPERATURA EXTREMA")

def main():
	LABIV()

main()