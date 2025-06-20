# main.py
from knowledge_base.rules import AsignacionHabitacion, Cliente, Habitacion

def main():
    print('Sistema Experto: Asignación de habitaciones en hoteles de Ushuaia')
    engine = AsignacionHabitacion()
    engine.reset()
    # Ejemplo de hechos
    engine.declare(Cliente(tipo='VIP'))
    engine.declare(Habitacion(vista='mar', disponible=True))
    engine.run()

if __name__ == '__main__':
    main()
