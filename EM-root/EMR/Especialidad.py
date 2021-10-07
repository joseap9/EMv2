class Especialidad:
    def __init__(self,iE,nE):
        self.idEspecialista = iE
        self.nombreEspecialidad = nE
        

    def getIdEspecialista(self):
        return self.idEspecialista

    def getNombreEspecialidad(self):
        return self.nombre

    def setIdEspecialista(self, id):
        self.idEspecialista = id

    def setNombreEspecialidad(self, nom):
        self.nombre = nom

    