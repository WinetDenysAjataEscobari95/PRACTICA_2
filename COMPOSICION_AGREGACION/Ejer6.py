class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        return f"{self.nombre} (Bs. {self.precio})"


class Medicamento(Producto):
    def __init__(self, id, nombre, precio, dosis, vencimiento):
        super().__init__(id, nombre, precio)
        self.dosis = dosis
        self.vencimiento = vencimiento


class Suplemento(Producto):
    def __init__(self, id, nombre, precio, tipo, presentacion):
        super().__init__(id, nombre, precio)
        self.tipo = tipo
        self.presentacion = presentacion


class Detalle:
    # Un detalle siempre pertenece a un medicamento (composición)
    def __init__(self, medicamento, cantidad):
        self.medicamento = medicamento
        self.cantidad = cantidad
        self.subtotal = medicamento.precio * cantidad


class Registro:
    def __init__(self, fecha):
        self.fecha = fecha
        self.detalles = []
        self.total = 0

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)
        self.total += detalle.subtotal

    def mostrar(self):
        print(f"Fecha: {self.fecha}")
        for d in self.detalles:
            print(f"- {d.medicamento.nombre} x{d.cantidad} = {d.subtotal}")
        print("Total:", self.total)


# -------- EJEMPLO DE USO --------
if __name__ == "__main__":
    med1 = Medicamento(1, "Paracetamol", 5.0, "500mg", "12/2026")
    sup1 = Suplemento(2, "Vitamina C", 10.0, "Inmunidad", "Tabletas")

    reg = Registro("15/11/2025")
    reg.agregar_detalle(Detalle(med1, 3))
    reg.agregar_detalle(Detalle(sup1, 1))

    reg.mostrar()
