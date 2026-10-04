SINTOMAS = ['cefalea', 'dolrretroo', 'malgias', 'artralgia', 'erupcionr', 'dolor_abdo', 'vomito']
ALARMA = ['somnolenci', 'hipotensio', 'hepatomeg', 'hem_mucosa', 'hipotermia',
          'aum_hemato', 'caida_plaq', 'acum_liquievento']

def agregar_conteos(X):
    """Conteos de dos grupos de variables; no son una escala clínica validada.

    Un faltante no se interpreta como ausencia. Un grupo completamente sin
    datos tiene conteo NaN; también se conserva el número de datos faltantes.
    """
    X = X.copy()
    for nombre, columnas in [('alarma', ALARMA), ('sintomas', SINTOMAS)]:
        X['n_' + nombre] = X[columnas].sum(axis=1, min_count=1)
        X['n_faltantes_' + nombre] = X[columnas].isna().sum(axis=1)
    return X
