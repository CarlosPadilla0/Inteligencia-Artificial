from nodo import nodo as Nodo

class arbolBinario:
    def __init__(self, dato):
        self.raiz = Nodo(dato)
    
    def agregar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._agregar(dato, self.raiz)
    
    def _agregar(self, dato, nodo):
        if dato < nodo.valor:
            if nodo.izq is None:
                nodo.izq = Nodo(dato)
            else:
                self._agregar(dato, nodo.izq)
        else:
            if nodo.der is None:
                nodo.der = Nodo(dato)
            else:
                self._agregar(dato, nodo.der)
    
    def buscar(self, nodo, dato):
        if nodo is None:
            return None
        if nodo.valor == dato:
            return nodo
        if dato < nodo.valor:
            return self.buscar(nodo.izq, dato)
        else:
            return self.buscar(nodo.der, dato)
