import json
import jinja2 as jj

def prepare_data():
  with open("data/playoffs.json") as f:
    playoffs = json.load(f)
  
  out = []
  for group in playoffs :
    len0 = len(group['ronda1']['partidos'])
    nCols = len0*2*2 - 1
    rondas = sorted(v for v in group if v.startswith('ronda'))+['final']
    nRows = len(rondas)+1
    
    headers = [ronda+'<br>'+group[ronda]['fecha'] for ronda in rondas]+['']
    tabla_rondas = []
    for _ in range(nRows):
      tabla_rondas.append([('','') for _ in range(nCols)])
    print(len(tabla_rondas), len(tabla_rondas[0]))
    
    for r,ronda in enumerate(rondas):
      for i,partido in enumerate(group[ronda]['partidos']):
        lenN = len(group[ronda]['partidos'])
        k = int(len0/lenN)*4
        o = int(k/4)-1 if r>0 else 0
        c1 = int(o+i*k)
        c2 = int(c1+k/2)
        c3  =int(c1+k/4+1)
        print('r1',r,c1,c2,c3)
        for v in range(c1+1,c2):
          tabla_rondas[r][v]=(tabla_rondas[r][v][0],'class="playoff_match"')
        tabla_rondas[r][c1]=(partido['jugador1'],'class="playoff_player1"')
        tabla_rondas[r][c2]=(partido['jugador2'],'class="playoff_player2"')
        tabla_rondas[r+1][c3]=(partido['resultado'],'class="playoff_result"')
    tabla_rondas[-1][int(nCols/2)]=(group['ganador'],'class="playoff_player1"')
    tabla_rondas[-1][int(nCols/2+1)]=(group['final']['partidos'][0]['resultado'],'class="playoff_result"')
    
    headers34 =['' for _ in headers]
    headers34[-2]='3er y 4to<br>'+group['final34']['fecha']
    tabla_rondas34=[]
    for _ in range(nRows):
      tabla_rondas34.append([('','') for _ in range(4)])
    tabla_rondas34[-2][0]=(group['final34']['partidos'][0]['jugador1'],'class="playoff_player1"')
    tabla_rondas34[-2][1]=('','class="playoff_match"')
    tabla_rondas34[-2][2]=(group['final34']['partidos'][0]['jugador2'],'class="playoff_player2"')
    tabla_rondas34[-1][1]=(group['ganador34'],'class="playoff_player1"')
    tabla_rondas34[-1][2]=(group['final34']['partidos'][0]['resultado'],'class="playoff_result"')
    
    tabla_html=[]
    tabla_html.append('<table class="playoff_table">')
    tabla_html.append('<tr class="playoff_header">')
    tabla_html+=['<th>'+header+'</th>' for header in headers]
    tabla_html.append('</tr>')
    for j,c in enumerate(tabla_rondas[0]):
      tabla_html.append('<tr>')
      for i,r in enumerate(tabla_rondas):
        tabla_html.append('<td '+tabla_rondas[i][j][1]+'>'+tabla_rondas[i][j][0]+'</td>')
      tabla_html.append('</tr>')
    tabla_html.append('<tr class="playoff_header">')
    tabla_html+=['<th>'+header+'</th>' for header in headers34]
    tabla_html.append('</tr>')
    for j,c in enumerate(tabla_rondas34[0]):
      tabla_html.append('<tr>')
      for i,r in enumerate(tabla_rondas34):
        tabla_html.append('<td '+tabla_rondas34[i][j][1]+'>'+tabla_rondas34[i][j][0]+'</td>')
      tabla_html.append('</tr>')
    tabla_html.append('</table>')
  
    out.append({
      'name':group['categoria'],
      'tabla':'\n'.join(tabla_html)
    })

  #print('\n'.join(tabla_html))
  return out

def generate_playoffs():
    playoffs = prepare_data()
  
    loader = jj.FileSystemLoader('.')
    env = jj.Environment(loader=loader)
    template = env.get_template('playoffs.html.jinja')
    web = template.render(playoffs=playoffs)
    with open('docs/playoffs.html', 'w') as f:
        f.write(web)
    print('[Debug] >>>Web Playoffs:')
    print(web)
    print('[Debug] <<<Web Playoffs:')
