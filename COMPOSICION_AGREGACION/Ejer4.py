class Ropa:
    def __init__(self, tipo, material):
        self.tipo = tipo
        self.material = material
    
    def __str__(self):
        return f"Ropa: {self.tipo} - Material: {self.material}"
    
    def __repr__(self):
        return f"Ropa('{self.tipo}', '{self.material}')"

class Ropero:
    def __init__(self, material_ropero):
        self.material = material_ropero
        self.ropa = [None] * 20
        self.nro_ropas = 0
    
    def adicionar_prenda(self, tipo, material):
        if self.nro_ropas >= 20:
            print("El ropero está lleno. No se puede agregar más prendas.")
            return False
        
        nueva_prenda = Ropa(tipo, material)
        self.ropa[self.nro_ropas] = nueva_prenda
        self.nro_ropas += 1
        print(f"Prenda agregada: {tipo} de {material}")
        return True
    
    def adicionar_n_prendas(self, n):
        if n <= 0:
            print("El número de prendas debe ser mayor a 0")
            return
        
        print(f"\nAdicionando {n} prendas al ropero:")
        prendas_agregadas = 0
        
        for i in range(n):
            if self.nro_ropas >= 20:
                print(f"Solo se pudieron agregar {prendas_agregadas} prendas. Ropero lleno.")
                break
            
            print(f"Prenda {i+1}:")
            tipo = input("Ingrese el tipo de prenda: ")
            material = input("Ingrese el material: ")
            
            if self.adicionar_prenda(tipo, material):
                prendas_agregadas += 1
        
        print(f"Se agregaron {prendas_agregadas} prendas correctamente.")
    
    def eliminar_prendas_material_tipo(self, material_x=None, tipo_y=None):
        if material_x is None and tipo_y is None:
            print("Debe especificar al menos material o tipo para eliminar")
            return 0
        
        prendas_eliminadas = 0
        i = 0
        
        while i < self.nro_ropas:
            prenda = self.ropa[i]
            eliminar = False
            
            if material_x and prenda.material.lower() == material_x.lower():
                eliminar = True
            if tipo_y and prenda.tipo.lower() == tipo_y.lower():
                eliminar = True
            
            if eliminar:
                print(f"Eliminando: {prenda}")
                for j in range(i, self.nro_ropas - 1):
                    self.ropa[j] = self.ropa[j + 1]
                self.ropa[self.nro_ropas - 1] = None
                self.nro_ropas -= 1
                prendas_eliminadas += 1
            else:
                i += 1
        
        print(f"Se eliminaron {prendas_eliminadas} prendas")
        return prendas_eliminadas
    
    def mostrar_prendas_material_tipo(self, material_x=None, tipo_y=None):
        if material_x is None and tipo_y is None:
            print("Debe especificar al menos material o tipo para mostrar")
            return
        
        print(f"\nPrendas con material '{material_x}' o tipo '{tipo_y}':")
        encontradas = False
        
        for i in range(self.nro_ropas):
            prenda = self.ropa[i]
            mostrar = False
            
            if material_x and prenda.material.lower() == material_x.lower():
                mostrar = True
            if tipo_y and prenda.tipo.lower() == tipo_y.lower():
                mostrar = True
            
            if mostrar:
                print(f"  - {prenda}")
                encontradas = True
        
        if not encontradas:
            print("No se encontraron prendas con los criterios especificados")
    
    def mostrar_todas_prendas(self):
        print(f"\nTodas las prendas en el ropero ({self.nro_ropas} prendas):")
        if self.nro_ropas == 0:
            print("El ropero está vacío")
            return
        
        for i in range(self.nro_ropas):
            print(f"  {i+1}. {self.ropa[i]}")
    
    def __str__(self):
        return f"Ropero de {self.material} con {self.nro_ropas} prendas"

def mostrar_menu():
    print("\n" + "="*50)
    print("          SISTEMA DE GESTIÓN DE ROPERO")
    print("="*50)
    print("1. Adicionar N prendas al ropero")
    print("2. Eliminar prendas por material o tipo")
    print("3. Mostrar prendas por material o tipo")
    print("4. Mostrar todas las prendas")
    print("5. Información del ropero")
    print("6. Salir")
    print("="*50)

def main():
    print("Creando ropero...")
    material_ropero = input("Ingrese el material del ropero: ")
    ropero = Ropero(material_ropero)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            try:
                n = int(input("Ingrese el número de prendas a agregar: "))
                ropero.adicionar_n_prendas(n)
            except ValueError:
                print("Error: Debe ingresar un número válido")
        
        elif opcion == "2":
            print("Eliminar prendas por:")
            material_x = input("Material (dejar vacío para omitir): ").strip()
            tipo_y = input("Tipo (dejar vacío para omitir): ").strip()
            
            if not material_x and not tipo_y:
                print("Debe especificar al menos un criterio")
                continue
            
            material_x = material_x if material_x else None
            tipo_y = tipo_y if tipo_y else None
            ropero.eliminar_prendas_material_tipo(material_x, tipo_y)
        
        elif opcion == "3":
            print("Mostrar prendas por:")
            material_x = input("Material (dejar vacío para omitir): ").strip()
            tipo_y = input("Tipo (dejar vacío para omitir): ").strip()
            
            if not material_x and not tipo_y:
                print("Debe especificar al menos un criterio")
                continue
            
            material_x = material_x if material_x else None
            tipo_y = tipo_y if tipo_y else None
            ropero.mostrar_prendas_material_tipo(material_x, tipo_y)
        
        elif opcion == "4":
            ropero.mostrar_todas_prendas()
        
        elif opcion == "5":
            print(ropero)
        
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione 1-6")

if __name__ == "__main__":
    main()