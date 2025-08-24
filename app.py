import torneos_clasico
import torneos_grupos
from playoffs import generate_playoffs

if __name__ == '__main__':
  torneos_grupos.generar_torneos()
  torneos_clasico.generar_torneos()
  generate_playoffs()
