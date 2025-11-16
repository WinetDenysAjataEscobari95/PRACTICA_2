class ErrorProductoNoEncontrado(Exception):
    def __init__(self, codigo):
        super().__init__(f"No existe producto con codigo {codigo}")
        self.codigo = codigo

class ErrorStockInsuficiente(Exception):
    def __init__(self, codigo, stock_actual, cantidad):
        super().__init__(f"Stock insuficiente. Producto: {codigo}, Stock: {stock_actual}, Se pidio: {cantidad}")
        self.codigo = codigo
        self.stock_actual = stock_actual
        self.cantidad = cantidad

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def mostrar_info(self):
        return f"Codigo: {self.codigo} | {self.nombre} | Precio: Bs. {self.precio} | Stock: {self.stock}"
    
    def reducir_stock(self, cantidad):
        if cantidad > self.stock:
            raise ErrorStockInsuficiente(self.codigo, self.stock, cantidad)
        self.stock -= cantidad

class Inventario:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        for prod in self.productos:
            if prod.codigo == producto.codigo:
                raise ValueError(f"Ya existe producto con codigo {producto.codigo}")
        
        if producto.precio < 0:
            raise ValueError("El precio no puede ser negativo")
        
        if producto.stock < 0:
            raise ValueError("El stock no puede ser negativo")
        
        self.productos.append(producto)
        print(f"Producto {producto.nombre} agregado correctamente")
    
    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        raise ErrorProductoNoEncontrado(codigo)
    
    def vender_producto(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        producto.reducir_stock(cantidad)
        print(f"Vendidas {cantidad} unidades de {producto.nombre}")
        print(f"Stock restante: {producto.stock}")
    
    def listar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario")
            return
        
        print("\n--- LISTA DE PRODUCTOS ---")
        for producto in self.productos:
            print(producto.mostrar_info())
    
    def productos_con_stock_bajo(self, limite=5):
        productos_bajos = [p for p in self.productos if p.stock < limite]
        if productos_bajos:
            print(f"\n--- PRODUCTOS CON STOCK BAJO (menos de {limite}) ---")
            for producto in productos_bajos:
                print(producto.mostrar_info())

def main():
    inventario = Inventario()
    
    p1 = Producto("P001", "Laptop Dell", 10500.00, 10)
    p2 = Producto("P002", "Mouse Logitech", 175.50, 30)
    p3 = Producto("P003", "Teclado Mecanico", 560.00, 3)
    p4 = Producto("P004", "Monitor 24\"", 2100.00, 8)
    
    print("=== SISTEMA DE INVENTARIO ===")
    
    print("\n1. Agregando productos...")
    try:
        inventario.agregar_producto(p1)
        inventario.agregar_producto(p2)
        inventario.agregar_producto(p3)
        inventario.agregar_producto(p4)
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n2. Intentando agregar producto con codigo duplicado...")
    try:
        p5 = Producto("P001", "Tablet Samsung", 2800.00, 5)
        inventario.agregar_producto(p5)
    except ValueError as e:
        print(f"Error esperado: {e}")
    
    print("\n3. Intentando agregar producto con precio negativo...")
    try:
        p6 = Producto("P006", "Producto Invalido", -350.00, 10)
        inventario.agregar_producto(p6)
    except ValueError as e:
        print(f"Error esperado: {e}")
    
    print("\n4. Listado completo de productos:")
    inventario.listar_productos()
    
    print("\n5. Buscando producto existente...")
    try:
        producto = inventario.buscar_producto("P002")
        print(f"Encontrado: {producto.mostrar_info()}")
    except ErrorProductoNoEncontrado as e:
        print(f"Error: {e}")
    
    print("\n6. Buscando producto inexistente...")
    try:
        producto = inventario.buscar_producto("P999")
        print(f"Encontrado: {producto.mostrar_info()}")
    except ErrorProductoNoEncontrado as e:
        print(f"Error esperado: {e}")
    
    print("\n7. Realizando venta exitosa...")
    try:
        inventario.vender_producto("P001", 2)
    except (ErrorProductoNoEncontrado, ErrorStockInsuficiente) as e:
        print(f"Error: {e}")
    
    print("\n8. Intentando venta con stock insuficiente...")
    try:
        inventario.vender_producto("P003", 5)
    except ErrorStockInsuficiente as e:
        print(f"Error esperado: {e}")
    
    print("\n9. Intentando vender producto inexistente...")
    try:
        inventario.vender_producto("P999", 1)
    except ErrorProductoNoEncontrado as e:
        print(f"Error esperado: {e}")
    
    print("\n10. Productos con stock bajo:")
    inventario.productos_con_stock_bajo(5)
    
    print("\n11. Estado final del inventario:")
    inventario.listar_productos()

if __name__ == "__main__":
    main()