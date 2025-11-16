class NumeroInvalidoException(Exception):
    """Excepción personalizada para números inválidos"""
    def __init__(self, valor, mensaje="No es un número válido"):
        self.valor = valor
        self.mensaje = mensaje
        super().__init__(f"{mensaje}: '{valor}'")

class ArithmeticException(Exception):
    """Excepción personalizada para errores aritméticos"""
    def __init__(self, mensaje="Error aritmético"):
        self.mensaje = mensaje
        super().__init__(mensaje)

# CLASE CALCULADORA

class Calculadora:
    
    @staticmethod
    def sumar(a, b):
        """Suma dos números"""
        return a + b
    
    @staticmethod
    def restar(a, b):
        """Resta dos números"""
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        """Multiplica dos números"""
        return a * b
    
    @staticmethod
    def dividir(a, b):
        """
        Divide dos números
        Lanza ArithmeticException si el divisor es cero
        """
        if b == 0:
            raise ArithmeticException("No se puede dividir entre cero")
        return a / b
    
    @staticmethod
    def convertir_a_entero(cadena):
        """
        Convierte un String a número entero
        Lanza NumeroInvalidoException si el valor no es numérico
        """
        try:
            # Intentar convertir a entero
            return int(cadena)
        except ValueError:
            # Lanzar nuestra excepción personalizada
            raise NumeroInvalidoException(cadena, "El valor no puede convertirse a número entero")
    
    @staticmethod
    def convertir_a_float(cadena):
        """
        Convierte un String a número float
        Lanza NumeroInvalidoException si el valor no es numérico
        """
        try:
            # Intentar convertir a float
            return float(cadena)
        except ValueError:
            # Lanzar nuestra excepción personalizada
            raise NumeroInvalidoException(cadena, "El valor no puede convertirse a número decimal")

# PROGRAMA PRINCIPAL

def probar_operaciones_basicas():
    """Prueba las operaciones básicas de la calculadora"""
    print("=" * 60)
    print("PRUEBA DE OPERACIONES BÁSICAS")
    print("=" * 60)
    
    # Casos de prueba normales
    test_cases = [
        (10, 5),
        (15, 3),
        (8, 2),
        (100, 25)
    ]
    
    for a, b in test_cases:
        print(f"\nOperaciones con {a} y {b}:")
        print(f"  {a} + {b} = {Calculadora.sumar(a, b)}")
        print(f"  {a} - {b} = {Calculadora.restar(a, b)}")
        print(f"  {a} * {b} = {Calculadora.multiplicar(a, b)}")
        print(f"  {a} / {b} = {Calculadora.dividir(a, b)}")

def probar_division_por_cero():
    """Prueba el manejo de división por cero"""
    print("\n" + "=" * 60)
    print("PRUEBA DE DIVISIÓN POR CERO")
    print("=" * 60)
    
    casos = [
        (10, 0),
        (0, 0),
        (-5, 0),
        (100, 0)
    ]
    
    for a, b in casos:
        try:
            print(f"\nIntentando dividir {a} / {b}:")
            resultado = Calculadora.dividir(a, b)
            print(f"  Resultado: {resultado}")
        except ArithmeticException as e:
            print(f"  ❌ Error aritmético: {e}")
        except Exception as e:
            print(f"  ❌ Error inesperado: {e}")

def probar_conversion_numeros():
    """Prueba la conversión de String a números"""
    print("\n" + "=" * 60)
    print("PRUEBA DE CONVERSIÓN DE STRING A NÚMEROS")
    print("=" * 60)
    
    # Casos válidos e inválidos
    test_cases = [
        "123",           # válido
        "45.67",         # válido para float
        "-89",           # válido
        "3.1416",        # válido para float
        "abc",           # inválido
        "123abc",        # inválido
        "45.67.89",      # inválido
        "",              # inválido
        "  123  ",       # inválido (espacios)
        "1,234",         # inválido (coma)
    ]
    
    for caso in test_cases:
        print(f"\nConvirtiendo: '{caso}'")
        
        # Probar conversión a entero
        try:
            entero = Calculadora.convertir_a_entero(caso)
            print(f"  ✅ Entero: {entero}")
        except NumeroInvalidoException as e:
            print(f"  ❌ Error en conversión a entero: {e}")
        except Exception as e:
            print(f"  ❌ Error inesperado: {e}")
        
        # Probar conversión a float
        try:
            decimal = Calculadora.convertir_a_float(caso)
            print(f"  ✅ Float: {decimal}")
        except NumeroInvalidoException as e:
            print(f"  ❌ Error en conversión a float: {e}")
        except Exception as e:
            print(f"  ❌ Error inesperado: {e}")

