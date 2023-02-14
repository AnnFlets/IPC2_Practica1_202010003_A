class Pila:
    def __init__(self):
        self.elementos = []

    def estaVacia(self):
        return self.elementos == []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        return self.elementos.pop()

    def ordenar(self):
        listaCodigoOrdenado = []
        for elementoPila in self.elementos:
            listaCodigoOrdenado.append(int(elementoPila.obtenerCodigo()))
        listaCodigoOrdenado.sort(reverse=True)
        listaOrdenada = []
        for i in range(self.tamanio()):
            for j in range(self.tamanio()):
                if int(self.elementos[j].obtenerCodigo()) == listaCodigoOrdenado[i]:
                    listaOrdenada.insert(i, self.elementos[j])
        self.elementos = listaOrdenada

    def tamanio(self):
        return len(self.elementos)