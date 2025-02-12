import os
import pandas as pd
import numpy as np
import json
import jinja2 as jj

def inicializar_datos(filepath):
    """Carga los datos desde un archivo JSON y crea un DataFrame de clasificación inicial."""
    with open(filepath, 'r', encoding='utf-8') as file:
        datos_partidos = json.load(file)['datos_partidos']

    jugadores = set()
    for partido in datos_partidos:
        jugadores.add(partido['local'])
        jugadores.add(partido['visitante'])

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
        local = partido['local']
        visitante = partido['visitante']

        # Excluir partidos con "Descansa" o "Bye"
        if local in ['Descansa', 'Bye'] or visitante in ['Descansa', 'Bye'] or not partido['set_1']:
            continue
        

        sets_local = 0
        sets_visitante = 0
        juegos_local = 0
        juegos_visitante = 0

        sets = sorted([key for key in partido.keys() if 'set' in key])
        for set_result in [partido[set] for set in sets]:
            if '-' in set_result:
                local_set, visitante_set = map(int, set_result.split('-'))
                juegos_local += local_set
                juegos_visitante += visitante_set
                if local_set > visitante_set:
                    sets_local += 1
                else:
                    sets_visitante += 1

        if partido['tie'] :
            tie_local, tie_visitante = map(int, partido['tie'].split('-'))
            if tie_local > tie_visitante:
                juegos_local+=1
                sets_local+=1
            else:
                juegos_visitante+=1
                sets_visitante+=1

        # Determinar puntos para el perdedor
        puntos_local = 3 if sets_local>sets_visitante else 2 if sets_local>0 else 1
        puntos_visitante = 3 if sets_visitante>sets_local else 2 if sets_visitante>0 else 1

        # Actualizar estadísticas del local
        df_clasificacion.loc[df_clasificacion['Jugador'] == local, ['P.J', 'P.G', 'P.P', 'S.G', 'S.P', 'J.G', 'J.P', 'Puntos']] += [
            1,
            1 if puntos_local>puntos_visitante else 0,
            1 if puntos_local<puntos_visitante else 0,
            sets_local,
            sets_visitante,
            juegos_local,
            juegos_visitante,
            puntos_local
        ]

        # Actualizar estadísticas del visitante
        df_clasificacion.loc[df_clasificacion['Jugador'] == visitante, ['P.J',  'P.G', 'P.P', 'S.G', 'S.P', 'J.G', 'J.P', 'Puntos']] += [
            1,
            1 if puntos_visitante>puntos_local else 0,
            1 if puntos_visitante<puntos_local else 0,
            sets_visitante,
            sets_local,
            juegos_visitante,
            juegos_local,
            puntos_visitante
        ]

    # Calcular la diferencia de juegos
    df_clasificacion['D.J'] = df_clasificacion['J.G'] - df_clasificacion['J.P']
    # Ordenar la clasificación
    df_clasificacion.sort_values(by=['Puntos', 'D.J', 'S.G'], ascending=[False, False, False], inplace=True)
    df_clasificacion.reset_index(drop=True, inplace=True)

    return df_clasificacion

def generar_cuadro_enfrentamientos(df_partidos):
    def resultado_contrario(set):
        if '-' in set:
            puntos = set.split('-')
            return f'{puntos[1]}-{puntos[0]}'
        else:
            return set
    
    """Genera un cuadro de enfrentamientos basado en los partidos jugados."""
    jugadores = set(df_partidos['local']).union(set(df_partidos['visitante']))
    jugadores.discard('Descansa')  # Excluir 'Descansa'
    jugadores.discard('Bye')       # Excluir 'Bye'
    jugadores = sorted(jugadores)  # Ordenar alfabéticamente para consistencia

    # Crear un DataFrame vacío para la matriz de enfrentamientos
    cuadro = pd.DataFrame('', index=jugadores, columns=jugadores)

    # Marcar la diagonal con una clase CSS
    for jugador in jugadores:
        cuadro.at[jugador, jugador] = '<span class="diagonal-content"></span>'

    # Rellenar resultados en el cuadro
    for _, partido in df_partidos.iterrows():
        local = partido['local']
        visitante = partido['visitante']

        # Validar que "local" y "visitante" no sean "Descansa" ni "Bye"
        if local in ['Descansa', 'Bye'] or visitante in ['Descansa', 'Bye']:
            continue

        sets = sorted([key for key in partido.keys() if 'set' in key])+['tie']
        resultado = '<br>'.join([partido[set] for set in sets])
        resultado_visitante ='<br>'.join([resultado_contrario(partido[set]) for set in sets])
        if local != visitante:  # Evitar sobrescribir la diagonal
            cuadro.at[local, visitante] = resultado
            cuadro.at[visitante, local] = resultado_visitante

    # Renderizar la tabla con atributos CSS y permitir HTML en celdas
    return cuadro.style.set_table_attributes('class="table matches"').set_td_classes(
        pd.DataFrame(
            data=np.where(cuadro.index.values[:, None] == cuadro.columns.values[None, :], "diagonal", ""),
            index=cuadro.index,
            columns=cuadro.columns,
        )
    ).to_html(escape=False)

