#TAREA SEMANA 3 - PROGRAMACION TRADICIONAL
#1 Implementa una solución utilizando estructuras de funciones
def ingresar_temperaturas():
    temperaturas = []
    for dia in range(1, 7):  #Asumiendo los 7 días a la semana
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {dia}: "))
                temperaturas.append(temp)
                break  #Salir del bucle si la entrada es válida
            except ValueError:
                print("Por favor ingrese un valor numérico válido.")
    return temperaturas

#2 Define funciones para la entrada de datos diarios (temperaturas) y el cálculo del promedio semanal
def calcular_promedio(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

#3 Organiza el código de manera lógica y funcional utilizando la programación tradicional
def main():
    print("Programa para calcular el promedio semanal del clima")
    temperaturas = ingresar_temperaturas()  #Ingreso las temperaturas de la semana
    promedio = calcular_promedio(temperaturas)  #Calcular el promedio
    print(f"\nEl promedio semanal de las temperaturas es: {promedio:.2f}°C")

#Ejecucion del programa
if __name__ == "__main__":
    main()

