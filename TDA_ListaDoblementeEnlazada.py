# TDA_ListaDoblementeEnlazada.py

class Nodo:
    def __init__(self, vuelo):
        self.vuelo = vuelo  # Puede ser un diccionario, objeto, etc.
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._tamano = 0

    def insertar_al_frente(self, vuelo):
        nuevo = Nodo(vuelo)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self._tamano += 1

    def insertar_al_final(self, vuelo):
        nuevo = Nodo(vuelo)
        if self.cola is None:
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        self._tamano += 1

    def obtener_primero(self):
        if self.cabeza is None:
            return None
        return self.cabeza.vuelo

    def obtener_ultimo(self):
        if self.cola is None:
            return None
        return self.cola.vuelo

    def longitud(self):
        return self._tamano

    def insertar_en_posicion(self, vuelo, posicion):
        if posicion <= 0:
            self.insertar_al_frente(vuelo)
        elif posicion >= self._tamano:
            self.insertar_al_final(vuelo)
        else:
            nuevo = Nodo(vuelo)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            anterior = actual.anterior
            anterior.siguiente = nuevo
            nuevo.anterior = anterior
            nuevo.siguiente = actual
            actual.anterior = nuevo
            self._tamano += 1

    def extraer_de_posicion(self, posicion):
        if posicion < 0 or posicion >= self._tamano:
            return None

        if posicion == 0:
            vuelo = self.cabeza.vuelo
            self.cabeza = self.cabeza.siguiente
            if self.cabeza:
                self.cabeza.anterior = None
            else:
                self.cola = None
        elif posicion == self._tamano - 1:
            vuelo = self.cola.vuelo
            self.cola = self.cola.anterior
            if self.cola:
                self.cola.siguiente = None
            else:
                self.cabeza = None
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            vuelo = actual.vuelo
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior

        self._tamano -= 1
        return vuelo

    def obtener_todos(self):
        vuelos = []
        actual = self.cabeza
        while actual:
            vuelos.append(actual.vuelo)
            actual = actual.siguiente
        return vuelos
