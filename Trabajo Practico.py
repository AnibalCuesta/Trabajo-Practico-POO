# 1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
# del rectángulo.

# class rectangulo():
#     def __init__(self, base, altura):
#         self.base=base
#         self.altura=altura

#     def area(self):
#         area=self.base * self.altura
#         print("el Area del rectangulo es ", area)

# rectangulo=rectangulo(25,10)
# rectangulo.area()

# 2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
# como miembros:

# class Mate():
#     def __init__(self,CebMaxima):
#         self.CebRestan=CebMaxima
#         self.Estado="vacio"
#         self.CeMaxima=CebMaxima

#     def cebado(self):
#         if self.Estado=="lleno":
#             print("Cuidado el Mate ya esta Cebado")
#         else:
#             self.Estado="lleno"
#             print("El mate esta Listo para Beber")

#     def beber(self):
#         if self.Estado=="lleno" and self.CebRestan>0:
#             self.Estado="vacio"
#             print("Que rico Mate")
#             if self.CebRestan>0:
#                 self.CebRestan=self.CebRestan-1
#         else:
#             if self.Estado=="vacio":
#                 print("El mate esta Sin Cebar")
#             elif self.CebRestan==0:
#                 print("Advertencia: el mate está lavado.")


# PrimerMate=Mate(1)
# PrimerMate.cebado()
# PrimerMate.beber()
# PrimerMate.beber()
# PrimerMate.cebado()
# PrimerMate.cebado()
# PrimerMate.beber()


# 3) Botella y Sacacorchos
#  Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
#  Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
# destapada.
#  Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
# una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
# sacacorchos ya contiene un corcho.
#  Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
# un corcho.

# class Corcho():
#     def __init__(self,bodega):
#         self.bodega=bodega

# class Botella():
#     def __init__(self,corcho):
#         self.corcho=corcho

# class SacaCorcho():
#     def __init__(self):
#         self.corcho=None

#     def destapa(self,botella):
#         if botella.corcho != "":
#             print("Se destapo la botella")
#             self.corcho = botella.corcho
#             botella.corcho = None
#         else:
#             if self.corcho is not None:
#                 print("El sacacorchos ya contiene un corcho.")

#     def limpiar(self):
#         if self.corcho is None:
#             print("El sacacorchos no contiene un corcho.")
#             self.corcho = None

# Corchito = Corcho("Nanni")
# Botella1 = Botella(Corchito)
# sacacor = SacaCorcho()
# sacacor.destapa(Botella1)
# sacacor.limpiar()

# 4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
# restaurante_nombre y tipo_comida.*** Cree un método describir_restaurante() que muestre estas piezas de información,**** y un
# método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto.*** Luego cree una clase
# Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
# sabores de helado disponibles.***** Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
# al método.

# class Restaurante():
#     def __init__(self,resto_nombre,resto_tipo):
#         self.resto_nombre=resto_nombre
#         self.resto_tipo=resto_tipo
#         self.resto_estado="cerrado"

#     def describir(self):
#         print("El nombre de este Restaurante es ",self.resto_nombre," que se dedica a este tipo ",self.resto_tipo)

#     def abrir(self):
#         if self.resto_estado=="cerrado":
#             print("Se abrio el Restaurante")
#             self.resto_estado="abierto"
#         else:
#             print("El Restaurante ya estaba abierto")

# class Heladeria(Restaurante):
#     def __init__(self, restaurante,hela_sabores):
#         self.restaurante=restaurante
#         self.hela_sabores=hela_sabores

#     def describirHeladeria(self):
#         print("mi restaurante se llama",self.restaurante.resto_nombre,"es de tipo",self.restaurante.resto_tipo,"y tiene estos Sabores",self.hela_sabores)

# RestoLocoto=Restaurante("Locoto","pizeria y heladeria")
# RestoLocoto.describir()
# sabores=["vainilla","Chocolate","pera","menta"]
# MiHeladeria=Heladeria(RestoLocoto,sabores)
# RestoLocoto.abrir()
# MiHeladeria.describirHeladeria()

# 5) Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
# reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
# que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad.
#
#  Escribir una clase Soldado que herede de Personaje, y agregue el atributo ataque y el método atacar, que reciba otro
# personaje, al que le debe hacer el daño indicado por el atributo ataque.

#  Escribir una clase Campesino que herede de Personaje, y agregue el atributo cosecha y el método cosechar, que
# devuelva la cantidad cosechada

# class Personaje():
#     def __init__(self,per_nombre,per_vida,per_pisicion,per_velocidad):
#         self.per_nombre=per_nombre
#         self.per_vida=per_vida
#         self.per_pisicion=per_pisicion
#         self.per_velocidad=per_velocidad

#     def RecibirAtaque(self,ataque):
#         if self.per_vida>0:
#             self.per_vida=self.per_vida-ataque
#             if self.per_vida<=0:
#                 raise Exception("El personaje ",self.per_nombre," ha muerto")
#         else:
#             print("El Personaje ",self.per_nombre," ya esta muerto")

#     def Mover(self,direccion):
#         if direccion == "arriba":
#             self.per_pisicion[1] += self.per_velocidad
#         elif direccion == "abajo":
#             self.per_pisicion[1] -= self.per_velocidad
#         elif direccion == "izquierda":
#             self.per_pisicion[0] -= self.per_velocidad
#         elif direccion == "derecha":
#             self.per_pisicion[0] += self.per_velocidad
#         else:
#             raise ValueError("Dirección no válida")

