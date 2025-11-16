class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.hospitales = []  # Lista de hospitales donde trabaja
    
    def __str__(self):
        return f"Dr. {self.nombre} - Especialidad: {self.especialidad}"
    
    def __repr__(self):
        return f"Doctor('{self.nombre}', '{self.especialidad}')"
    
    def agregar_hospital(self, hospital):
        """Agrega un hospital a la lista donde trabaja el doctor"""
        if hospital not in self.hospitales:
            self.hospitales.append(hospital)
            print(f"El Dr. {self.nombre} ahora trabaja en el {hospital.nombre}")
    
    def mostrar_hospitales(self):
        """Muestra los hospitales donde trabaja el doctor"""
        if not self.hospitales:
            print(f"El Dr. {self.nombre} no trabaja en ningún hospital actualmente")
            return
        
        print(f"\nHospitales donde trabaja el Dr. {self.nombre}:")
        for i, hospital in enumerate(self.hospitales, 1):
            print(f"  {i}. {hospital.nombre}")

class Hospital:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.doctores = []  # Lista de doctores que trabajan en el hospital
    
    def __str__(self):
        return f"Hospital: {self.nombre} - Dirección: {self.direccion}"
    
    def __repr__(self):
        return f"Hospital('{self.nombre}', '{self.direccion}')"
    
    def asignar_doctor(self, doctor):
        """Asigna un doctor al hospital (relación de agregación)"""
        if doctor in self.doctores:
            print(f"El Dr. {doctor.nombre} ya trabaja en este hospital")
            return False
        
        self.doctores.append(doctor)
        doctor.agregar_hospital(self)  # También actualizamos la lista del doctor
        print(f"Dr. {doctor.nombre} asignado al {self.nombre}")
        return True
    
    def mostrar_doctores(self):
        """Muestra todos los doctores que trabajan en el hospital"""
        print(f"\n{'='*60}")
        print(f"DOCTORES DEL {self.nombre.upper()}")
        print(f"{'='*60}")
        
        if not self.doctores:
            print("No hay doctores asignados a este hospital")
            return
        
        # Agrupar doctores por especialidad
        especialidades = {}
        for doctor in self.doctores:
            if doctor.especialidad not in especialidades:
                especialidades[doctor.especialidad] = []
            especialidades[doctor.especialidad].append(doctor)
        
        # Mostrar por especialidad
        for especialidad, doctores_esp in especialidades.items():
            print(f"\n{especialidad.upper()}:")
            for i, doctor in enumerate(doctores_esp, 1):
                print(f"  {i}. Dr. {doctor.nombre}")
    
    def contar_doctores_por_especialidad(self):
        """Cuenta cuántos doctores hay por cada especialidad"""
        conteo = {}
        for doctor in self.doctores:
            if doctor.especialidad in conteo:
                conteo[doctor.especialidad] += 1
            else:
                conteo[doctor.especialidad] = 1
        
        print(f"\nDistribución de especialidades en {self.nombre}:")
        for especialidad, cantidad in conteo.items():
            print(f"  {especialidad}: {cantidad} doctor(es)")
        
        return conteo
    
    def buscar_doctores_por_especialidad(self, especialidad):
        """Busca doctores por especialidad"""
        doctores_especialidad = [doc for doc in self.doctores if doc.especialidad.lower() == especialidad.lower()]
        
        if not doctores_especialidad:
            print(f"No hay doctores de {especialidad} en este hospital")
            return []
        
        print(f"\nDoctores de {especialidad} en {self.nombre}:")
        for i, doctor in enumerate(doctores_especialidad, 1):
            print(f"  {i}. {doctor}")
        
        return doctores_especialidad

class SistemaHospitales:
    def __init__(self):
        self.hospitales = []
        self.doctores = []
    
    def agregar_hospital(self, hospital):
        """Agrega un hospital al sistema"""
        self.hospitales.append(hospital)
        print(f"Hospital agregado: {hospital.nombre}")
    
    def agregar_doctor(self, doctor):
        """Agrega un doctor al sistema"""
        self.doctores.append(doctor)
        print(f"Doctor agregado: Dr. {doctor.nombre}")
    
    def asignar_doctor_a_hospital(self, doctor, hospital):
        """Asigna un doctor a un hospital"""
        if hospital not in self.hospitales:
            print(f"Error: El hospital {hospital.nombre} no está registrado en el sistema")
            return False
        
        if doctor not in self.doctores:
            print(f"Error: El Dr. {doctor.nombre} no está registrado en el sistema")
            return False
        
        return hospital.asignar_doctor(doctor)
    
    def mostrar_todos_hospitales(self):
        """Muestra todos los hospitales del sistema"""
        print(f"\n{'='*80}")
        print("SISTEMA DE HOSPITALES - LISTA COMPLETA")
        print(f"{'='*80}")
        
        if not self.hospitales:
            print("No hay hospitales registrados en el sistema")
            return
        
        for i, hospital in enumerate(self.hospitales, 1):
            print(f"\n{i}. {hospital}")
            print(f"   Doctores asignados: {len(hospital.doctores)}")
    
    def mostrar_todos_doctores(self):
        """Muestra todos los doctores del sistema"""
        print(f"\n{'='*80}")
        print("SISTEMA DE HOSPITALES - LISTA DE DOCTORES")
        print(f"{'='*80}")
        
        if not self.doctores:
            print("No hay doctores registrados en el sistema")
            return
        
        for i, doctor in enumerate(self.doctores, 1):
            print(f"{i}. {doctor}")
            print(f"   Trabaja en {len(doctor.hospitales)} hospital(es)")
    
    def doctores_que_trabajan_en_varios_hospitales(self):
        """Muestra doctores que trabajan en más de un hospital"""
        print(f"\n{'='*60}")
        print("DOCTORES QUE TRABAJAN EN MÚLTIPLES HOSPITALES")
        print(f"{'='*60}")
        
        multi_hospital = [doc for doc in self.doctores if len(doc.hospitales) > 1]
        
        if not multi_hospital:
            print("No hay doctores que trabajen en múltiples hospitales")
            return
        
        for doctor in multi_hospital:
            print(f"\nDr. {doctor.nombre} - {doctor.especialidad}")
            print(f"  Hospitales: {', '.join([h.nombre for h in doctor.hospitales])}")

