class Persona:
    def __init__(self, nombre, apellido, edad, ci):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.ci = ci


class Participante(Persona):
    def __init__(self, nombre, apellido, edad, ci, nroTicket):
        super().__init__(nombre, apellido, edad, ci)
        self.nroTicket = nroTicket


class Speaker(Persona):
    def __init__(self, nombre, apellido, edad, ci, especialidad):
        super().__init__(nombre, apellido, edad, ci)
        self.especialidad = especialidad


class Charla:
    def __init__(self, lugar, nombreCharla, speaker):
        self.lugar = lugar
        self.nombreCharla = nombreCharla
        self.S = speaker
        self.np = 0
        self.P = [None] * 50     # Arreglo para participantes

    def agregarParticipante(self, participante):
        if self.np < 50:
            self.P[self.np] = participante
            self.np += 1


class Evento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nc = 0
        self.C = [None] * 50   # Arreglo de charlas

    def agregarCharla(self, charla):
        if self.nc < 50:
            self.C[self.nc] = charla
            self.nc += 1

    # a) Edad promedio de los participantes del evento
    def edadPromedio(self):
        suma = 0
        cont = 0
        for i in range(self.nc):
            charla = self.C[i]
            for j in range(charla.np):
                suma += charla.P[j].edad
                cont += 1
        return suma / cont if cont > 0 else 0

    # b) Ver si persona X Y participa o es speaker
    def buscarPersona(self, nombre, apellido):
        for i in range(self.nc):
            charla = self.C[i]

            # Revisar speaker
            if charla.S.nombre == nombre and charla.S.apellido == apellido:
                return True

            # Revisar participantes
            for j in range(charla.np):
                p = charla.P[j]
                if p.nombre == nombre and p.apellido == apellido:
                    return True

        return False

    # c) El speaker con CI X no asistió → eliminar todas sus charlas
    def eliminarCharlasPorSpeaker(self, ci_buscar):
        nuevo = []
        for i in range(self.nc):
            charla = self.C[i]
            if charla.S.ci != ci_buscar:
                nuevo.append(charla)

        # Actualizar arreglo C[]
        self.nc = len(nuevo)
        self.C = nuevo + [None] * (50 - self.nc)

    # d) Ordenar las charlas por número de participantes
    def ordenarCharlasPorParticipantes(self):
        ordenadas = [self.C[i] for i in range(self.nc)]
        ordenadas.sort(key=lambda x: x.np, reverse=True)
        for i in range(len(ordenadas)):
            self.C[i] = ordenadas[i]
# ------------------------ PRUEBA RÁPIDA ------------------------
if __name__ == "__main__":
    # Crear evento
    e = Evento("TechConf 2025")

    # Crear speakers
    sp1 = Speaker("Ana", "Lopez", 35, 123, "IA")
    sp2 = Speaker("Luis", "Perez", 40, 777, "Redes")

    # Crear charlas
    c1 = Charla("Auditorio A", "Introducción a IA", sp1)
    c2 = Charla("Sala B", "Ciberseguridad 101", sp2)

    # Crear participantes
    p1 = Participante("Mario", "Rojas", 20, 456, 1)
    p2 = Participante("Laura", "Diaz", 22, 789, 2)
    p3 = Participante("Diego", "Mamani", 25, 321, 3)

    # Añadir participantes
    c1.agregarParticipante(p1)
    c1.agregarParticipante(p2)
    c2.agregarParticipante(p3)

    # Añadir charlas al evento
    e.agregarCharla(c1)
    e.agregarCharla(c2)

    print("Edad promedio:", e.edadPromedio())
    print("¿Está Laura Diaz?:", e.buscarPersona("Laura", "Diaz"))

    # Eliminar charlas del speaker con CI 777
    e.eliminarCharlasPorSpeaker(777)

    print("Charlas después de eliminar al speaker 777:", e.nc)

    # Ordenar charlas
    e.ordenarCharlasPorParticipantes()

    print("Charlas ordenadas (solo muestra np):")
    for i in range(e.nc):
        print(e.C[i].nombreCharla, "→", e.C[i].np, "participantes")
