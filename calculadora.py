class Calculadora:

    def __init__(self, tipo_operacion, resultado, fecha_uso):
        self.tipo_operacion= tipo_operacion
        self.resultado= resultado
        self.fecha_uso= fecha_uso

    def get_fecha(self):
        return self.fecha_uso
    
    def set_fecha(self, nueva_fecha):
      self.nueva_fecha = nueva_fecha
       
    def calcular_suma(self, obj_num1, obj_num2):
        result_suma = obj_num1.get_num() + obj_num2.get_num()
        print(f"el resultado de la suma es: {result_suma}")
        return result_suma
    
    def calcular_resta(self, obj_num1, obj_num2):
        print(f"el resultado de la resta es: {result_resta}")
        result_resta = obj_num1.get_num() - obj_num2.get_num()
        return result_resta
    
    def calcular_multiplicacion(self, obj_num1, obj_num2):
        print(f"el resultado de la multiplicacion es {result_multiplicacion}")
        result_multiplicacion = obj_num1.get_num() * obj_num2.get_num()
        return result_multiplicacion
    
    def calcular_division(self, obj_num1, obj_num2):
        print(f"el resultado de la division es {result_division}")
        result_division = obj_num1.get_num() / obj_num2.get_num()
        return result_division
    
    def realizar_operacion(self, numero_1, numero_2, operacion):
        if self.tipo_operacion == "suma":
            dato = self.calcular_suma(numero_1, numero_2)
            return dato
        elif self.tipo_operacion == "resta":
            dato = self.calcular_resta(numero_1, numero_2)
            return dato
        elif self.tipo_operacion == "mulñtiplicacion" or self.tipo_operacion == "multiplicacion":
            dato = self.calcular_multiplicacion(numero_1, numero_2)
            return dato
        elif self.tipo_operacion == "division":
            dato = self.calcular_division(numero_1, numero_2)
            return dato
        else:
            pass

        def mostrar_resultado(self):
            print(f"El resultado de la suma es: {self.resultado_suma}")
            print(f"El resultado de la resta es: {self.resultado_resta}")
            print(f"El resultadom de la multiplicacion es: {self.resultado_multiplicacion}")
            print(f"El resultado de la division es: {self.resultado_division}")
            