from flask import Flask, render_template, request
from src.knowledge_base.rules import AsignacionHabitacion, Cliente, Habitacion, Reserva, generar_habitaciones

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    habitacion_asignada = None
    if request.method == 'POST':
        tipo_cliente = request.form.get('tipo_cliente')
        edad = request.form.get('edad')
        preferencia_cama = request.form.get('preferencia_cama')
        preferencia_vista = request.form.get('preferencia_vista')
        vista = request.form.get('vista')
        disponible = request.form.get('disponible') == 'si'
        piso = request.form.get('piso')
        tipo_cama = request.form.get('tipo_cama')
        capacidad = request.form.get('capacidad')
        contigua = request.form.get('contigua') == 'si'
        habitaciones_contiguas = request.form.get('habitaciones_contiguas') == 'si'
        ocupacion = request.form.get('ocupacion')

        habitaciones = generar_habitaciones()
        engine = AsignacionHabitacion(habitaciones)
        engine.reset()
        # Declarar hechos según los campos
        cliente_kwargs = {'tipo': tipo_cliente}
        if edad:
            cliente_kwargs['edad'] = int(edad)
        if preferencia_cama:
            cliente_kwargs['preferencia_cama'] = preferencia_cama
        if preferencia_vista:
            cliente_kwargs['preferencia_vista'] = preferencia_vista
        engine.declare(Cliente(**cliente_kwargs))

        # Declarar todas las habitaciones como hechos
        for h in habitaciones:
            engine.declare(Habitacion(**h))

        reserva_kwargs = {}
        if habitaciones_contiguas:
            reserva_kwargs['habitaciones_contiguas'] = habitaciones_contiguas
        if ocupacion:
            reserva_kwargs['ocupacion'] = int(ocupacion)
        if reserva_kwargs:
            engine.declare(Reserva(**reserva_kwargs))

        # Captura la salida de la inferencia
        import io, sys
        buffer = io.StringIO()
        sys.stdout = buffer
        engine.run()
        sys.stdout = sys.__stdout__
        resultado = buffer.getvalue()
        if engine.asignada:
            habitacion_asignada = engine.asignada
    return render_template('index.html', resultado=resultado, habitacion_asignada=habitacion_asignada)

if __name__ == '__main__':
    app.run(debug=True)
