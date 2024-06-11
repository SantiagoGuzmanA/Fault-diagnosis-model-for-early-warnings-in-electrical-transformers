# Proyecto1
# Fault Diagnosis Model for Early Warnings in Electrical Transformers

## Descripción General

### Objetivo del Proyecto
Desarrollar un modelo de diagnóstico de fallas para generar alertas tempranas en transformadores eléctricos, mejorando la eficiencia operativa y prolongando la vida útil de los equipos mediante la detección oportuna de anomalías.

### Problema a Resolver
Las fallas en transformadores pueden ser causadas por diversos factores como sobrecalentamiento, cortocircuitos, problemas de aislamiento y descargas parciales. Estas fallas, sin un sistema de alerta temprana efectivo, pueden resultar en eventos no programados, afectando la continuidad del suministro eléctrico y generando altos costos de reparación. El modelo desarrollado busca mitigar estos problemas, contribuyendo a la eficiencia energética y a la gestión de transformadores eléctricos.

### Metodología
1. **Revisión Bibliográfica**: Selección del método de análisis de variables eléctricas.
2. **Selección del Método de Análisis**: Evaluación y selección del método más adecuado.
3. **Identificación de Técnica de Procesamiento**: Investigación y selección de técnicas de procesamiento de datos.
4. **Desarrollo del Modelo**: Integración de resultados y establecimiento de umbrales de alarma.
5. **Validación**: Pruebas de simulación y ajustes necesarios.
6. **Documentación y Difusión**: Elaboración de documentos detallados sobre el proceso y resultados.

## Configuración del Entorno

### Requisitos del Sistema
- Python 3.x
- Librerías: sys, os, numpy, matplotlib, seaborn, pandas, math, time, scipy, sklearn


### Instalación de Dependencias
```bash
git clone https://github.com/tu_usuario/Fault-diagnosis-model-for-early-warnings-in-electrical-transformers.git
cd Fault-diagnosis-model-for-early-warnings-in-electrical-transformers
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
Fundamentación Teórica
```
Fundamentación Teórica
El diagnóstico temprano de fallas en transformadores eléctricos es crucial para prevenir fallas mayores y reducir costos de mantenimiento. Diversos métodos, como el monitoreo de gases disueltos, termografía infrarroja y análisis de parámetros eléctricos, son utilizados para detectar fallas. Integrar múltiples métodos puede proporcionar una evaluación más completa de la salud del transformador.

Referencias:

Youssef et al., 2022
Juan Z et al., 2019
Lynn Hamrick, 2009
Hussain et al., 2021
Abbasi, 2022
Kang et al., 2004
Asadi & Kelk, 2015
Masoum et al., 2017
Resultados
El modelo desarrollado ha mostrado una precisión del X% en la detección de fallas. Los resultados incluyen gráficos y tablas que detallan las métricas de rendimiento.

Discusión y Conclusiones
Los resultados indican que el modelo es efectivo para la detección temprana de fallas. Sin embargo, se identifican áreas de mejora, como la integración de más datos y la optimización de los algoritmos utilizados. Futuros trabajos podrían enfocarse en la validación del modelo en condiciones reales.

Estructura del Proyecto
src/: Códigos fuente en Python.
data/: Datasets utilizados.
results/: Resultados obtenidos, incluyendo figuras, gráficos y tablas.
