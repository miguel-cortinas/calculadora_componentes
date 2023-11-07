from suma import suma
from resta import resta
from multiplicacion import multiplicacion
from division import division

while True:
    print("Seleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = input("Ingrese el número de la operación deseada: ")
    
    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        if opcion == '1':
            print("Resultado: ", suma(num1, num2))
        elif opcion == '2':
            print("Resultado: ", resta(num1, num2))
        elif opcion == '3':
            print("Resultado: ", multiplicacion(num1, num2))
        elif opcion == '4':
            print("Resultado: ", division(num1, num2))
    elif opcion == '5':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese un número del 1 al 5.")