def main():
    # Crear el sistema
    sistema = SistemaHospitales()
    
    print("INICIALIZANDO SISTEMA DE HOSPITALES Y DOCTORES")
    print("=" * 50)
    
    # Crear hospitales
    hospital1 = Hospital("Hospital General", "Av. Principal 123")
    hospital2 = Hospital("Clínica Central", "Calle Central 456")
    hospital3 = Hospital("Hospital Infantil", "Av. Niños 789")
    
    # Agregar hospitales al sistema
    sistema.agregar_hospital(hospital1)
    sistema.agregar_hospital(hospital2)
    sistema.agregar_hospital(hospital3)
    
    # Crear doctores
    doctor1 = Doctor("Carlos Mendoza", "Cardiología")
    doctor2 = Doctor("Ana López", "Pediatría")
    doctor3 = Doctor("Miguel Torres", "Cirugía")
    doctor4 = Doctor("Laura García", "Cardiología")
    doctor5 = Doctor("Roberto Díaz", "Pediatría")
    doctor6 = Doctor("Sofia Castro", "Neurología")
    
    # Agregar doctores al sistema
    sistema.agregar_doctor(doctor1)
    sistema.agregar_doctor(doctor2)
    sistema.agregar_doctor(doctor3)
    sistema.agregar_doctor(doctor4)
    sistema.agregar_doctor(doctor5)
    sistema.agregar_doctor(doctor6)
    
    print("\n" + "="*50)
    print("ASIGNANDO DOCTORES A HOSPITALES")
    print("="*50)
    
    
    # Hospital General
    sistema.asignar_doctor_a_hospital(doctor1, hospital1)  # Cardiología
    sistema.asignar_doctor_a_hospital(doctor3, hospital1)  # Cirugía
    sistema.asignar_doctor_a_hospital(doctor6, hospital1)  # Neurología
    
    # Clínica Central
    sistema.asignar_doctor_a_hospital(doctor2, hospital2)  # Pediatría
    sistema.asignar_doctor_a_hospital(doctor4, hospital2)  # Cardiología
    sistema.asignar_doctor_a_hospital(doctor6, hospital2)  # Neurología (mismo doctor en 2 hospitales)
    
    # Hospital Infantil
    sistema.asignar_doctor_a_hospital(doctor2, hospital3)  # Pediatría (mismo doctor en 2 hospitales)
    sistema.asignar_doctor_a_hospital(doctor5, hospital3)  # Pediatría
    
    print("\n" + "="*80)
    print("INFORME COMPLETO DEL SISTEMA")
    print("="*80)
    
    # Mostrar doctores de cada hospital
    hospital1.mostrar_doctores()
    hospital2.mostrar_doctores()
    hospital3.mostrar_doctores()
    
    # Mostrar distribución por especialidad
    print("\n" + "="*50)
    print("ESTADÍSTICAS POR ESPECIALIDAD")
    print("="*50)
    hospital1.contar_doctores_por_especialidad()
    hospital2.contar_doctores_por_especialidad()
    hospital3.contar_doctores_por_especialidad()
    
    # Mostrar doctores que trabajan en múltiples hospitales
    sistema.doctores_que_trabajan_en_varios_hospitales()
    
    # Mostrar información completa del sistema
    sistema.mostrar_todos_hospitales()
    sistema.mostrar_todos_doctores()
    
    # Demostrar búsqueda por especialidad
    print("\n" + "="*50)
    print("BÚSQUEDA DE DOCTORES POR ESPECIALIDAD")
    print("="*50)
    hospital1.buscar_doctores_por_especialidad("Cardiología")
    hospital2.buscar_doctores_por_especialidad("Neurología")
    
    # Mostrar hospitales donde trabaja un doctor específico
    print("\n" + "="*50)
    print("INFORMACIÓN DE DOCTORES ESPECÍFICOS")
    print("="*50)
    doctor2.mostrar_hospitales()  # Doctor que trabaja en 2 hospitales
    doctor6.mostrar_hospitales()  # Doctor que trabaja en 2 hospitales

if __name__ == "__main__":
    main()