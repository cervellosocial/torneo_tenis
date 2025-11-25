from glob import glob
import torneo_clasico
import torneo_grupos
import playoffs 


if __name__ == '__main__':

  datos_torneo1 = sorted(glob('datos/temporada25_26/torneo1/*.json'))
  torneo_grupos.generar_web('ronda1.html',datos_torneo1)

  datos_torneo2 = sorted(glob('datos/temporada25_26/torneo2/*.json'))
  torneo_grupos.generar_web('ronda2.html', datos_torneo2)

  datos_infantil = ['datos/temporada25_26/division_infantil.json']
  torneo_clasico.generar_web('infantil.html', datos_infantil,)

  datos_playoffs = 'datos/temporada25_26/playoffs.json'
  playoffs.generar_web('playoffs.html', datos_playoffs)