def probar_calculadora_completa():
    """Prueba completa de la calculadora con entrada del usuario"""
    print("\n" + "=" * 60)
    print("CALCULADORA INTERACTIVA")
    print("=" * 60)
    
    while True:
        print("\nOperaciones disponibles:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "5":
            print("¡Hasta luego!")
            break
        
        if opcion not in ["1", "2", "3", "4"]:
            print("❌ Opción no válida. Por favor seleccione 1-5.")
            continue
        
        try:
            # Obtener los números del usuario
            num1_str = input("Ingrese el primer número: ")
            num2_str = input("Ingrese el segundo número: ")
            
            # Convertir a float
            num1 = Calculadora.convertir_a_float(num1_str)
            num2 = Calculadora.convertir_a_float(num2_str)
            
            # Realizar la operación seleccionada
            if opcion == "1":
                resultado = Calculadora.sumar(num1, num2)
                operacion = "+"
            elif opcion == "2":
                resultado = Calculadora.restar(num1, num2)
                operacion = "-"
            elif opcion == "3":
                resultado = Calculadora.multiplicar(num1, num2)
                operacion = "*"
            elif opcion == "4":
                resultado = Calculadora.dividir(num1, num2)
                operacion = "/"
            
            print(f"\n✅ Resultado: {num1} {operacion} {num2} = {resultado}")
            
        except NumeroInvalidoException as e:
            print(f"❌ Error en los números ingresados: {e}")
        except ArithmeticException as e:
            print(f"❌ Error aritmético: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

def demostrar_manejo_excepciones():
    """Demuestra el manejo de diferentes tipos de excepciones"""
    print("\n" + "=" * 60)
    print("DEMOSTRACIÓN DE MANEJO DE EXCEPCIONES")
    print("=" * 60)
    
    # Casos de prueba específicos
    casos_demostracion = [
        # (descripcion, funcion, *args)
        ("División normal", Calculadora.dividir, 10, 2),
        ("División por cero", Calculadora.dividir, 10, 0),
        ("Conversión válida", Calculadora.convertir_a_entero, "123"),
        ("Conversión inválida", Calculadora.convertir_a_entero, "abc"),
        ("Suma con números grandes", Calculadora.sumar, 1000000, 500000),
        ("Multiplicación con negativos", Calculadora.multiplicar, -5, 8),
    ]
    
    for descripcion, funcion, *args in casos_demostracion:
        print(f"\n{descripcion}:")
        print(f"  Función: {funcion.__name__}")
        print(f"  Argumentos: {args}")
        
        try:
            resultado = funcion(*args)
            print(f"  ✅ Éxito: {resultado}")
        except NumeroInvalidoException as e:
            print(f"  ❌ NumeroInvalidoException: {e}")
        except ArithmeticException as e:
            print(f"  ❌ ArithmeticException: {e}")
        except Exception as e:
            print(f"  ❌ Exception inesperada: {type(e).__name__}: {e}")

def main():
    """Función principal que ejecuta todas las pruebas"""
    print("CALCULADORA CON MANEJO DE EXCEPCIONES")
    print("=" * 60)
    
    try:
        # Ejecutar todas las pruebas
        probar_operaciones_basicas()
        probar_division_por_cero()
        probar_conversion_numeros()
        demostrar_manejo_excepciones()
        
        # Opcional: Ejecutar calculadora interactiva
        ejecutar_interactiva = input("\n¿Desea probar la calculadora interactiva? (s/n): ")
        if ejecutar_interactiva.lower() == 's':
            probar_calculadora_completa()
            
    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario")
    except Exception as e:
        print(f"\nError inesperado en el programa principal: {e}")

# EJECUCIÓN DEL PROGRAMA


if __name__ == "__main__":
    main()