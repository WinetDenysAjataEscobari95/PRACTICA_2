class Persona:
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
    
    def __str__(self):
        return f"{self.nombre} (CI: {self.cedula}, Edad: {self.edad})"

class Bailarin(Persona):
    def __init__(self, nombre, edad, cedula, facultad, fraternidad):
        super().__init__(nombre, edad, cedula)
        self.facultad = facultad
        self.fraternidad = fraternidad
        self.es_encargado = False
    
    def __str__(self):
        encargado_str = " - ENCARGADO" if self.es_encargado else ""
        return f"{super().__str__()} - Facultad: {self.facultad.nombre} - Fraternidad: {self.fraternidad.nombre}{encargado_str}"

class Facultad:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
    
    def __str__(self):
        return f"{self.nombre} (Código: {self.codigo})"

class Fraternidad:
    def __init__(self, nombre, anio_fundacion):
        self.nombre = nombre
        self.anio_fundacion = anio_fundacion
        self.encargado = None
        self.bailarines = []
    
    def asignar_encargado(self, bailarin):
        if bailarin not in self.bailarines:
            print(f"Error: {bailarin.nombre} no pertenece a esta fraternidad")
            return False
        
        if self.encargado:
            self.encargado.es_encargado = False
        
        bailarin.es_encargado = True
        self.encargado = bailarin
        print(f"Encargado asignado: {bailarin.nombre}")
        return True
    
    def agregar_bailarin(self, bailarin):
        self.bailarines.append(bailarin)
        print(f"Bailarín agregado: {bailarin.nombre}")
    
    def __str__(self):
        encargado_str = f" - Encargado: {self.encargado.nombre}" if self.encargado else " - Sin encargado"
        return f"{self.nombre} (Fundación: {self.anio_fundacion}){encargado_str}"

class SistemaFraternidades:
    def __init__(self):
        self.bailarines = []
        self.fraternidades = []
        self.facultades = []
    
    def registrar_bailarin(self, nombre, edad, cedula, facultad, fraternidad):
        # Verificar que no esté en 2 o más fraternidades
        for bailarin in self.bailarines:
            if bailarin.cedula == cedula:
                print(f"Error: Ya existe un bailarín con cédula {cedula}")
                return None
        
        nuevo_bailarin = Bailarin(nombre, edad, cedula, facultad, fraternidad)
        self.bailarines.append(nuevo_bailarin)
        fraternidad.agregar_bailarin(nuevo_bailarin)
        
        print(f"Bailarín registrado exitosamente: {nombre}")
        return nuevo_bailarin
    
    def mostrar_bailarines(self):
        print("\n" + "="*80)
        print("LISTA COMPLETA DE BAILARINES")
        print("="*80)
        if not self.bailarines:
            print("No hay bailarines registrados")
            return
        
        for i, bailarin in enumerate(self.bailarines, 1):
            print(f"{i}. {bailarin}")
    
    def mostrar_bailarines_por_fraternidad(self, fraternidad):
        print(f"\nBailarines de la fraternidad '{fraternidad.nombre}':")
        bailarines_fraternidad = [b for b in self.bailarines if b.fraternidad == fraternidad]
        
        if not bailarines_fraternidad:
            print("  No hay bailarines en esta fraternidad")
            return
        
        for i, bailarin in enumerate(bailarines_fraternidad, 1):
            print(f"  {i}. {bailarin}")
    
    def mostrar_bailarines_por_facultad(self, facultad):
        print(f"\nBailarines de la facultad '{facultad.nombre}':")
        bailarines_facultad = [b for b in self.bailarines if b.facultad == facultad]
        
        if not bailarines_facultad:
            print("  No hay bailarines en esta facultad")
            return
        
        for i, bailarin in enumerate(bailarines_facultad, 1):
            print(f"  {i}. {bailarin}")
    
    def mostrar_encargados(self):
        print("\nENCARGADOS DE FRATERNIDADES:")
        encargados = [f.encargado for f in self.fraternidades if f.encargado]
        
        if not encargados:
            print("No hay encargados asignados")
            return
        
        for i, encargado in enumerate(encargados, 1):
            print(f"{i}. {encargado} - Fraternidad: {encargado.fraternidad.nombre}")
    
    def mostrar_edades_participantes(self):
        print("\nEDADES DE LOS PARTICIPANTES:")
        if not self.bailarines:
            print("No hay participantes registrados")
            return
        
        edades = [b.edad for b in self.bailarines]
        print(f"Edad mínima: {min(edades)} años")
        print(f"Edad máxima: {max(edades)} años")
        print(f"Promedio de edad: {sum(edades)/len(edades):.1f} años")
        
        print("\nDetalle por participante:")
        for i, bailarin in enumerate(self.bailarines, 1):
            print(f"{i}. {bailarin.nombre}: {bailarin.edad} años")
    
    def verificar_duplicados(self):
        print("\nVERIFICANDO BAILARINES EN MÚLTIPLES FRATERNIDADES...")
        cedulas = {}
        duplicados = False
        
        for bailarin in self.bailarines:
            if bailarin.cedula in cedulas:
                cedulas[bailarin.cedula].append(bailarin)
            else:
                cedulas[bailarin.cedula] = [bailarin]
        
        for cedula, bailarines in cedulas.items():
            if len(bailarines) > 1:
                print(f"¡ALERTA! Cédula {cedula} aparece en {len(bailarines)} fraternidades:")
                for bailarin in bailarines:
                    print(f"  - {bailarin.nombre} en {bailarin.fraternidad.nombre}")
                duplicados = True
        
        if not duplicados:
            print("✓ No se encontraron bailarines en múltiples fraternidades")
        
        return duplicados

