# Dengue: clasificación de hospitalización registrada

Proyecto académico CRISP-DM. Fuente declarada: SIVIGILA / Medata, Medellín.
Dataset: https://medata.app.medellin.gov.co/dataset/1-026-22-000135
No se ha demostrado disponibilidad de todos los predictores antes de hospitalizar.

- Periodo: 2015–2021. Registros: 27,448.
- Partición por patrones idénticos: 70.01% entrenamiento y 29.99% test.
- Selección: CV anidada en entrenamiento; tolerancia académica de 0.01 F1 y prioridad a recall.
- Modelo: SVM. Umbral: 0.330527.
- Test retrospectivo: F1=0.6626; recall=0.7256; AUC=0.8494.
- La base fue explorada en el desarrollo. Estas métricas no son validación prospectiva.
- No se ha evaluado calibración de probabilidades individuales.
- Python del entrenamiento: 3.13.15. Usar la misma versión menor al desplegar.

## Archivos para desplegar
app.py, utilidades.py, modelo_dengue.joblib, metadata.json, requirements.txt y README.md,
en la misma carpeta. Los CSV y HTML se entregan por separado; no se incluyen en el repositorio público.

## Ejecutar
pip install -r requirements.txt
streamlit run app.py

## Enlaces
- App pública: https://jsg7trkphxk3fwjqsurska.streamlit.app/
- Cuaderno de Colab: https://colab.research.google.com/drive/1SsnkvqqgfVBqj6zPp7YPR4ShzoyUrKWA?usp=sharing
- Autoras: Andrea Restrepo Pérez y Sara Vanesa Espinal Ramírez

Apoyo analítico académico. No determina necesidad clínica ni reemplaza criterio médico.
Uso real sujeto a validación clínica, monitoreo de sesgos y aprobación institucional.
