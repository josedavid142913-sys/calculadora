class User:

    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre_nuevo):
         self.nombre = nombre_nuevo

    def get_cedula(self):
        return self.cedula
    
    def set_cedula(self, cedula_nueva):
        self.cedula = cedula_nueva

    def mostrar_info(self):
        print(f"cedula: {self.cedula}")
        print(f"nombre: {self.nombre}")