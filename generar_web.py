from glob import glob
import torneo_clasico
import torneo_grupos
from playoffs import generate_playoffs


if __name__ == '__main__':

  datos_torneo1 = sorted(glob('datos/temporada25_26/torneo1/*.json'))
  torneo_grupos.generar_torneos(datos_torneo1,'torneo1.html')

  datos_torneo2 = sorted(glob('datos/temporada25_26/torneo2/*.json'))
  torneo_grupos.generar_torneos(datos_torneo2,'torneo2.html')

  datos_infantil = ['datos/temporada25_26/division_infantil.json']
  torneo_clasico.generar_torneos(datos_infantil,'infantil.html')

  datos_playoffs = 'datos/temporada25_26/playoffs.json'
  generate_playoffs(datos_playoffs, 'playoffs.html')
