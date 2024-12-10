#TAREA SEMANA 3 - POO
#Clase que representa la información de un día específico del clima
class ClimaDiario:
    def __init__(self, dia, temperatura=None):
        self.dia = dia
        self._temperatura = temperatura 

    #Crea una clase que represente la información diaria del clima
    def ingresar_temperatura(self):
        while True:
            try:
                self._temperatura = float(input(f"Ingrese la temperatura del día {self.dia}: "))
                break  #Salir si la entrada es válida
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")

    #Método para obtener la temperatura del día
    def obtener_temperatura(self):
        return self._temperatura


#Utiliza métodos de la clase para ingresar datos y calcular el promedio semanal
class SemanaClima:
    def __init__(self):
        self.dias = []  #Lista que almacenará los objetos ClimaDiario

    #Método para ingresar las temperaturas de la semana
    def ingresar_temperaturas(self):
        for dia in range(1, 7):  #7 días en una semana
            clima = ClimaDiario(dia)  #Crear un objeto ClimaDiario para cada día
            clima.ingresar_temperatura() # Ingresar la temperatura del día
            self.dias.append(clima)  

    #Método para calcular el promedio de las temperaturas de la semana
    def calcular_promedio(self):
        total = sum(clima.obtener_temperatura() for clima in self.dias)
        return total / len(self.dias)

    #Método para mostrar el promedio semanal
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f}°C")


#Función principal que organiza el flujo del programa
def main():
    print("Programa para calcular el promedio semanal del clima")
    semana = SemanaClima()  #Crear un objeto de la clase SemanaClima
    semana.ingresar_temperaturas()  #Ingresar las temperaturas para la semana
    semana.mostrar_promedio()  #Mostrar el promedio de la semana


#Ejecucion del programa
if __name__ == "__main__":
    main()
