try:
  import requests as r
  import ipaddress, sys, os
  from os import system as s
  import time
  from datetime import datetime
  from requests.exceptions import Timeout
except ModuleNotFoundError:
  print('\npip install -r req.txt\n')

s('clear')
cg='\033[92m'
cp='\033[35m'
clb='\033[94m'
cb='\033[34m'
k='\033[0m'
clr='\033[91m'
ver = '@Ver 1.1 LTS'
aaa = datetime.now().strftime(' %d/%m/%y')

print(f'''
       uuuuuuu
       uu$$$$$$$$$$$uu
    uu$$$$$$$$$$$$$$$$$uu
   u$$$$${clr} COOL-CODER {k}$$$$u
  u$$$$$$$$$$$$$$$$$$$$$$$u
 u$$${cg} IP RANGE SCANNER {k}$$$$u
 u$$$$$$$$$$$$$$$$$$$$$$$$$u
 u$$$$$$"   "$$$"   "$$$$$$u
  "$$$$"      u$u       $$$$"
   $$$u       u$u       u$$$
   $$$u      u$$$u      u$$$
    "$$$$uu$$$   $$$uu$$$$"
     "$$$$$$$"   "$$$$$$$"
       u$$$$$$$u$$$$$$$u
        u$"$"$"$"$"$"$u
uuu     $$u$ $ $ $ $u$$     uuu
u$$$$    $$$$$u$u$u$$$     u$$$$
 $$$$$uu  "$$$$$$$$$"   uu$$$$$$
u$$$$$$$$$$$uu    """""  $$$$$$$$
$$$$"""$$$$$$$$$$uuu   uu$$$$$$$"
 """      ""$$$$$$$$$$$uu ""$"""
           uuuu ""$$$$$$$$$$uuu
u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$
$$$$$$$$$$""""         ""$$$$$$$$$$$"
 "$$$$$"                    ""$$$$"
   $$$"                       $$$$"
                {cb}@Ver {ver}{k}
___________________________________________________
  Noob       |  sem dinheiro    |  Plataforma  |  Data
———————————————|—————————————|————————————|———————————
{clr}「Sofre」{k} |  @Denny_a_gvo |  Telegram  |{aaa}
''')

print(f'{clb}[ {cp}obs {clb}]{k} A conexão de dados fornece resultados mais precisos\n')

# Perguntar se vai ser input manual ou de arquivo
opt = input(f'{clb}[{cp}1{clb}]{k} Input manual\n{clb}[{cp}2{clb}]{k} Ler IPs de arquivo .txt\n{cg}|\n└──{k}Escolha ~{cg}#{k} ')

targets = []

if opt == '1':
  user_input = input(f'{clb}[ {cp}obs {clb}]{k} Digite IP, range ou domínio (ex: 192.168.0.1 ou 192.168.0.0/24)\n{cg}|\n└──{k}Entrada ~{cg}#{k} ')
  targets.append(user_input.strip())

elif opt == '2':
  file_path = input(f'{clb}[ {cp}obs {clb}]{k} Digite o nome do arquivo .txt (ex: lista.txt): ')
  if not os.path.isfile(file_path):
    print(f'{clr}Arquivo não encontrado!{k}')
    sys.exit(1)

  with open(file_path, 'r') as file:
    lines = file.readlines()
    targets = [line.strip() for line in lines if line.strip()]

else:
  print(f'{clr}Opção inválida.{k}')
  sys.exit(1)

total_hosts = []
for target in targets:
  try:
    if '/' in target:
      net = ipaddress.ip_network(target, strict=False)
      total_hosts.extend([str(ip) for ip in net.hosts()])
    else:
      total_hosts.append(target)
  except ValueError as e:
    print(f'{clr}Entrada inválida:{k} {target} - {e}')

print(f'\n{clb}DIGITALIZANDO{k}: {len(total_hosts)} hosts detectados\n')

strt = time.time()
c = 0
resultados_validos = []

for host in total_hosts:
  h1 = f'http://{host}'

  try:
    x = r.get(h1, timeout=5)
    x = x.status_code
    print(f'{cg}{host}{k} | vivo - status {x}')
    resultados_validos.append(f'{host} - status {x}')
    c += 1

  except Timeout:
    print(f'{clr}{host}{k} | Inacessível (Timeout)')

  except KeyboardInterrupt:
    print('\nCTRL + C detectado. Saindo ...')
    sys.exit(1)

  except Exception:
    print(f'{clr}{host}{k} | caiu')

en = time.time()
print(f'\nTempo gasto: {round(en - strt, 2)} segundos')
print(f'{cp}Hits{k}: {cg}{c}{k}/{len(total_hosts)}\n')

# Salvar os IPs válidos em arquivo
if resultados_validos:
  with open('resultados.txt', 'w') as f:
    f.write('Hosts válidos encontrados:\n')
    f.write('\n'.join(resultados_validos))
  print(f'{clb}Resultados salvos em:{k} resultados.txt\n')
else:
  print(f'{clr}Nenhum host válido encontrado. Nada salvo.{k}')