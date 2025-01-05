import os
import pandas as pd
import json
from flask import Flask, render_template

app = Flask(__name__)

def inicializar_datos(filepath):
    """Carga los datos desde un archivo JSON y crea un DataFrame de clasificación inicial."""
    with open(filepath, 'r', encoding='utf-8') as file:
        datos_partidos = json.load(file)['datos_partidos']

    jugadores = set()
    for partido in datos_partidos:
        jugadores.add(partido['Local'])
        jugadores.add(partido['Visitante'])

    jugadores.discard("Descansa")
    jugadores.discard("Bye")

    clasificacion = {
        'Jugador': list(jugadores),
        'Puntos': [0] * len(jugadores),
        'P.J': [0] * len(jugadores),
        'P.G': [0] * len(jugadores),
        'P.P': [0] * len(jugadores),
        'S.G': [0] * len(jugadores),
        'S.P': [0] * len(jugadores),
        'J.G': [0] * len(jugadores),
        'J.P': [0] * len(jugadores),
        'D.J': [0] * len(jugadores),
    }

    df_partidos = pd.DataFrame(datos_partidos)
    df_clasificacion = pd.DataFrame(clasificacion)

    return df_partidos, df_clasificacion

def actualizar_clasificacion(df_partidos, df_clasificacion):
    # Reiniciar estadísticas
    df_clasificacion.update(df_clasificacion[['Puntos', 'P.J', 'P.G', 'P.P', 'S.G', 'S.P', 'J.G', 'J.P', 'D.J']].apply(lambda x: 0))

    for index, partido in df_partidos.iterrows():
        local = partido['Local']
        visitante = partido['Visitante']

        sets_local = 0
        sets_visitante = 0
        juegos_local = 0
        juegos_visitante = 0

        for set_result in [partido['Set 1'], partido['Set 2'], partido['Set 3']]:
            if '-' in set_result:
                local_set, visitante_set = map(int, set_result.split('-'))
                juegos_local += local_set
                juegos_visitante += visitante_set
                if local_set > visitante_set:
                    sets_local += 1
                else:
                    sets_visitante += 1

        if sets_local > sets_visitante:
            ganador, perdedor = local, visitante
        elif sets_visitante > sets_local:
            ganador, perdedor = visitante, local
        else:
            continue

        # Determinar puntos para el perdedor
        puntos_perdedor = 2 if sets_local + sets_visitante == 3 else 1
        puntos_ganador = 3

        # Actualizar estadísticas del ganador
        df_clasificacion.loc[df_clasificacion['Jugador'] == ganador, ['P.J', 'P.G', 'S.G', 'S.P', 'J.G', 'J.P', 'Puntos']] += [
            1, 1, max(sets_local, sets_visitante), min(sets_local, sets_visitante),
            juegos_local if ganador == local else juegos_visitante,
            juegos_visitante if ganador == local else juegos_local,
            puntos_ganador
        ]

        # Actualizar estadísticas del perdedor
        df_clasificacion.loc[df_clasificacion['Jugador'] == perdedor, ['P.J', 'P.P', 'S.G', 'S.P', 'J.G', 'J.P', 'Puntos']] += [
            1, 1, min(sets_local, sets_visitante), max(sets_local, sets_visitante),
            juegos_visitante if perdedor == visitante else juegos_local,
            juegos_local if perdedor == visitante else juegos_visitante,
            puntos_perdedor
        ]

    # Calcular la diferencia de juegos
    df_clasificacion['D.J'] = df_clasificacion['J.G'] - df_clasificacion['J.P']
    # Ordenar la clasificación
    df_clasificacion.sort_values(by=['Puntos', 'D.J', 'S.G'], ascending=[False, False, False], inplace=True)
    df_clasificacion.reset_index(drop=True, inplace=True)

    return df_clasificacion

def generar_cuadro_enfrentamientos(df_partidos):
    """Genera un cuadro de enfrentamientos basado en los partidos jugados."""
    jugadores = set(df_partidos['Local']).union(set(df_partidos['Visitante']))
    jugadores.discard('Descansa')  # Excluir 'Descansa' de la matriz
    jugadores = sorted(jugadores)  # Ordenar alfabéticamente para mantener consistencia

    # Crear un DataFrame vacío para la matriz de enfrentamientos
    cuadro = pd.DataFrame('', index=jugadores, columns=jugadores)

    for _, partido in df_partidos.iterrows():
        local = partido['Local']
        visitante = partido['Visitante']
        resultado = f"{partido['Set 1']} {partido['Set 2']} {partido['Set 3']}".strip()

        if local != 'Descansa' and visitante != 'Descansa':
            cuadro.loc[local, visitante] = resultado

    return cuadro

@app.route('/')
def mostrar_tablas():
    """Renderiza las tablas de clasificación y cuadros de enfrentamientos desde los JSON en la carpeta data."""
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    tablas = {}
    cuadros = {}

    for filename in os.listdir(data_dir):
        if filename.endswith('.json'):
            filepath = os.path.join(data_dir, filename)
            df_partidos, df_clasificacion = inicializar_datos(filepath)
            df_clasificacion = actualizar_clasificacion(df_partidos, df_clasificacion)
            cuadro_enfrentamientos = generar_cuadro_enfrentamientos(df_partidos)

            # Guardar las tablas en HTML
            tablas[filename.split('.')[0]] = df_clasificacion.to_html(index=False, classes='table table-striped')
            cuadros[filename.split('.')[0]] = cuadro_enfrentamientos.to_html(index=True, classes='table table-bordered')

    return render_template('tablas.html', tablas=tablas, cuadros=cuadros)

if __name__ == '__main__':
    app.run(debug=True)
