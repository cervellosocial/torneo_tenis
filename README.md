# Torneos

Pagina Resultante : [https://cervellosocial.github.io/torneo_tenis/](https://cervellosocial.github.io/torneo_tenis/)

# Documentacion & Detalles

* En torneos, los jugadores con nombre `Descansa` y `Bye` se muestran en las jornadas pero se ignoran en las tablas de puntuacion
* [Distribucion de partidos para torneos](./Distribucion_de_partidos_para_torneos.md)

##Pagina de entrada & paginas estaticas

El archivo [web/index.html](web/index.html) es el puto de entrada de la web.<br>
Este archivo es manual y contiene los enlaces a las otras paginas

El resto de archivos en el directorio [web/](web/) son publicados directamente como parte de la web.<br>
Cualquier archivo .html en [web/](web/) sera una pagina web estatica. 

## Actualizar Datos 

Algunas paginas son generadas a partir de datos de partidos, con los que se crean tablas puntucion, clasificaciones, etc.<br>
El punto de entrada para la generacion de paginas es el archivo [generar_web.py](generar_web.py)

Los datos de las paginas generadas estan en el directorio [datos/](datos/)<br>
Los diferentes torneos estaran en diferentes carpetas o achivos, dependiendo de la pagina.<br>
e.g. [datos/temporada25_26/torneo1/torneo_grupo_1.json](datos/temporada25_26/torneo1/torneo_grupo_1.json)

Al modificar estos archivos la correspondiente pagina generada se actualizara automaticamente al cabo de unos minutos

## Añadir nuevas paginas generadas

En [generar_web.py](generar_web.py) se combinan listas de archivos de datos para generar diferentes paginas.<br>
Tanto los archivos de datos como las paginas son explcitas. 

e.g. - Para genera el archivo `torneo1.html` con los datos de los archivos en `datos/temporada25_26/torneo1/*.json`
``` python 
  datos_torneo1 = sorted(glob('datos/temporada25_26/torneo1/*.json'))
  torneo_grupos.generar_web('torneo1.html',datos_torneo1)
```

Si se quiere añadir una nueva pagina generada (un nuevo torneo) hay que añadir la generacion de una nueva pagina como en el ejemplo anterior; con el tipo de torneo, el nombre de la nueva pagina y la ruta a los nuevos archivos de datos.

Para que se pueda navegar hasta la pagina facilmente, tambien habra que añadirla a [web/index.html](web/index.html)




