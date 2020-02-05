class Libro:
	def __init__(self):
		self.nombre=""
		

	def consulta(self):	
		nombre = open ('titulos.txt','r')
		mensaje = nombre.read()
		print(mensaje)
		nombre.close()

	def consulta_nombre(self):
		titulo=input("Introduce titulo que deseas buscar -> ")
		f = open("titulos.txt", "r")
		for linea in f:#Esta tomando cada linea de este texto
			linea = linea.rstrip('\n')#quita el salto de linea
			
			if titulo == linea:#si titulo es igual a linea compara el titulo q he metido con cada una de las lineas
				print("\nEl título ",linea," si se encuentra\n")
				bandera=0
				break
			else:
				bandera=1

		if bandera==1:
			print("Este título no se encuentra")
		f.close()
