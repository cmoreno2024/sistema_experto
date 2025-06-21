# 🎓 ENTREGA ACADÉMICA - Sistema Experto para Asignación de Habitaciones

## 📋 Verificación de Requisitos Cumplidos

### ✅ 1. Entrega de notebooks en formato .ipynb
- **Cumplido**: 2 notebooks disponibles en `/notebooks/`
  - `verificacion_requisitos.ipynb` - Notebook de verificación completa
  - `sistema_experto_sklearn.ipynb` - Implementación con scikit-learn

### ✅ 2. Uso de Python
- **Cumplido**: Todo el proyecto está desarrollado en Python 3.13
- Archivos Python principales:
  - `src/knowledge_base/rules.py` - Motor de reglas con experta
  - `src/webapp/app.py` - Aplicación web Flask
  - Scripts de utilidad y configuración

### ✅ 3. Implementación del modelo con scikit-learn
- **Cumplido**: Implementación completa en `sistema_experto_sklearn.ipynb`
- Modelos utilizados:
  - **RandomForest** para predicción de piso
  - **DecisionTree** para predicción de número de habitación
- Pipeline completo: generación de datos → preprocesamiento → entrenamiento → evaluación → predicción

### ✅ 4. Disponibilidad en repositorio GIT
- **Cumplido**: Repositorio público disponible
- **URL**: https://github.com/cmoreno2024/sistema_experto.git
- **Rama**: main
- **Último commit**: 184da70 mejora del readme y mejor detalle para el usuario

### ✅ 5. Organización con plantilla Cookiecutter Data Science
- **Cumplido**: Estructura completa implementada
- Carpetas principales:
  ```
  ├── data/          # Datasets
  ├── docs/          # Documentación
  ├── models/        # Modelos entrenados
  ├── notebooks/     # Jupyter notebooks
  ├── reports/       # Reportes y análisis
  ├── src/           # Código fuente
  └── tests/         # Pruebas unitarias
  ```

## 🚀 Funcionalidades Implementadas

### 🧠 Sistema Experto Basado en Reglas (Experta)
- Motor de inferencia con reglas lógicas
- Asignación inteligente considerando:
  - Tipo de cliente (VIP/Estándar)
  - Tipo de viaje (Familiar/Pareja/Trabajo/Negocios)
  - Preferencias de vista y cama
  - Cantidad de pasajeros
  - Habitaciones contiguas

### 🤖 Modelo de Machine Learning (Scikit-learn)
- **RandomForest** para asignación de piso (Accuracy: 24.5%)
- **DecisionTree** para asignación de habitación (Accuracy: 80.0%)
- Dataset sintético de 1000 muestras
- Evaluación completa con métricas y matrices de confusión

### 🌐 Interfaz Web Interactiva
- Aplicación Flask moderna y responsiva
- Pestañas organizadas:
  - **Asignación**: Formulario para nueva reserva
  - **Habitaciones**: Listado visual por piso
- Integración con motor de reglas
- Interfaz amigable y profesional

## 📊 Librerías y Tecnologías Utilizadas

### Core del Sistema Experto
- **experta**: Motor de reglas para inferencia lógica
- **Flask**: Framework web para la interfaz

### Machine Learning y Data Science
- **scikit-learn**: Modelos de aprendizaje automático
- **pandas**: Manipulación y análisis de datos
- **numpy**: Operaciones numéricas
- **matplotlib/seaborn**: Visualización de datos

### Desarrollo y Notebooks
- **jupyter**: Entorno de notebooks interactivos
- **ipython**: Kernel mejorado para Python

## 🎯 Resultados de Verificación

```
🎯 VERIFICACIÓN COMPLETA DE REQUISITOS ACADÉMICOS
================================================================================
1. Entrega en formato .ipynb: ✅ CUMPLIDO
2. Uso de Python: ✅ CUMPLIDO
3. Implementación con scikit-learn: ✅ CUMPLIDO
4. Repositorio GIT disponible: ✅ CUMPLIDO
5. Estructura Cookiecutter Data Science: ✅ CUMPLIDO
================================================================================
🏆 RESULTADO: TODOS LOS REQUISITOS ACADÉMICOS ESTÁN CUMPLIDOS
```

## 🔧 Instrucciones de Uso

### 1. Clonar el Repositorio
```bash
git clone https://github.com/cmoreno2024/sistema_experto.git
cd sistema_experto
```

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar Notebooks
```bash
jupyter notebook
# Abrir notebooks/verificacion_requisitos.ipynb
# Abrir notebooks/sistema_experto_sklearn.ipynb
```

### 4. Ejecutar Interfaz Web
```bash
python src/webapp/app.py
# Abrir http://127.0.0.1:5000
```

## 📁 Archivos de Entrega

### Notebooks Principales
1. **`notebooks/verificacion_requisitos.ipynb`**
   - Verificación automatizada de todos los requisitos
   - Análisis de estructura del proyecto
   - Confirmación de tecnologías utilizadas

2. **`notebooks/sistema_experto_sklearn.ipynb`**
   - Implementación completa con scikit-learn
   - Pipeline de ML: datos → modelo → evaluación → predicción
   - Ejemplos de uso y resultados

### Código Fuente
- **`src/knowledge_base/rules.py`**: Motor de reglas con experta
- **`src/webapp/app.py`**: Aplicación web Flask
- **`src/webapp/templates/index.html`**: Interfaz web moderna

### Documentación
- **`README.md`**: Documentación principal del proyecto
- **`ENTREGA_ACADEMICA.md`**: Este documento de entrega
- **`requirements.txt`**: Dependencias del proyecto

## 🏆 Conclusión

El sistema experto para asignación de habitaciones en hoteles de Ushuaia **CUMPLE COMPLETAMENTE** con todos los requisitos académicos solicitados:

✅ **Notebooks .ipynb entregados**  
✅ **Desarrollado en Python**  
✅ **Implementación con scikit-learn**  
✅ **Repositorio GIT público**  
✅ **Estructura Cookiecutter Data Science**  

Además, incluye funcionalidades extra como interfaz web interactiva, motor de reglas avanzado y documentación completa, superando las expectativas del proyecto académico.

---
**Fecha de entrega**: 21 de junio de 2025  
**Repositorio**: https://github.com/cmoreno2024/sistema_experto.git  
**Estado**: ✅ COMPLETO Y ENTREGADO