# class Soldado(Personaje):
#     def __init__(self, per_nombre, per_vida, per_pisicion, per_velocidad,ataque):
#         super().__init__(per_nombre, per_vida, per_pisicion, per_velocidad)
#         self.ataque=ataque

#     def Atacar(self,otro_personaje):
#         otro_personaje.RecibirAtaque(self.ataque)

# class Campesino(Personaje):
#     def __init__(self, per_nombre, per_vida, per_pisicion, per_velocidad,cosecha):
#         super().__init__(per_nombre, per_vida, per_pisicion, per_velocidad)
#         self.cosecha=cosecha

#     def cosechar(self):
#         return self.cosecha
# i=0
# SoldadoRey=Soldado("Rey",100,[0,0],10,30)
# CampesinoLauti=Campesino("Lautaro",80,[5,5],5,50)
# CampesinoLauti.Mover("arriba")
# print("posicion Actual",CampesinoLauti.per_pisicion)
# SoldadoRey.Atacar(CampesinoLauti)
# print("la vida del Campesino es ",CampesinoLauti.per_vida)
# try:
#     SoldadoRey.Mover("hola")
# except ValueError as e: print(e)

# CampesinoLauti.cosechar()
# print(CampesinoLauti.cosecha)

# # 6) Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
# # se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
# # usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
# # Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno.

# class Usuario():

#     def __init__(self,NomApell,Usuario,Clave,Sector,Permisos):
#         self.NomApell=NomApell
#         self.Usuario=Usuario
#         self.Clave=Clave
#         self.Sector=Sector
#         self.Permisos=Permisos

#     def Describir(self):
#         print("El Usuario: ",self.NomApell," Pertenece al Sector:",self.Sector)

#     def Saludar(self):# saludo personalizado para el usuario
#         print("Bienvenido al Sistema de Gestion Sr/a:",self.NomApell)

# Contable=Usuario("German Perez","GPerez","Perez123","Contable","Administrador")
# Administracion=Usuario("Nicolas Diaz","NDiaz","Diaz123","Administracón","Administrador")
# Maestranza=Usuario("Gabriel Cabrera","GCabrera","Cabrera123","Maestranza","Restringido")

# Contable.Describir()
# Administracion.Saludar()
# Administracion.Describir()
# Maestranza.Saludar()

# # 7) Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
# # Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como “puede
# # postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
# # muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método.

# class Admin(Usuario):
#     def __init__(self, usuario, Permisos):
#         self.Usuario=usuario
#         self.Permisos=Permisos

#     def MuestraPermisos(self):
#         print("Los Permisos del Usuario",self.Usuario.NomApell,"son :",self.Permisos)


# ListaPerAdm=["postear en el foro","borrar un post","banear usuario","eliminar registros"]
# Nico=Admin(Administracion,ListaPerAdm)
# Nico.MuestraPermisos()


# 8) Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
# con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
# clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
# el método para mostrar privilegios.

#------------------- punto 8 ---- para mi en el punto 8 cambia la logica de como lo pense al principio por eso reacomodo 
# todo el programa de nuevo usando lo mismo

# class Usuario():
#     def __init__(self,NomApell,Usuario,Clave,Sector):
#         self.NomApell=NomApell
#         self.Usuario=Usuario
#         self.Clave=Clave
#         self.Sector=Sector
    
#     def Describir(self):
#         print("El Usuario: ",self.NomApell," Pertenece al Sector:",self.Sector)

#     def Saludar(self):# saludo personalizado para el usuario
#         print("Bienvenido al Sistema de Gestion Sr/a:",self.NomApell)

# class Privilegios():
#     def __init__(self,Permisos):
#         self.Permisos=Permisos

#     def MuestraPer(self):
#         print("Los Permisos Son: ",self.Permisos)

# class Admin(Usuario):
#     def __init__(self, NomApell, Usuario, Clave, Sector, Permisos):
#         super().__init__(NomApell, Usuario, Clave, Sector)
#         self.Privilegios = Privilegios(Permisos)

#     def mostrar_privilegios(self):
#         self.Privilegios.MuestraPer()

# ListaPerAdm=Privilegios(["postear en el foro","borrar un post","banear usuario","eliminar registros"])
# ListaPerAdm.MuestraPer()

# ListaPerMaes=Privilegios(["Consulta","imprimir reporte"])
# ListaPerMaes.MuestraPer()

# Contable=Usuario("German Perez","GPerez","Perez123","Contable")
# Administracion=Usuario("Nicolas Diaz","NDiaz","Diaz123","Administracón")
# Maestranza=Usuario("Gabriel Cabrera","GCabrera","Cabrera123","Maestranza")

# Nico = Admin("Nicolas Diaz", "NDiaz", "Diaz123", "Administracion", ["postear en el foro", "borrar un post", "banear usuario", "eliminar registros"]) 

# Nico.mostrar_privilegios()

# Contable.Describir()
# Administracion.Saludar()
# Administracion.Describir()
# Maestranza.Saludar()


# 9) Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela
# al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación
# funcionó.