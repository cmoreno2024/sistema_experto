# rules.py
# Aquí se definen las reglas del sistema experto para la asignación de habitaciones

from experta import Fact, Rule, KnowledgeEngine
from experta import P, AS

class Cliente(Fact):
    """Información sobre el cliente"""
    pass

class Habitacion(Fact):
    """Información sobre la habitación"""
    pass

class Reserva(Fact):
    """Información sobre la reserva"""
    pass

def generar_habitaciones():
    habitaciones = []
    for piso in range(1, 11):
        for numero in range(1, 6):
            if numero <= 3:
                vista = 'sin_vista'
            else:
                vista = 'canal'
            habitaciones.append({
                'piso': piso,
                'numero': numero,
                'vista': vista,
                'capacidad': 5,
                'disponible': True
            })
    return habitaciones

class AsignacionHabitacion(KnowledgeEngine):
    def __init__(self, habitaciones):
        super().__init__()
        self.habitaciones = habitaciones
        self.asignada = None

    @Rule(Cliente(tipo='VIP'),
          AS.habitacion << Habitacion(vista='canal', disponible=True, piso=P(lambda x: x >= 7)))
    def asignar_vip_canal_alta(self, habitacion):
        self.asignada = habitacion
        print(f"Asignar habitación premium con vista al canal en piso alto: Piso {habitacion['piso']} Habitación {habitacion['numero']}")
        self.habitaciones.remove(habitacion)

    @Rule(Cliente(preferencia_vista='canal'),
          AS.habitacion << Habitacion(vista='canal', disponible=True))
    def asignar_preferencia_canal(self, habitacion):
        self.asignada = habitacion
        print(f"Asignar habitación con vista al canal: Piso {habitacion['piso']} Habitación {habitacion['numero']}")
        self.habitaciones.remove(habitacion)

    @Rule(Cliente(),
          AS.habitacion << Habitacion(disponible=True))
    def asignar_cualquier_disponible(self, habitacion):
        self.asignada = habitacion
        print(f"Asignar cualquier habitación disponible: Piso {habitacion['piso']} Habitación {habitacion['numero']}")
        self.habitaciones.remove(habitacion)

    @Rule(Cliente(tipo='VIP'), Habitacion(vista='mar', disponible=True))
    def asignar_vip_mar(self):
        print('Asignar habitación con vista al mar al cliente VIP')

    @Rule(Cliente(tipo='VIP'), Habitacion(vista='montaña', disponible=True))
    def asignar_vip_montana(self):
        print('Asignar habitación con vista a la montaña al cliente VIP')

    @Rule(Cliente(edad=P(lambda x: x >= 65)), Habitacion(piso=P(lambda x: x <= 2), disponible=True))
    def asignar_piso_bajo_mayores(self):
        print('Asignar habitación en piso bajo a persona mayor')

    @Rule(Cliente(tipo='familia'), Reserva(habitaciones_contiguas=True), Habitacion(contigua=True, disponible=True))
    def asignar_habitaciones_contiguas(self):
        print('Asignar habitaciones contiguas para familia')

    @Rule(Cliente(tipo='familia'), Reserva(habitaciones_contiguas=True), Habitacion(contigua=True, disponible=True, capacidad=P(lambda x: x >= 4)))
    def asignar_familia_grande_contigua(self):
        print('Asignar habitación contigua y amplia para familia grande')

    @Rule(Cliente(tipo='pareja'), Habitacion(tipo_cama='matrimonial', disponible=True))
    def asignar_pareja_matrimonial(self):
        print('Asignar habitación con cama matrimonial a pareja')

    @Rule(Cliente(tipo='persona_mayor'), Habitacion(piso=P(lambda x: x == 1), disponible=True))
    def asignar_persona_mayor_planta_baja(self):
        print('Asignar habitación en planta baja a persona mayor')

    @Rule(Cliente(preferencia_cama='matrimonial'), Habitacion(tipo_cama='matrimonial', disponible=True))
    def asignar_cama_matrimonial(self):
        print('Asignar habitación con cama matrimonial según preferencia')

    @Rule(Cliente(preferencia_cama='twin'), Habitacion(tipo_cama='twin', disponible=True))
    def asignar_cama_twin(self):
        print('Asignar habitación con camas twin según preferencia')

    @Rule(Cliente(preferencia_vista='mar'), Habitacion(vista='mar', disponible=True))
    def asignar_preferencia_vista_mar(self):
        print('Asignar habitación con vista al mar según preferencia')

    @Rule(Cliente(preferencia_vista='montaña'), Habitacion(vista='montaña', disponible=True))
    def asignar_preferencia_vista_montana(self):
        print('Asignar habitación con vista a la montaña según preferencia')

    @Rule(Cliente(preferencia_vista='ciudad'), Habitacion(vista='ciudad', disponible=True))
    def asignar_preferencia_vista_ciudad(self):
        print('Asignar habitación con vista a la ciudad según preferencia')

    @Rule(Reserva(ocupacion=P(lambda x: x > 4)), Habitacion(capacidad=P(lambda x: x < 5)))
    def restriccion_ocupacion(self):
        print('No se puede asignar: la ocupación excede la capacidad de la habitación')

    @Rule(Cliente(tipo='Regular'), Habitacion(vista='ciudad', disponible=True))
    def asignar_regular_ciudad(self):
        print('Asignar habitación con vista a la ciudad a cliente regular')

    @Rule(Cliente(tipo='VIP'), Habitacion(disponible=False))
    def vip_sin_disponibilidad(self):
        print('No hay habitaciones disponibles para cliente VIP, sugerir upgrade o alternativa')

    # Puedes seguir agregando reglas según los casos del PDF
