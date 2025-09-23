# torneo-tenis
Web estática para mostrar la clasificación del torneo de tenis.

Para actualizar la pagina con nuevos resultados, simplemente editar los diferentes archivos en [data](./data) y pulsar `Commit changes`

Pagina : [https://cervellosocial.github.io/torneo_tenis/](https://cervellosocial.github.io/torneo_tenis/)

---
# Guia para distribucion de partidos en torneo normal -todos contra todos-
## Numero de partidos
 | Jugadores | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12|
 | - | - | - | - | - | - | - | - | - | - | - | - | 
 | #Partidos | 1 | 3 | 6 | 10 | 15 | 21 | 28 | 36 | 45 | +10 | +11 | 
 |  | j1-j2 | j1-j3 | j1-j4 | j1-j5 | j1-j6 | j1-j7 | j1-j8 | 
 |  |       | j2-j3 | j2-j4 | j2-j5 | j2-j6 | j2-j7 | j2-j8 | 
 |  |       |       | j3-j4 | j3-j5 | j3-j6 | j3-j7 | j3-j8 | 
 |  |       |       |       | j4-j5 | j4-j6 | j4-j7 | j4-j8 | 
 |  |       |       |       |       | j5-j6 | j5-j7 | j5-j8 | 
 |  |       |       |       |       |       | j6-j7 | j6-j8 | 
 |  |       |       |       |       |       |       | j7-j8 | 

## Distribucion de partidos y jornadas
Para 1 partido por jugador por jornada:
* 4 jugadores = 3 jornadas con 3 partidos por jornada
* 5 jugadores = 4 jornadas con 3 partidos por jornada
* 6 jugadores = 5 jornadas con 3 partidos por jornada
* 7 jugadores = 6 jornadas con 4 partidos por jornada
* 8 jugadores = 7 jornadas con 4 partidos por jornada
* ...
## Distribucion uniforme de partidos en jornadas
Regla para la tabla : Se empieza con el jugador de indice mas bajo que no haya jugado en la jornada y se anade un partido no jugado con el siguiente jugador de indice mas bajo
Para 8 jugadores
 | Jornada |  |  |  |  | 
 | - | - | - | - | - | 
 | 1 | j1-j2 | j3-j4 | j5-j6 | j7-j8 | 
 | 2 | j1-j3 | j2-j4 | j5-j7 | j6-j8 | 
 | 3 | j1-j4 | j2-j3 | j5-j8 | j6-j7 | 
 | 4 | j1-j5 | j2-j6 | j3-j7 | j4-j8 | 
 | 5 | j1-j6 | j2-j5 | j3-j8 | j4-j7 | 
 | 6 | j1-j7 | j2-j8 | j3-j5 | j4-j6 |  
 | 7 | j1-j8 | j2-j7 | j3-j6 | j4-j5 | 

