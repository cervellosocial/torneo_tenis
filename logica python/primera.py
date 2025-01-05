import pandas as pd

def inicializar_datos():
    # Crear un DataFrame con la estructura de los partidos
    datos_partidos = [
        {'Jornada': 1, 'Local': 'Mario Cuenca', 'Visitante': 'Alejandro Huertas', 'Set 1': '3-6', 'Set 2': '6-0', 'Set 3': '3-6'},
        {'Jornada': 1, 'Local': 'Esther Garrós', 'Visitante': 'Alejandro Ariza', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 1, 'Local': 'Crisanto Lucas', 'Visitante': 'Joan Agudo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 1, 'Local': 'Fran Morales', 'Visitante': 'Bye', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 1, 'Local': 'Javier Morant', 'Visitante': 'Alejo Zeballo', 'Set 1': '6-0', 'Set 2': '6-0', 'Set 3': ''},
        # Jornada 2
        {'Jornada': 2, 'Local': 'Fran Morales', 'Visitante': 'Joan Agudo', 'Set 1': '6-3', 'Set 2': '6-1', 'Set 3': ''},
        {'Jornada': 2, 'Local': 'Bye', 'Visitante': 'Esther Garrós', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 2, 'Local': 'Crisanto Lucas', 'Visitante': 'Alejandro Huertas', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 2, 'Local': 'Alejandro Ariza', 'Visitante': 'Alejo Zeballo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 2, 'Local': 'Mario Cuenca', 'Visitante': 'Javier Morant', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 3
        {'Jornada': 3, 'Local': 'Fran Morales', 'Visitante': 'Esther Garrós', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 3, 'Local': 'Joan Agudo', 'Visitante': 'Alejandro Huertas', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 3, 'Local': 'Bye', 'Visitante': 'Alejo Zeballo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 3, 'Local': 'Crisanto Lucas', 'Visitante': 'Javier Morant', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 3, 'Local': 'Alejandro Ariza', 'Visitante': 'Mario Cuenca', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 4
        {'Jornada': 4, 'Local': 'Fran Morales', 'Visitante': 'Alejandro Huertas', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 4, 'Local': 'Esther Garrós', 'Visitante': 'Alejo Zeballo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 4, 'Local': 'Joan Agudo', 'Visitante': 'Javier Morant', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 4, 'Local': 'Bye', 'Visitante': 'Mario Cuenca', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 4, 'Local': 'Crisanto Lucas', 'Visitante': 'Alejandro Ariza', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 5
        {'Jornada': 5, 'Local': 'Alejo Zeballo', 'Visitante': 'Fran Morales', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 5, 'Local': 'Javier Morant', 'Visitante': 'Alejandro Huertas', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 5, 'Local': 'Mario Cuenca', 'Visitante': 'Esther Garrós', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 5, 'Local': 'Alejandro Ariza', 'Visitante': 'Joan Agudo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 5, 'Local': 'Crisanto Lucas', 'Visitante': 'Bye', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 6
        {'Jornada': 6, 'Local': 'Javier Morant', 'Visitante': 'Fran Morales', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 6, 'Local': 'Mario Cuenca', 'Visitante': 'Alejo Zeballo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 6, 'Local': 'Alejandro Ariza', 'Visitante': 'Alejandro Huertas', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 6, 'Local': 'Crisanto Lucas', 'Visitante': 'Esther Garrós', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 6, 'Local': 'Bye', 'Visitante': 'Joan Agudo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 7
        {'Jornada': 7, 'Local': 'Mario Cuenca', 'Visitante': 'Fran Morales', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 7, 'Local': 'Alejandro Ariza', 'Visitante': 'Javier Morant', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 7, 'Local': 'Crisanto Lucas', 'Visitante': 'Alejo Zeballo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 7, 'Local': 'Bye', 'Visitante': 'Alejandro Huertas', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 7, 'Local': 'Joan Agudo', 'Visitante': 'Esther Garrós', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 8
        {'Jornada': 8, 'Local': 'Alejandro Ariza', 'Visitante': 'Fran Morales', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 8, 'Local': 'Crisanto Lucas', 'Visitante': 'Mario Cuenca', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 8, 'Local': 'Bye', 'Visitante': 'Javier Morant', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 8, 'Local': 'Joan Agudo', 'Visitante': 'Alejo Zeballo', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 8, 'Local': 'Esther Garrós', 'Visitante': 'Alejandro Huertas', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        # Jornada 9
        {'Jornada': 9, 'Local': 'Crisanto Lucas', 'Visitante': 'Fran Morales', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 9, 'Local': 'Bye', 'Visitante': 'Alejandro Ariza', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 9, 'Local': 'Joan Agudo', 'Visitante': 'Mario Cuenca', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 9, 'Local': 'Esther Garrós', 'Visitante': 'Javier Morant', 'Set 1': '', 'Set 2': '', 'Set 3': ''},
        {'Jornada': 9, 'Local': 'Alejandro Huertas', 'Visitante': 'Alejo Zeballo', 'Set 1': '', 'Set 2': '', 'Set 3': ''}
    ]
    
    df_partidos = pd.DataFrame(datos_partidos)

    # Crear un DataFrame para la clasificación inicial
    jugadores = ['Mario Cuenca', 'Alejandro Huertas', 'Esther Garrós', 'Alejandro Ariza', 
                 'Crisanto Lucas', 'Joan Agudo', 'Fran Morales', 'Javier Morant', 'Alejo Zeballo']
    
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
