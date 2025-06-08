# Proyecto de sistema experto: Optimización de la Asignación de Habitaciones en Hoteles de Ushuaia

## Descripción del Proyecto

Este proyecto de Sistema Experto se enfoca en el desarrollo de un modelo de decisión para la asignación óptima de habitaciones en hoteles de Ushuaia, considerando las diversas preferencias de los turistas.El objetivo es mejorar la eficiencia operativa del hotel y, fundamentalmente, aumentar la satisfacción del cliente al garantizar que, en la medida de lo posible, se cumplan sus solicitudes específicas.

El sistema funcionará como un asistente inteligente para el personal de reservas, ofreciendo recomendaciones de asignación de habitaciones basadas en un conjunto de reglas y conocimientos predefinidos.Estas reglas incorporarán tanto la disponibilidad del inventario de habitaciones como la jerarquía y compatibilidad de las preferencias de los huéspedes.

## Objetivo del Trabajo

El objetivo principal de este trabajo es minimizar la insatisfacción de los huéspedes y optimizar la utilización del inventario de habitaciones del hotel mediante la implementación de un Sistema Experto capaz de:
*Clasificar y priorizar las preferencias de los turistas de manera estructurada.
*Evaluar la disponibilidad de habitaciones en tiempo real.
*Proponer la mejor asignación de habitación para cada reserva, buscando el mayor grado de cumplimiento de las preferencias del huésped, respetando al mismo tiempo las restricciones del hotel.

El problema específico a abordar es la ineficiente y subjetiva asignación manual de habitaciones, que a menudo ignora o gestiona mal las preferencias individuales de los turistas, llevando a experiencias negativas y una subutilización de las habitaciones más valoradas.

## Contexto del Problema y su Relevancia

El problema de la asignación de habitaciones es una constante en la industria hotelera, pero adquiere una relevancia particular en Ushuaia, especialmente durante la temporada alta y eventos especiales. [cite_start]En estos períodos, la capacidad hotelera puede verse desbordada y la demanda de ciertas características de habitación (como vistas al Canal Beagle o habitaciones comunicadas para familias) excede la oferta.

Actualmente, muchos hoteles (incluido el de mi contexto laboral) dependen de procesos manuales o sistemas de gestión hotelera (PMS) básicos que no tienen la capacidad de aplicar lógica compleja para la asignación basada en preferencias. Esto resulta en:
**Insatisfacción del cliente**: Huéspedes que no obtienen la habitación deseada a menudo expresan frustración, lo que se traduce en quejas directas, malas reseñas online y una menor probabilidad de repetir la visita.
**Ineficiencia operativa**: El personal de reservas invierte tiempo considerable en tratar de conciliar manualmente las preferencias, a menudo realizando reasignaciones de última hora o gestionando reclamaciones post-check-in, lo que impacta la productividad.
**Pérdida de ingresos potenciales**: Si las habitaciones premium (con vista, por ejemplo) no se asignan de manera óptima o se ofrecen a huéspedes que no las valoran tanto, el hotel pierde la oportunidad de maximizar sus ingresos.
**Subjetividad en la asignación**: Las decisiones pueden variar entre los miembros del personal, lo que lleva a inconsistencias y una falta de un criterio unificado.

La relevancia de abordar este problema radica en que una asignación mejorada no solo impactará positivamente la satisfacción del cliente y la reputación del hotel, sino que también generará un beneficio económico tangible a través de una mejor gestión del inventario y una reducción de los costos asociados a la insatisfacción (compensaciones, gestión de quejas, etc.).

## Aporte del Sistema Experto

El Sistema Experto aportará una solución estructurada y lógica al problema de la asignación de habitaciones, transformando un proceso subjetivo y manual en uno basado en el conocimiento y la optimización. Específicamente, su aporte será:
**Automatización inteligente de la asignación**: Proporcionará recomendaciones de asignación de habitaciones, reduciendo la carga de trabajo manual y la probabilidad de errores humanos.
**Consistencia en las decisiones**: Asegurará que las decisiones de asignación sigan un conjunto de reglas predefinidas y lógicas, eliminando la variabilidad individual del personal.
**Maximización de la satisfacción del cliente**: Al priorizar y satisfacer las preferencias del huésped de manera eficiente, el sistema contribuirá directamente a una mejor experiencia de estadía.
**Optimización del uso del inventario**: Permitirá al hotel maximizar la utilización de sus habitaciones más demandadas y valiosas, lo que puede traducirse en un aumento de ingresos.
**Facilitación de la toma de decisiones**: Actuará como una herramienta de apoyo para el personal de reservas, proporcionando una base lógica para justificar las asignaciones y manejar situaciones complejas.
**Base de conocimiento evolutiva**: A medida que se incorpore más experiencia y se refinen las reglas, el sistema podrá aprender y mejorar sus recomendaciones con el tiempo, adaptándose a nuevas preferencias o situaciones del mercado.

## Arquitectura del Conocimiento

La arquitectura del conocimiento se basa en la extracción y organización de la experticia humana para guiar las decisiones del sistema.

### 1. Estructura del Conocimiento

