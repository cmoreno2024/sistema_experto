from flask import Flask, render_template, request
from src.knowledge_base.rules import AsignacionHabitacion, Cliente, Habitacion, Reserva, generar_habitaciones

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    habitacion_asignada = None
    if request.method == 'POST':
        tipo_cliente = request.form.get('tipo_cliente')
        tipo_viaje = request.form.get('tipo_viaje')
        cantidad_pasajeros = int(request.form.get('cantidad_pasajeros'))
        preferencia_cama = request.form.get('preferencia_cama')
        preferencia_vista = request.form.get('preferencia_vista')
        habitaciones_contiguas = request.form.get('habitaciones_contiguas') == 'si'
        
        # NUEVOS CAMPOS DE ACCESIBILIDAD
        necesita_accesibilidad = request.form.get('necesita_accesibilidad') == 'si'
        edad = int(request.form.get('edad', 25))  # Edad por defecto 25
        movilidad_reducida = request.form.get('movilidad_reducida') == 'si'

        habitaciones = generar_habitaciones()
        
        # PRIORIDAD ALTA: Si necesita accesibilidad, filtrar solo habitaciones accesibles
        if necesita_accesibilidad or movilidad_reducida or edad >= 70:
            habitaciones = [h for h in habitaciones if h['accesible'] == True]
            print(f"🦽 FILTRO DE ACCESIBILIDAD APLICADO: {len(habitaciones)} habitaciones adaptadas disponibles")
        else:
            # Marcar pisos según tipo de cliente (solo si no necesita accesibilidad)
            if tipo_cliente == 'VIP':
                pisos_validos = list(range(6, 11))
            else:
                pisos_validos = list(range(1, 6))
            habitaciones = [h for h in habitaciones if h['piso'] in pisos_validos]

        # Marcar vista según preferencia
        if preferencia_vista == 'canal':
            habitaciones = [h for h in habitaciones if h['numero'] in [4, 5]]
        elif preferencia_vista == 'montaña':
            habitaciones = [h for h in habitaciones if h['numero'] in [1, 2, 3]]

        # Habitaciones menos ruidosas para trabajo o pareja: 3 y 4
        if tipo_viaje in ['trabajo', 'pareja']:
            if preferencia_vista == 'canal':
                habitaciones = [h for h in habitaciones if h['numero'] == 4]
            elif preferencia_vista == 'montaña':
                habitaciones = [h for h in habitaciones if h['numero'] == 3]

        # Filtrar por capacidad
        habitaciones = [h for h in habitaciones if h['capacidad'] >= cantidad_pasajeros]

        engine = AsignacionHabitacion(habitaciones)
        engine.reset()
        
        # Declarar cliente con información de accesibilidad
        cliente_kwargs = {
            'tipo': tipo_cliente,
            'tipo_viaje': tipo_viaje, 
            'preferencia_cama': preferencia_cama,
            'preferencia_vista': preferencia_vista,
            'necesita_accesibilidad': necesita_accesibilidad,
            'edad': edad,
            'movilidad_reducida': movilidad_reducida
        }
        engine.declare(Cliente(**cliente_kwargs))
        
        reserva_kwargs = {'ocupacion': cantidad_pasajeros}
        if tipo_viaje == 'familiar':
            reserva_kwargs['habitaciones_contiguas'] = habitaciones_contiguas
        engine.declare(Reserva(**reserva_kwargs))
        for h in habitaciones:
            engine.declare(Habitacion(**h))
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
