from televisores.control import Control 

class TV:
   __numTV = 0
   canal = 1
   precio = 500
   volumen = 1
   control = Control()

   def __init__(self, marca, estado):
       self.marca = marca
       self.estado = estado
       TV.__numTV += 1  

   def turnOn(self):
       self.estado = True

   def turnOff(self):
       self.estado = False

   def setCanal(self, nuevoCanal):
       if(self.estado and nuevoCanal >= 1 and nuevoCanal <= 120):
           self.canal = nuevoCanal

   def setVolumen(self, nuevoVolumen):
       if(self.estado and nuevoVolumen >= 0 and nuevoVolumen <= 7):
           self.volumen = nuevoVolumen

   def setPrecio(self, precio):
       self.precio = precio

   def setMarca(self, marca):
       self.marca = marca

   def setControl(self, control):
       self.control = control

   @classmethod
   def setNumTV(cls, numTV):
       cls.__numTV = numTV

   def canalUp(self):
       self.canal += 1

   def canalDown(self):
       self.canal -= 1 

   def volumenUp(self):
       self.volumen += 1

   def volumenDown(self):
       self.volumen -= 1 

   ##aquí empiezan los getters

   def getEstado(self):
       return self.estado

   def getPrecio(self):
       return self.precio

   def getCanal(self):
       return self.canal

   def getVolumen(self):
       return self.volumen

   def getMarca(self):
       return self.marca

   def getControl(self):
       return self.control

   def getNumTV(self):
       return self.__numTV                     


