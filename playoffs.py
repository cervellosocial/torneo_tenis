import json
import jinja2 as jj

def prepare_data():
  with open("data/playoffs.json") as f:
    playoffs = json.load(f)
  
  out = []
  for group in playoffs :
    tabla_rondas = []
    len0 = len(group['ronda1']['partidos'])
    print('len0',len0)
    rondas = sorted(v for v in group if v.startswith('ronda'))+['final']
    for j,ronda in enumerate(rondas):
      row=[['',''] for v in range(len0*4)]
      lenN = len(group[ronda]['partidos'])
      k=int(len0/lenN)*4
      o = int(k/4)-1 if j>0 else 0
      print(ronda,lenN,'k',k,'o',o)
      for i,entry in enumerate(group[ronda]['partidos']):
        for ii in range(int(k/2)):
          row[int(o+i*k+ii)]=('','class="playoff_match"')
        row[int(o+i*k)]=(entry['jugador1'],'class="playoff_player1"')
        row[int(o+i*k+k/2)]=(entry['jugador2'],'class="playoff_player2"')
        row[int(o+i*k+k/4)]=(entry['resultado'],'class="playoff_match"')
      tabla_rondas.append(row)
  
    row=[['',''] for v in range(len0*4)]
    row[len0*2-1] = (group['ganador'],'class="playoff_player1"')
    tabla_rondas.append(row)
  
    headers = [group[ronda]['fecha'] for ronda in rondas]
  
    tabla_html=[]
    tabla_html.append('<table class="playoff_table">')
    tabla_html.append('<tr class="playoff_header">')
    tabla_html+=['<th>'+header+'</th>' for header in headers]
    tabla_html.append('<th></th>')
    tabla_html.append('</tr>')
    for j,c in enumerate(tabla_rondas[0]):
      tabla_html.append('<tr>')
      for i,r in enumerate(tabla_rondas):
        tabla_html.append('<td '+tabla_rondas[i][j][1]+'>'+tabla_rondas[i][j][0]+'</td>')
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
    with open('docs/playoffs_beta.html', 'w') as f:
        f.write(web)
    print('[Debug] >>>Web Playoffs:')
    print(web)
    print('[Debug] <<<Web Playoffs:')