El conocimiento se organiza en:
* **Hechos (Base de Datos o Memoria de Trabajo)**:
    * **Inventario de Habitaciones**: Número, tipo, características especiales (vistas al Canal Beagle, balcón, tamaño, habitaciones comunicadas, accesibilidad), estado (limpia/sucia, disponible/ocupada).
    * **Reservas Activas**: ID, fechas de check-in/out, número de huéspedes, tipo de habitación reservada, preferencias específicas del huésped, historial de estadías, categoría de cliente (VIP, recurrente).
    * **Disponibilidad en Tiempo Real**: Actualización constante de habitaciones libres y ocupadas.
    * **Reglas de Negocio del Hotel**: Políticas internas (ej. priorización de ciertos tipos de clientes, restricciones de asignación por duración de estadía).
* **Base de Conocimiento (Reglas y Criterios)**: Contiene el conocimiento heurístico y declarativo del experto codificado en reglas.

### 2. Organización del Conocimiento: Reglas y Criterios

Las preferencias de los turistas se clasifican y priorizan con un "peso" o "nivel de importancia":
* **Preferencias de Alta Prioridad (Críticas)**: Generan alta insatisfacción si no se cumplen (ej. habitaciones comunicadas, accesibilidad, camas específicas).
* **Preferencias de Media Prioridad (Deseables)**: Mejoran la experiencia (ej. vistas al Canal Beagle, balcón, piso alto/bajo).
* **Preferencias de Baja Prioridad (Opcionales)**: Flexibles, contribuyen a la satisfacción (ej. habitación en esquina, lejos del ruido).

**Ejemplos de Reglas (If-Then):**
* **Regla de Preferencias Críticas:** `IF (Reserva solicita "habitaciones comunicadas") AND (Existen habitaciones comunicadas disponibles que cumplen con el tipo de habitación reservado) THEN (Priorizar la asignación de habitaciones comunicadas y verificar compatibilidad con otras preferencias de alta prioridad).`
* **Regla de Priorización de Vistas:** `IF (Reserva solicita "vista al Canal Beagle") AND (Existen habitaciones con vista al Canal Beagle disponibles del tipo reservado) AND (La asignación no entra en conflicto con una preferencia de mayor prioridad) THEN (Considerar la asignación de una habitación con vista al Canal Beagle).`
* **Regla de Optimización de Habitaciones Premium:** `IF (Una habitación premium (ej. con vista al Canal Beagle) está disponible) AND (Existen múltiples reservas que cumplen con los requisitos básicos para esa habitación) THEN (Asignar la habitación premium a la reserva que tiene una preferencia explícita por ella O a un cliente VIP/recurrente que la valore más, según políticas del hotel).`
* **Regla de Manejo de Restricciones:** `IF (La asignación propuesta viola una restricción del hotel) THEN (Descartar la asignación y buscar una alternativa que cumpla con las restricciones).`
* **Regla de Resolución de Conflictos:** `IF (Múltiples habitaciones cumplen con las preferencias) THEN (Seleccionar la habitación que maximice el cumplimiento de preferencias secundarias, o la que minimice futuros conflictos de asignación, o la que optimice la ocupación).`

### 3. Métodos de Inferencia

El Sistema Experto utilizará principalmente:
* **Encadenamiento Hacia Adelante (Forward Chaining)**: A partir de los hechos conocidos (preferencias, disponibilidad), el sistema aplicará reglas para inferir conclusiones y refinar la lista de habitaciones candidatas.
* **Sistema Basado en Reglas con Puntaje**: Cada preferencia satisfecha otorga un puntaje (mayor para preferencias de alta prioridad). Se recomienda la habitación con el puntaje total más alto, permitiendo una evaluación cuantitativa.
* **Encadenamiento Hacia Atrás (Backward Chaining - para diagnósticos/explicaciones)**: Permite justificar por qué se asignó una habitación particular, rastreando las reglas que llevaron a esa decisión.

### 4. Lógica de Organización del Conocimiento

La organización busca replicar la experticia humana mediante:
* **Modularidad**: Reglas agrupadas por función para facilitar mantenimiento y adición.
* **Jerarquía de Preferencias**: Asegura que las necesidades críticas se aborden primero.
* **Secuencia de Evaluación**: Sigue un flujo lógico: restricciones > preferencias absolutas > preferencias de menor prioridad > optimización.
* **Resolución de Conflictos**: Reglas específicas para manejar situaciones complejas donde no todas las preferencias pueden cumplirse.
* **Explicabilidad**: Estructura clara que permite al sistema justificar sus decisiones.

## Contribuciones

Si deseas contribuir a este proyecto, por favor, sigue las siguientes pautas:
1.  Haz un "fork" del repositorio.
2.  Crea una nueva rama para tus cambios (`git checkout -b feature/nueva-caracteristica`).
3.  Realiza tus cambios y asegúrate de que el código sea claro y esté bien comentado.
4.  Realiza un "commit" de tus cambios (`git commit -m 'feat: Añadir nueva característica'`).
5.  Haz un "push" a tu rama (`git push origin feature/nueva-caracteristica`).
6.  Abre un "Pull Request" describiendo tus cambios.

## Licencia



## Contacto

Para consultas, puedes contactar a Celeste Moreno
Github cmoreno2024
Mail Celemore.cm@gmail.com
