class Nodo:
    def __init__(self, data = None, proximo = None):
        self.data = data
        self.proximo = proximo
        self.clave = None

    def __str__(self):
        return str(self.data)
