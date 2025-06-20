# Sistema Experto para Asignación de Habitaciones en Hoteles de Ushuaia

![Logo Hotel Ushuaia](https://cdn-icons-png.flaticon.com/512/684/684908.png)

## Descripción
Este sistema experto, desarrollado en Python, optimiza la asignación de habitaciones en hoteles de Ushuaia según las preferencias y necesidades de cada cliente. Utiliza reglas de negocio reales y una interfaz web moderna para el departamento de reservas.

## Características principales
- Asignación automática de habitaciones según tipo de cliente (VIP o estándar), tipo de viaje, cantidad de pasajeros, preferencia de cama y vista.
- Reglas de negocio adaptadas a hoteles reales de Ushuaia.
- Interfaz web intuitiva y visualmente atractiva.
- Opción de habitaciones contiguas para familias y habitaciones silenciosas para trabajo o parejas.

## Estructura del proyecto
```
├── src/
│   ├── knowledge_base/   # Reglas y motor de inferencia
│   └── webapp/           # Aplicación web Flask
├── tests/                # Pruebas unitarias
├── documentacion/        # PDFs y documentación
├── requirements.txt      # Dependencias
├── README.md             # Este archivo
```

## Instalación y ejecución
1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPO>
   cd sistema_experto
   ```
2. Crea y activa un entorno virtual:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # En Windows
   # source .venv/bin/activate  # En Linux/Mac
   ```
3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
4. Ejecuta la aplicación web:
   ```bash
   python -m src.webapp.app
   ```
5. Abre tu navegador en [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Uso
1. Completa el formulario con los datos del cliente y sus preferencias.
2. El sistema asignará automáticamente la mejor habitación disponible y mostrará el resultado.
3. El cuadro de asignación detalla el piso (VIP o estándar), número, vista y si la habitación es silenciosa o normal.

## Ejemplo de uso
1. Ingresa los datos del cliente y preferencias en el formulario web:
   - Tipo de cliente: VIP o estándar
   - Tipo de viaje: familiar, pareja o trabajo
   - Cantidad de pasajeros: 1 a 5
   - Preferencia de cama: matrimonial o twin
   - Preferencia de vista: Canal Beagle o Montaña
   - Si el viaje es familiar, puedes elegir habitaciones contiguas
2. Haz clic en "Consultar asignación".
3. El sistema mostrará la habitación asignada, indicando:
   - Piso (VIP o estándar)
   - Número de habitación
   - Vista
   - Si es silenciosa o normal

### Captura de pantalla

![Ejemplo de interfaz](https://i.imgur.com/2Qw8QwB.png)

## Documentación adicional
- Las reglas de negocio y la lógica de inferencia están en `src/knowledge_base/rules.py`.
- Puedes consultar los documentos PDF en la carpeta `documentacion/` para ver la base de conocimiento y justificación de las reglas.

## Créditos y licencia
- Proyecto desarrollado por [Tu Nombre].
- Licencia MIT.
- Logo ficticio de hotel tomado de [flaticon.com](https://www.flaticon.com/free-icon/hotel_684908).

---
¿Dudas o sugerencias? Contacta al equipo de desarrollo o al área de reservas.
