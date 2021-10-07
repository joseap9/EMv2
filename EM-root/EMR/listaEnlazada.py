class Nodo:
    def __init__(self, data = None, proximo = None):
        self.data = data
        self.proximo = proximo
        self.clave = None

    def __str__(self):
        return str(self.data)

class ListaEnlazada:

    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0

    def __getitem__(self, index):

        Nodo = self.cabeza

        for i in range(index):
            Nodo = Nodo.proximo
        return Nodo.dat



    # ________________________________________________
    # metodo para ordenar por burbuja
    def ordenamientoBurbuja(self):
        for i in range(self.size - 1):  # for controlling passes of Bubble Sort
            curr = self.cabeza
            nxt = curr.proximo
            prev = None
            while nxt:  # Comparisons in passes
                if curr.data > nxt.data:
                    if prev == None:
                        prev = curr.proximo
                        nxt = nxt.proximo
                        prev.proximo = curr
                        curr.proximo = nxt
                        self.cabeza = prev
                    else:
                        temp = nxt
                        nxt = nxt.proximo
                        prev.proximo = curr.proximo
                        prev = temp
                        temp.proximo = curr
                        curr.proximo = nxt
                else:
                    prev = curr
                    curr = nxt
                    nxt = nxt.proximo
            i = i + 1

    #_________________________________________________
    # metodo para ordenar por seleccion
    def ordenamientoSeleccion(self):

            temp = self.cabeza

            # Traverse the List
            while (temp):

                minn = temp
                r = temp.proximo

                # Traverse the unsorted sublist
                while (r):
                    if (minn.data > r.data):
                        minn = r

                    r = r.proximo

                # Swap Data
                x = temp.data
                temp.data = minn.data
                minn.data = x
                temp = temp.proximo

    # ________________________________________________
    # metodo para ordenar por MergeSort
    def ordenamientoMergeSort(self):

        def sortedMerge(a, b):
            result = None
            # Base cases
            if a == None:
                return b
            if b == None:
                return a

            # pick either a or b and recur..
            if a.data <= b.data:
                result = a
                result.proximo = sortedMerge(a.proximo, b)
            else:
                result = b
                result.proximo = sortedMerge(a, b.proximo)
            return result

        def mergeSort(h):

            # Base case if head is None
            if h == None or h.proximo == None:
                return h

            # get the middle of the list
            middle = getMiddle(h)
            nexttomiddle = middle.proximo

            # set the next of middle node to None
            middle.proximo = None

            # Apply mergeSort on left list
            left = mergeSort(h)

            # Apply mergeSort on right list
            right = mergeSort(nexttomiddle)

            # Merge the left and right lists
            sortedlist = sortedMerge(left, right)
            return sortedlist

        # Utility function to get the middle
        # of the linked list
        def getMiddle(head):
            if head == None:
                return head

            slow = head
            fast = head

            while (fast.proximo != None and
                   fast.proximo.proximo != None):
                slow = slow.proximo
                fast = fast.proximo.proximo

            return slow

        return mergeSort(self.cabeza)

    # Método para agregar elementos en el frente de la lsta encadena
    def adicionarFrente(self, data):
        self.cabeza = Nodo(data=data, proximo=self.cabeza)
        # ________________________________________________

    # Método para verificar si la estructura de datos esta vacia
    def esVacio(self):
        return self.cabeza == None

    # _________________________________________________
    # Método para agregar elementos al final de la lista enlazada
    def adicionarFinal(self, data):
        self.size += 1
        if not self.cabeza:
            self.cabeza = Nodo(data=data)
            return
        curr = self.cabeza
        while curr.proximo:
            curr = curr.proximo
        curr.proximo = Nodo(data=data)

    # Método para eliminar Nodos
    # _________________________________________________
    def eliminarNodo(self, key):
        curr = self.cabeza
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.proximo
        if prev is None:
            self.cabeza = curr.proximo
        elif curr:
            prev.proximo = curr.proximo
            curr.proximo = None


    # __________________________________________
    #metodo para buscar elemento en la lista
    def estaEnLista(self, keyBuscar):
        esta = False
        curr = self.cabeza
        while curr and not esta:
            if curr.clave == keyBuscar:
                esta = True
                break
            curr = curr.proximo
        return esta

    # ___________________________________________________
    # Método para obtener el ultimo Nodo
    def ultimoNodo(self):
        temp = self.cabeza
        while (temp.proximo is not None):
            temp = temp.proximo
        print(temp.data)

    # Método para obtener el primer nodo
    def primerNodo(self):
        temp = self.cabeza
        while (temp.proximo is not None):
            temp = temp.proximo
        print(temp.data)

    # ___________________________________________________
    # Método para imprimir la lista de Nodos
    def imprimirLista(self):
        Nodo = self.cabeza
        while Nodo != None:
            print(Nodo.data, end="\n")
            Nodo = Nodo.proximo

    #Metodo retorno cantidad total de nodos
    def contador(self):
        Nodo = self.cabeza
        len = 0
        while Nodo != None:
            len = len + 1
            Nodo = Nodo.proximo

        return len

   #Metodo para borrar primer Nodo
    def borrarPrimero(self):
        Nodo = self.cabeza
        if self.esVacio() == False:
            Nodo = Nodo.proximo

    #Metodo para iterar nodos
    def iterar(self):
        Nodo = self.cabeza
        while Nodo:
            dato = Nodo.data
            Nodo = Nodo.proximo
            yield dato


    #Metodo para buscar por iteracion
    def buscarPorIteraracion(self, key):

        for n in self.iterar():
            if key == n.data:
                return n
        return "Nodo no encontrado"




