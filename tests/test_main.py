# test_main.py
from src.engine.inference import MotorInferencia
from src.knowledge_base.rules import reglas, AsignacionHabitacion, Cliente, Habitacion

def test_motor_inferencia():
    motor = MotorInferencia(reglas)
    assert hasattr(motor, 'ejecutar')

def test_asignacion_vip():
    engine = AsignacionHabitacion()
    engine.reset()
    engine.declare(Cliente(tipo='VIP'))
    engine.declare(Habitacion(vista='mar', disponible=True))
    engine.run()
    # Aquí podrías capturar la salida o el estado para asserts más avanzados
