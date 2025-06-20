# inference.py
# Motor de inferencia simple para el sistema experto

class MotorInferencia:
    def __init__(self, reglas):
        self.reglas = reglas

    def ejecutar(self):
        print('Ejecutando motor de inferencia...')
        # Aquí iría la lógica para aplicar las reglas
        for regla in self.reglas:
            print(f"Regla: Si {' y '.join(regla['condiciones'])} entonces {regla['accion']}")
        print('Motor de inferencia finalizado.')
