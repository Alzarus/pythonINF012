def LABIII():
	vetor = [None] * 5
	num = 10
	for x in range(len(vetor)):
		vetor[x] = num
		num+=1
	for x in vetor:
		print(x)
	vetorStrings = ["Zé", "João", "Tonho"]
	for nome in vetorStrings:
		print(nome)
	vetorStrings[0] = "Maria"
	for nome in vetorStrings:
		print(nome)

def main():
	LABIII()

main()