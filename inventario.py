class ItemInventario:
    def __init__(self, codigo, nombre, cantidad):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__cantidad = cantidad

    def get_nombre(self): return self.__nombre
    def get_cantidad(self): return self.__cantidad

    def set_cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.__cantidad = nueva_cantidad
        else:
            print("Error: El stock no puede ser negativo.")

    def gestionar_uso(self):
        return "Uso generico no definido."


class Alimento(ItemInventario):
    def __init__(self, codigo, nombre, cantidad, tipo_dieta):
        super().__init__(codigo, nombre, cantidad)
        self.__tipo_dieta = tipo_dieta

    def gestionar_uso(self):
        return (f"ALIMENTO [{self.get_nombre()}]: Distribuir en zona "
                f"'{self.__tipo_dieta}'. Quedan {self.get_cantidad()} kg/unidades.")


class ImplementoAseo(ItemInventario):
    def __init__(self, codigo, nombre, cantidad, area_asignada):
        super().__init__(codigo, nombre, cantidad)
        self.__area_asignada = area_asignada

    def gestionar_uso(self):
        return (f"MANTENIMIENTO [{self.get_nombre()}]: Entregar en zona "
                f"'{self.__area_asignada}'. Stock: {self.get_cantidad()}.")


class Medicina(ItemInventario):
    def __init__(self, codigo, nombre, cantidad, requiere_refrigeracion):
        super().__init__(codigo, nombre, cantidad)
        self.__requiere_refrigeracion = requiere_refrigeracion

    def gestionar_uso(self):
        r = "EN NEVERA" if self.__requiere_refrigeracion else "A TEMPERATURA AMBIENTE"
        return (f"VETERINARIA [{self.get_nombre()}]: Almacenar {r}. "
                f"Unidades: {self.get_cantidad()}.")
