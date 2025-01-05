from flask import Flask, render_template
from primera import inicializar_datos as primera_datos, actualizar_clasificacion as primera_clasificacion
from segunda import inicializar_datos as segunda_datos, actualizar_clasificacion as segunda_clasificacion
from tercera import inicializar_datos as tercera_datos, actualizar_clasificacion as tercera_clasificacion
from infantil import inicializar_datos as infantil_datos, actualizar_clasificacion as infantil_clasificacion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/primera')
def primera():
    # Obtener datos de la primera división
    df_partidos, df_clasificacion = inicializar_datos()
    df_clasificacion = actualizar_clasificacion(df_partidos, df_clasificacion)
    # Convertir la clasificación a un diccionario para pasarlo a la plantilla
    clasificacion = df_clasificacion.to_dict(orient='records')
    return render_template('primera.html', clasificacion=clasificacion)

@app.route('/segunda')
def segunda():
    df_partidos, df_clasificacion = segunda_datos()
    df_clasificacion = segunda_clasificacion(df_partidos, df_clasificacion)
    return render_template('segunda.html', clasificacion=df_clasificacion.to_dict(orient='records'))

@app.route('/tercera')
def tercera():
    df_partidos, df_clasificacion = tercera_datos()
    df_clasificacion = tercera_clasificacion(df_partidos, df_clasificacion)
    return render_template('tercera.html', clasificacion=df_clasificacion.to_dict(orient='records'))

@app.route('/infantil')
def infantil():
    df_partidos, df_clasificacion = infantil_datos()
    df_clasificacion = infantil_clasificacion(df_partidos, df_clasificacion)
    return render_template('infantil.html', clasificacion=df_clasificacion.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
