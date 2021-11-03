
class Control: 
    def enlazar(self, televisor):
        self.__tv = televisor
        self.__tv.setControl(self)

    def turnOn(self):
        self.__tv.turnOn()  

    def turnOff(self):
        self.__tv.turnOff()

    def setCanal(self, nuevoCanal):
        self.__tv.setCanal(nuevoCanal)

    def canalUp(self):
        self.__tv.canalUp()

    def canalDown(self):
        self.__tv.canalDown()

    def volumenUp(self):
        self.__tv.volumenUp()

    def volumenDown(self):
        self.__tv.volumenDown() 


    def getTV(self):
        return self.__tv

    def setTV(self, televisor):
        self.__tv = televisor                   