def main():
    # Crear el sistema
    sistema = SistemaFraternidades()

    # b) INSTANCIAR 5 PARTICIPANTES, 2 FRATERNIDADES Y 2 FACULTADES
    
    # Crear facultades
    fac_ingenieria = Facultad("Ingeniería", "FING-001")
    fac_medicina = Facultad("Medicina", "FMED-002")
    
    sistema.facultades.extend([fac_ingenieria, fac_medicina])
    
    # Crear fraternidades
    frat_alpha = Fraternidad("Alpha Omega", 2010)
    frat_beta = Fraternidad("Beta Gamma", 2015)
    
    sistema.fraternidades.extend([frat_alpha, frat_beta])
    
    # Registrar 5 bailarines
    print("REGISTRANDO PARTICIPANTES...")
    print("-" * 50)
    
    # Bailarines para fraternidad Alpha
    bailarin1 = sistema.registrar_bailarin("Carlos Rodríguez", 21, "12345678", fac_ingenieria, frat_alpha)
    bailarin2 = sistema.registrar_bailarin("María González", 22, "23456789", fac_medicina, frat_alpha)
    bailarin3 = sistema.registrar_bailarin("Juan Pérez", 20, "34567890", fac_ingenieria, frat_alpha)
    
    # Bailarines para fraternidad Beta
    bailarin4 = sistema.registrar_bailarin("Ana López", 23, "45678901", fac_medicina, frat_beta)
    bailarin5 = sistema.registrar_bailarin("Pedro Sánchez", 19, "56789012", fac_ingenieria, frat_beta)
    
    # Asignar encargados
    print("\nASIGNANDO ENCARGADOS...")
    print("-" * 30)
    frat_alpha.asignar_encargado(bailarin1)
    frat_beta.asignar_encargado(bailarin4)
  
    # c) RESOLVER LO QUE PIDE EL CLIENTE
   
    print("\n" + "="*80)
    print("INFORME COMPLETO DEL SISTEMA")
    print("="*80)
    
    # 1. Ver bailarines y a qué fraternidad y facultad pertenecen
    sistema.mostrar_bailarines()
    
    # 2. Conocer al encargado de cada fraternidad
    sistema.mostrar_encargados()
    
    # 3. Ver las edades de los participantes
    sistema.mostrar_edades_participantes()
    
    # 4. Verificar que no estén en 2 o más fraternidades
    sistema.verificar_duplicados()
    
    # 5. Mostrar información por fraternidad
    print("\n" + "="*50)
    print("INFORMACIÓN POR FRATERNIDAD")
    print("="*50)
    for fraternidad in sistema.fraternidades:
        print(f"\n{fraternidad}")
        sistema.mostrar_bailarines_por_fraternidad(fraternidad)
    
    # 6. Mostrar información por facultad
    print("\n" + "="*50)
    print("INFORMACIÓN POR FACULTAD")
    print("="*50)
    for facultad in sistema.facultades:
        print(f"\n{facultad}")
        sistema.mostrar_bailarines_por_facultad(facultad)
    
    # 7. Demostrar que no se pueden registrar duplicados
    print("\n" + "="*50)
    print("PRUEBA: INTENTAR REGISTRAR DUPLICADO")
    print("="*50)
    sistema.registrar_bailarin("Carlos Duplicado", 25, "12345678", fac_ingenieria, frat_beta)

if __name__ == "__main__":
    main()