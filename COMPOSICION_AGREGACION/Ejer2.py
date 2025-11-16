class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.nombre = nombre
        self.cargo = cargo
        self.sueldo = sueldo

    def __str__(self):
        return f"{self.nombre}, {self.cargo}, sueldo: {self.sueldo}"


class Departamento:
    def __init__(self, nombre, area):
        self.nombre = nombre
        self.area = area
        self.empleados = []

    def agregar(self, emp):
        self.empleados.append(emp)

    def mostrarEmpleados(self):
        print(f"Departamento: {self.nombre} ({self.area})")
        if len(self.empleados) == 0:
            print("  No tiene empleados.")
        else:
            for e in self.empleados:
                print("  -", e)

    def cambioSalario(self, nuevo):
        for e in self.empleados:
            e.sueldo = nuevo

    def moverA(self, otroDep):
        for e in self.empleados:
            otroDep.agregar(e)
        self.empleados.clear()


d1 = Departamento("Sistemas", "Tecnologia")
d2 = Departamento("Marketing", "Ventas")

d1.agregar(Empleado("Ana", "Analista", 4500))
d1.agregar(Empleado("Luis", "Programador", 5000))
d1.agregar(Empleado("Maria", "Soporte", 4000))
d1.agregar(Empleado("Carlos", "Tester", 4200))
d1.agregar(Empleado("Andrea", "QA", 4300))

print("Estado inicial:")
d1.mostrarEmpleados()
d2.mostrarEmpleados()

d1.cambioSalario(6000)

repetido = any(e in d2.empleados for e in d1.empleados)
print("\n¿Algún empleado de d1 está en d2?:", "Sí" if repetido else "No")

d1.moverA(d2)

print("\nEstado final:")
d1.mostrarEmpleados()
d2.mostrarEmpleados()
