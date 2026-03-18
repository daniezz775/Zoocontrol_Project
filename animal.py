class Animal:
    def __init__(self, identificador, especie, peso):
        self.__identificador = identificador
        self.__especie = especie
        self.__peso = peso

    def get_identificador(self): return self.__identificador
    def get_especie(self): return self.__especie
    def get_peso(self): return self.__peso
