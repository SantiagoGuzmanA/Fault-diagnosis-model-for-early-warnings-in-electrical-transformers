# Fault Diagnosis Model for Early Warnings in Electrical Transformers
# SRC

## Environment Configuration
### System Requirements
```
- Python 3.12.0
- Bookstores: sys, os, numpy, matplotlib, seaborn, pandas, math, time, scipy, sklearn
```


### Installation of Dependencies
```bash
git clone https://github.com/SantiagoGuzmanA/Fault-diagnosis-model-for-early-warnings-in-electrical-transformers.git
cd Fault-diagnosis-model-for-early-warnings-in-electrical-transformers
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Este directorio contiene todos los códigos fuente en Python utilizados para el diagnóstico de fallas en transformadores eléctricos.

## Descripción de Archivos
- `main.py`: Script principal que coordina el preprocesamiento de datos, el entrenamiento del modelo y la generación de resultados.
- `mainpandas.py`: Script auxiliar para manipulación avanzada de datos.
- `preprocessing.py`: Funciones para el preprocesamiento de los datos.
- `model.py`: Definición y entrenamiento del modelo de diagnóstico.
- `evaluation.py`: Evaluación del rendimiento del modelo utilizando diversas métricas.

## Ejecución
Para ejecutar el análisis completo, utiliza los siguientes comandos desde el directorio raíz del proyecto:
```bash
python src/main.py
python src/mainpandas.py
