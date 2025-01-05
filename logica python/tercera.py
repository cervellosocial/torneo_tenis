import pandas as pd

def inicializar_datos():
    # Crear un DataFrame con la estructura de los partidos
    datos_partidos = [
        {'Jornada': 1, 'Local': 'Montse Solsona', 'Visitante': 'Jordi Garrido', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 1, 'Local': 'Jose Antonio', 'Visitante': 'Marc Garrido', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 1, 'Local': 'Soledad Manes', 'Visitante': 'Laura Nasta', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 2
        {'Jornada': 2, 'Local': 'Montse Solsona', 'Visitante': 'Marc Garrido', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 2, 'Local': 'Jordi Garrido', 'Visitante': 'Laura Nasta', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 2, 'Local': 'Jose Antonio', 'Visitante': 'Soledad Manes', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 3
        {'Jornada': 3, 'Local': 'Montse Solsona', 'Visitante': 'Laura Nasta', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 3, 'Local': 'Marc Garrido', 'Visitante': 'Soledad Manes', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 3, 'Local': 'Jordi Garrido', 'Visitante': 'Jose Antonio', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 4
        {'Jornada': 4, 'Local': 'Montse Solsona', 'Visitante': 'Soledad Manes', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 4, 'Local': 'Laura Nasta', 'Visitante': 'Jose Antonio', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 4, 'Local': 'Marc Garrido', 'Visitante': 'Jordi Garrido', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 5
        {'Jornada': 5, 'Local': 'Montse Solsona', 'Visitante': 'Jose Antonio', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 5, 'Local': 'Soledad Manes', 'Visitante': 'Jordi Garrido', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 5, 'Local': 'Laura Nasta', 'Visitante': 'Marc Garrido', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 6
        {'Jornada': 6, 'Local': 'Jordi Garrido', 'Visitante': 'Jose Antonio', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 6, 'Local': 'Marc Garrido', 'Visitante': 'Soledad Manes', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 6, 'Local': 'Laura Nasta', 'Visitante': 'Montse Solsona', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 7
        {'Jornada': 7, 'Local': 'Marc Garrido', 'Visitante': 'Montse Solsona', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 7, 'Local': 'Laura Nasta', 'Visitante': 'Jordi Garrido', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 7, 'Local': 'Soledad Manes', 'Visitante': 'Jose Antonio', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 8
        {'Jornada': 8, 'Local': 'Laura Nasta', 'Visitante': 'Montse Solsona', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 8, 'Local': 'Soledad Manes', 'Visitante': 'Marc Garrido', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 8, 'Local': 'Jose Antonio', 'Visitante': 'Jordi Garrido', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 9
        {'Jornada': 9, 'Local': 'Soledad Manes', 'Visitante': 'Montse Solsona', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 9, 'Local': 'Jose Antonio', 'Visitante': 'Laura Nasta', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 9, 'Local': 'Jordi Garrido', 'Visitante': 'Marc Garrido', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 10
        {'Jornada': 10, 'Local': 'Jose Antonio', 'Visitante': 'Montse Solsona', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 10, 'Local': 'Jordi Garrido', 'Visitante': 'Soledad Manes', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 10, 'Local': 'Marc Garrido', 'Visitante': 'Laura Nasta', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
    ]


    df_partidos = pd.DataFrame(datos_partidos)

    # Crear un DataFrame para la clasificación inicial
    jugadores = ['Montse Solsona', 'Jordi Garrido', 'Jose Antonio',
    'Marc Garrido', 'Soledad Manes', 'Laura Nasta']

    
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
