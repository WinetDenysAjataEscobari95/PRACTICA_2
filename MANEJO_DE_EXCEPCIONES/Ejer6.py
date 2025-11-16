class LibroNoDisponibleException(Exception):
    pass

class LibroNoEncontradoException(Exception):
    pass

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True
    
    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' - {self.autor} [{estado}]"

class Biblioteca:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro agregado: {libro.titulo}")
    
    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None
    
    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        
        if not libro:
            raise LibroNoEncontradoException(f"El libro '{titulo}' no existe en la biblioteca")
        
        if not libro.disponible:
            raise LibroNoDisponibleException(f"El libro '{titulo}' ya está prestado")
        
        libro.disponible = False
        print(f"Libro prestado: {titulo}")
        return True
    
    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        
        if not libro:
            raise LibroNoEncontradoException(f"El libro '{titulo}' no existe en la biblioteca")
        
        libro.disponible = True
        print(f"Libro devuelto: {titulo}")
        return True
    
    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca no tiene libros")
            return
        
        print("\n--- CATÁLOGO DE LIBROS ---")
        for i, libro in enumerate(self.libros, 1):
            print(f"{i}. {libro}")

def main_biblioteca():
    biblioteca = Biblioteca()
    
    libros_iniciales = [
        Libro("Cien años de soledad", "Gabriel García Márquez"),
        Libro("1984", "George Orwell"),
        Libro("El Quijote", "Miguel de Cervantes"),
        Libro("Rayuela", "Julio Cortázar")
    ]
    
    for libro in libros_iniciales:
        biblioteca.agregar_libro(libro)
    
    print("\n=== PRUEBAS DE PRÉSTAMO DE LIBROS ===")
    
    biblioteca.mostrar_libros()
    
    print("\n1. Préstamo exitoso:")
    try:
        biblioteca.prestar_libro("1984")
    except (LibroNoDisponibleException, LibroNoEncontradoException) as e:
        print(f"Error: {e}")
    
    print("\n2. Intentar prestar libro ya prestado:")
    try:
        biblioteca.prestar_libro("1984")
    except LibroNoDisponibleException as e:
        print(f"Error esperado: {e}")
    
    print("\n3. Intentar prestar libro inexistente:")
    try:
        biblioteca.prestar_libro("Harry Potter")
    except LibroNoEncontradoException as e:
        print(f"Error esperado: {e}")
    
    print("\n4. Devolución exitosa:")
    try:
        biblioteca.devolver_libro("1984")
    except LibroNoEncontradoException as e:
        print(f"Error: {e}")
    
    print("\n5. Intentar devolver libro inexistente:")
    try:
        biblioteca.devolver_libro("Don Quijote")
    except LibroNoEncontradoException as e:
        print(f"Error esperado: {e}")
    
    print("\n6. Préstamo después de devolución:")
    try:
        biblioteca.prestar_libro("1984")
        print("Préstamo exitoso después de devolución")
    except (LibroNoDisponibleException, LibroNoEncontradoException) as e:
        print(f"Error: {e}")
    
    print("\n--- ESTADO FINAL DE LA BIBLIOTECA ---")
    biblioteca.mostrar_libros()

class FondosInsuficientesException(Exception):
    pass

class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, saldo_inicial=0):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, monto):
        if monto <= 0:
            raise ValueError(f"Monto de depósito debe ser positivo: {monto}")
        
        self.saldo += monto
        print(f"Depositados Bs. {monto:.2f}. Nuevo saldo: Bs. {self.saldo:.2f}")
    
    def retirar(self, monto):
        if monto <= 0:
            raise ValueError(f"Monto de retiro debe ser positivo: {monto}")
        
        if monto > self.saldo:
            raise FondosInsuficientesException(
                f"Fondos insuficientes. Saldo: Bs. {self.saldo:.2f}, Retiro: Bs. {monto:.2f}"
            )
        
        self.saldo -= monto
        print(f"Retirados Bs. {monto:.2f}. Nuevo saldo: Bs. {self.saldo:.2f}")
    
    def mostrar_info(self):
        print(f"Cuenta: {self.numero_cuenta}")
        print(f"Titular: {self.titular}")
        print(f"Saldo: Bs. {self.saldo:.2f}")

def main_cuenta_bancaria():
    print("\n" + "="*50)
    print("SISTEMA BANCARIO")
    print("="*50)
    
    cuenta = CuentaBancaria("12345", "Juan Pérez", 1000.0)
    
    print("Cuenta creada:")
    cuenta.mostrar_info()
    
    print("\n=== PRUEBAS DE OPERACIONES BANCARIAS ===")
    
    print("\n1. Depósito válido:")
    try:
        cuenta.depositar(500.0)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n2. Depósito con monto negativo:")
    try:
        cuenta.depositar(-100.0)
    except ValueError as e:
        print(f"Error esperado: {e}")
    
    print("\n3. Retiro válido:")
    try:
        cuenta.retirar(300.0)
    except (FondosInsuficientesException, ValueError) as e:
        print(f"Error: {e}")
    
    print("\n4. Retiro que supera el saldo:")
    try:
        cuenta.retirar(2000.0)
    except FondosInsuficientesException as e:
        print(f"Error esperado: {e}")
    
    print("\n5. Retiro con monto negativo:")
    try:
        cuenta.retirar(-50.0)
    except ValueError as e:
        print(f"Error esperado: {e}")
    
    print("\n6. Múltiples operaciones:")
    try:
        cuenta.depositar(1000.0)
        cuenta.retirar(500.0)
        cuenta.retirar(800.0)
    except (FondosInsuficientesException, ValueError) as e:
        print(f"Error durante operaciones: {e}")
    
    print("\n--- ESTADO FINAL DE LA CUENTA ---")
    cuenta.mostrar_info()

if __name__ == "__main__":
    print("EJERCICIO 5 - SISTEMA DE BIBLIOTECA")
    main_biblioteca()
    
    print("\n" + "="*60)
    
    print("EJERCICIO 6 - SISTEMA BANCARIO")
    main_cuenta_bancaria()