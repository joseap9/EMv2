class Persona:

    def __init__(self,n,r,s,e):
        self.nombre = n
        self.rut = r
        self.sexo = s
        self.edad = e

    def __gt__(self, persona):
        return self.edad > persona.edad

    def setNombre(self, nombre):
        self.nombre = nombre

    def setRut(self, rut):
        self.rut = rut

    def setSexo(self, sexo):
        self.sexo = sexo

    def setEdad(self, edad):
        self.edad = edad

    def getNombre(self):
        return self.nombre

    def getRut(self):
        return self.rut

    def getSexo(self):
        return self.sexo

    def getEdad(self):
        return self.edad

    def getInfoBreve(self):
        return self.nombre + "  -  " + str(self.rut) + "  -  " + self.sexo

    def __str__(self):
        return self.nombre + "\n" + str(self.rut)  + "\n" + "edad:   "+str(self.edad)