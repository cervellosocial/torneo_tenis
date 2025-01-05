import pandas as pd

def inicializar_datos():
    # Crear un DataFrame con la estructura de los partidos
    datos_partidos = [
        # Jornada 1
        {'Jornada': 1, 'Local': 'Alberto Díaz', 'Visitante': 'Sergi Déu déu', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 1, 'Local': 'Daniel Álvarez', 'Visitante': 'Domenec Ramadan', 'Set 1': '6-7', 'Set 2': '3-6', 'Set 3': ''},
        {'Jornada': 1, 'Local': 'Alberto Cerceda', 'Visitante': 'Antonio Ruiz', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 1, 'Local': 'Jose Luis', 'Visitante': 'Aurelio Calvo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 2
        {'Jornada': 2, 'Local': 'Alberto Díaz', 'Visitante': 'Domenec Ramadan', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 2, 'Local': 'Sergi Déu déu', 'Visitante': 'Antonio Ruiz', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 2, 'Local': 'Daniel Álvarez', 'Visitante': 'Aurelio Calvo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 2, 'Local': 'Alberto Cerceda', 'Visitante': 'Jose Luis', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 3
        {'Jornada': 3, 'Local': 'Alberto Díaz', 'Visitante': 'Antonio Ruiz', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 3, 'Local': 'Domenec Ramadan', 'Visitante': 'Aurelio Calvo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 3, 'Local': 'Sergi Déu déu', 'Visitante': 'Jose Luis', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 3, 'Local': 'Daniel Álvarez', 'Visitante': 'Alberto Cerceda', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 4
        {'Jornada': 4, 'Local': 'Aurelio Calvo', 'Visitante': 'Alberto Díaz', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 4, 'Local': 'Jose Luis', 'Visitante': 'Antonio Ruiz', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 4, 'Local': 'Alberto Cerceda', 'Visitante': 'Domenec Ramadan', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 4, 'Local': 'Daniel Álvarez', 'Visitante': 'Sergi Déu déu', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 5
        {'Jornada': 5, 'Local': 'Jose Luis', 'Visitante': 'Alberto Díaz', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 5, 'Local': 'Alberto Cerceda', 'Visitante': 'Aurelio Calvo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 5, 'Local': 'Daniel Álvarez', 'Visitante': 'Antonio Ruiz', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 5, 'Local': 'Sergi Déu déu', 'Visitante': 'Domenec Ramadan', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 6
        {'Jornada': 6, 'Local': 'Alberto Cerceda', 'Visitante': 'Alberto Díaz', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 6, 'Local': 'Daniel Álvarez', 'Visitante': 'Jose Luis', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 6, 'Local': 'Sergi Déu déu', 'Visitante': 'Aurelio Calvo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 6, 'Local': 'Domenec Ramadan', 'Visitante': 'Antonio Ruiz', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 7
        {'Jornada': 7, 'Local': 'Daniel Álvarez', 'Visitante': 'Alberto Díaz', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 7, 'Local': 'Sergi Déu déu', 'Visitante': 'Alberto Cerceda', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 7, 'Local': 'Domenec Ramadan', 'Visitante': 'Jose Luis', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 7, 'Local': 'Antonio Ruiz', 'Visitante': 'Aurelio Calvo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
]

    df_partidos = pd.DataFrame(datos_partidos)

    # Crear un DataFrame para la clasificación inicial
    jugadores = ['Alberto Díaz', 'Sergi Déu déu', 'Daniel Álvarez', 'Domenec Ramadan',
        'Alberto Cerceda','Jose Luis','Antonio Ruiz','Aurelio Calvo']
    
    clasificacion = {
        'Jugador': jugadores,
        'Puntos': [0] * len(jugadores),
        'P.J': [0] * len(jugadores),
        'P.G': [0] * len(jugadores),
        'P.P': [0] * len(jugadores),
        'S.G': [0] * len(jugadores),
        'S.P': [0] * len(jugadores),
        'J.G': [0] * len(jugadores),
        'J.P': [0] * len(jugadores),
        'D.J': [0] * len(jugadores)
    }

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

def imprimir_clasificacion(df_clasificacion):
    df_clasificacion.insert(0, 'Posición', range(1, len(df_clasificacion) + 1))
    print(df_clasificacion[['Posición', 'Jugador', 'Puntos', 'P.J', 'P.G', 'P.P', 'S.G', 'S.P', 'J.G', 'J.P', 'D.J']])

# Inicializar datos
df_partidos, df_clasificacion = inicializar_datos()

# Actualizar clasificación
df_clasificacion = actualizar_clasificacion(df_partidos, df_clasificacion)

# Imprimir clasificación
imprimir_clasificacion(df_clasificacion)
