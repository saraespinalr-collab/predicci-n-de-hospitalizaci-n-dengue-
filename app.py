import json
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
import streamlit as st
from utilidades import SINTOMAS, ALARMA, agregar_conteos

st.set_page_config(page_title='Hospitalización registrada en dengue', page_icon='🦟')
BASE = Path(__file__).resolve().parent

@st.cache_resource
def cargar():
    with (BASE / 'metadata.json').open(encoding='utf-8') as archivo:
        meta = json.load(archivo)
    return joblib.load(BASE / 'modelo_dengue.joblib'), meta

modelo, meta = cargar()
st.title('Dengue: demostrador de hospitalización registrada')
st.caption(f"{meta['modelo']} · Medellín · {meta['periodo']} · Evaluación retrospectiva")
st.info('Apoyo analítico académico. La salida no determina necesidad de hospitalizar ni reemplaza el criterio médico.')
st.caption(f"F1 test: {meta['f1_test']:.3f} · Recall test: {meta['recall_test']:.3f}")

REGIMEN = {'Contributivo': 'C', 'Subsidiado': 'S', 'Especial': 'E',
           'Excepción': 'P', 'No asegurado': 'N', 'Indeterminado': 'I'}
ETIQUETAS = {'cefalea':'Cefalea', 'dolrretroo':'Dolor retroocular', 'malgias':'Mialgias',
    'artralgia':'Artralgias', 'erupcionr':'Erupción cutánea', 'dolor_abdo':'Dolor abdominal',
    'vomito':'Vómito', 'somnolenci':'Somnolencia', 'hipotensio':'Hipotensión',
    'hepatomeg':'Hepatomegalia', 'hem_mucosa':'Hemorragia en mucosas', 'hipotermia':'Hipotermia',
    'aum_hemato':'Aumento del hematocrito', 'caida_plaq':'Caída de plaquetas',
    'acum_liquievento':'Acumulación de líquidos'}
OPCIONES = ['Desconocido/no evaluado', 'No', 'Sí']
MAPA = {'Desconocido/no evaluado': np.nan, 'No': 0, 'Sí': 1}

with st.form('entrada'):
    c1, c2 = st.columns(2)
    edad = c1.number_input('Edad en años', min_value=0.0, max_value=120.0, value=30.0, step=0.1)
    sexo = c2.selectbox('Sexo', ['Desconocido', 'Femenino', 'Masculino'])
    dias = c1.number_input('Días entre inicio de síntomas y consulta', 0, 30, 3)
    dias_desconocidos = c1.checkbox('Intervalo de síntomas desconocido')
    semana = c2.number_input('Semana epidemiológica de notificación', 1, 53, 20)
    comuna = c1.selectbox('Comuna', meta['comunas'])
    regimen = c2.selectbox('Régimen de salud', ['Desconocido'] + list(REGIMEN))
    despl = st.selectbox('Desplazamiento registrado', OPCIONES)
    valores = {}
    st.subheader('Variables registradas')
    columnas = st.columns(2)
    for i, variable in enumerate(SINTOMAS + ALARMA):
        respuesta = columnas[i % 2].selectbox(ETIQUETAS[variable], OPCIONES, key=variable)
        valores[variable] = MAPA[respuesta]
    enviar = st.form_submit_button('Obtener predicción del modelo')

if enviar:
    fila = {'edad_anios': edad, 'semana': semana,
        'dias_sintomas': np.nan if dias_desconocidos else dias,
        'sexo_': {'Desconocido': np.nan, 'Femenino': 0, 'Masculino': 1}[sexo],
        'desplazami': MAPA[despl], 'comuna': comuna,
        'tipo_ss_': REGIMEN.get(regimen, np.nan), **valores}
    entrada = pd.DataFrame([fila])[meta['columnas']]
    pred = int(modelo.predict(entrada)[0])  # Usa el umbral exacto serializado.
    st.write('Predicción del modelo: **' +
        ('Hospitalización registrada' if pred == 1 else 'Sin hospitalización registrada') + '**')
    if meta['tipo_salida'] == 'predict_proba':
        salida = float(modelo.predict_proba(entrada)[0, 1])
        st.metric('Salida del clasificador', f'{salida:.3f}')
        st.caption('Salida predict_proba. Su calibración como probabilidad individual no se ha evaluado.')
    else:
        salida = float(modelo.decision_function(entrada)[0])
        st.metric('Puntuación del clasificador', f'{salida:.3f}')
    st.caption(f"Umbral estadístico ajustado en entrenamiento: {meta['umbral']:.6f}")
    n_faltantes = int(entrada.isna().sum().sum())
    if n_faltantes:
        st.warning(f'{n_faltantes} entradas desconocidas: el pipeline aplica su tratamiento aprendido. No equivalen a ausencia clínica.')
    st.caption('Uso real sujeto a validación clínica, disponibilidad temporal de predictores, revisión de sesgos y aprobación institucional.')
