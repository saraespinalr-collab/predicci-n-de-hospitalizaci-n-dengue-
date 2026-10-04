# Dengue: clasificación de hospitalización registrada

Proyecto académico CRISP-DM. Fuente declarada: SIVIGILA / Medata, Medellín.
URL exacta del dataset y ficha de códigos: [Completar con fuentes verificadas].
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

## Evidencia pendiente
URL pública: [Completar después de verificar la app].
Repositorio GitHub: [Completar con URL real].
Captura de funcionamiento: [Adjuntar captura real].

Apoyo analítico académico. No determina necesidad clínica ni reemplaza criterio médico.
Uso real sujeto a validación clínica, monitoreo de sesgos y aprobación institucional.
