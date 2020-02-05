from libros import Libro

class Libreria:
	def __init__(self):
		self.libro1 = Libro()
		

	def agregar(self,titulo):
		fichero = open('titulos.txt','a')
		fichero.write(titulo + "\n")
		fichero.close()




	def Validar(self):
		valida= input("introduce titulo de libro ")
		documento=open("titulos.txt",'r')
		lect=documento.read()
		res=lect.find(valida)
        

		if(res<0):
			self.agregar(valida)
			print("agregado con exito")
		else:
			print("libro ya existe")



	def eliminar(self):
		tituloEliminar= input("Ingrese el título del libro que quiera eliminar -> ")
		f = open("titulos.txt", "r")
		titulos = f.readlines()#En esta variable estoy guardando todos los titulos
		libreria = open("titulos.txt", "w")#Abro el archivo para sobreescribirlo(borro todo y escribo lo que me interesa escribir)
		existe = False
		for titulo in titulos:#En este ciclo voy a escribir todo lo que ya había otra vez
			if titulo.rstrip('\n') != tituloEliminar:#Estoy filtrando que se escriban todos menos el que voy a eliminar
				libreria.write(titulo)#escribiendo todos los titulos otra ves al archivo menos el que quiero Eliminar
				
			else:
				print("Eliminado con éxito")
				existe= True


		if existe==False:
			print("El título no existe")


	def menu(self):

		while True:
			print("[1] Agregar\t[2] Consultar \t[3]Consulta por título \t[4] Eliminar \t[5] Salir " )
			opcion = input("> ")

			if opcion == "1":                  #poner if en todos el rendimiento puede ser mas lento por eso esta bien el if
				self.Validar()

			elif opcion == "2":
				self.libro1.consulta()

			elif opcion == "3":
				self.libro1.consulta_nombre()

			elif opcion == "4":
				self.eliminar()

			elif opcion == "5":
				nombre = input("Introduzca su nombre\n> ")
				print("Gracias por su visita", nombre)
				break
			else:
				pass
			
libreria1=Libreria() 
libreria1.menu() 
