class MetodoClass:

	def Welcome():
		print("Seja Bem Vindo!!!")

	def addTwo(valor):
		return valor+2


	def main():
		MetodoClass.Welcome()
		valor = 3
		print("addTwo(%d) é %d" %(valor, MetodoClass.addTwo(valor)))
		valor = 19
		print("addTwo(%d) é %d" %(valor, MetodoClass.addTwo(valor)))

MetodoClass.main()