def generar_tabla_calendario(df_partidos):
    """Genera una tabla HTML para el calendario, con estilos para jornadas pares e impares."""
    tabla_html = '<table class="calendar-table">'
    tabla_html += '<thead><tr><th>Jornada</th><th>Fecha</th><th>Local</th><th>Visitante</th></tr></thead>'
    tabla_html += '<tbody>'
    
    for _, partido in df_partidos.iterrows():
        try:
            jornada = int(partido["jornada"])  # Asegúrate de que "jornada" sea un número entero
            clase = "jornada-par" if jornada % 2 == 0 else "jornada-impar"
            tabla_html += f'<tr class="{clase}">'
            tabla_html += f'<td>{jornada}</td>'
            tabla_html += f'<td>{partido["fecha"]}</td>'
            tabla_html += f'<td>{partido["local"]}</td>'
            tabla_html += f'<td>{partido["visitante"]}</td>'
            tabla_html += '</tr>'
        except ValueError:
            print(f"Error: El valor de 'jornada' no es un entero: {partido['jornada']}")
    
    tabla_html += '</tbody></table>'
    return tabla_html

def mostrar_tablas():
    """Renderiza las tablas de clasificación y cuadros de enfrentamientos desde los JSON en la carpeta data."""
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    tablas = {}
    cuadros = {}
    calendarios = {}

    # Obtener archivos JSON y ordenarlos numéricamente según el prefijo del nombre
    archivos_json = sorted(
        [f for f in os.listdir(data_dir) if f.endswith('.json')],
        key=lambda x: int(x.split('_')[0])  # Extraer y convertir el número inicial a entero
    )

    for filename in archivos_json:
        filepath = os.path.join(data_dir, filename)
        df_partidos, df_clasificacion = inicializar_datos(filepath)
        df_clasificacion = actualizar_clasificacion(df_partidos, df_clasificacion)
        cuadro_enfrentamientos = generar_cuadro_enfrentamientos(df_partidos)

        # Añadir columna "Posición" antes de exportar
        df_clasificacion.insert(0, 'Posición', range(1, len(df_clasificacion) + 1))

        # Generar calendario de partidos
        calendario = generar_tabla_calendario(df_partidos)

        # Extraer el nombre de la división eliminando el prefijo numérico
        nombre_division = "_".join(filename.split('_')[1:]).replace('.json', '')

        # Añadir las tablas generadas al contexto
        tablas[nombre_division] = df_clasificacion.to_html(
            index=False, classes='table classification'
        )
        cuadros[nombre_division] = cuadro_enfrentamientos
        calendarios[nombre_division] = calendario

    loader = jj.FileSystemLoader('.')
    env = jj.Environment(loader=loader)
    template = env.get_template('tablas.html')
    web = template.render(tablas=tablas, cuadros=cuadros, calendarios=calendarios)
    with open('docs/index.html', 'w') as f:
        f.write(web)
    print('[Debug] >>>Web:')
    print(web)
    print('[Debug] <<<Web:')
    #return render_template('tablas.html', tablas=tablas, cuadros=cuadros, calendarios=calendarios)

if __name__ == '__main__':
    mostrar_tablas()
