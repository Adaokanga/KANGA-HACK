try:
    import requests as r
    import ipaddress, sys, os
    from os import system as s
    import time
    from datetime import datetime
    from requests.exceptions import Timeout
except ModuleNotFoundError:
    print('\nInstale os requisitos com:\n  pip install -r req.txt\n')
    sys.exit(1)

s('cls' if os.name == 'nt' else 'clear')

ver = '@Ver 1.1 LTS'
aaa = datetime.now().strftime(' %d/%m/%y')

print(f'''
       uuuuuuu
       uu$$$$$$$$$$$uu
    uu$$$$$$$$$$$$$$$$$uu
   u$$$$$ COOL-CODER $$$$u
  u$$$$$$$$$$$$$$$$$$$$$$$u
 u$$$  IP RANGE SCANNER  $$$u
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
                @Ver {ver}
___________________________________________________
  Noob       |  sem dinheiro    |  Plataforma  |  Data
-------------|------------------|--------------|------------
「Sofre」     |  @Denny_a_gvo    |  Telegram    |{aaa}
''')

print('[ obs ] A conexão de dados fornece resultados mais precisos\n')

opt = input('[1] Input manual\n[2] Ler IPs de arquivo .txt\n|\n└──Escolha ~# ')

targets = []

if opt == '1':
    user_input = input('[ obs ] Digite IP, range ou domínio (ex: 192.168.0.1 ou 192.168.0.0/24)\n|\n└──Entrada ~# ')
    targets.append(user_input.strip())

elif opt == '2':
    file_path = input('[ obs ] Digite o nome do arquivo .txt (ex: lista.txt): ')
    if not os.path.isfile(file_path):
        print('Arquivo não encontrado!')
        sys.exit(1)
    with open(file_path, 'r') as file:
        lines = file.readlines()
        targets = [line.strip() for line in lines if line.strip()]
else:
    print('Opção inválida.')
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
        print(f'Entrada inválida: {target} - {e}')

print(f'\nDIGITALIZANDO: {len(total_hosts)} hosts detectados\n')

strt = time.time()
c = 0
resultados_validos = []

for host in total_hosts:
    h1 = f'http://{host}'

    try:
        x = r.get(h1, timeout=5)
        x = x.status_code
        print(f'{host} | vivo - status {x}')
        resultados_validos.append(f'{host} - status {x}')
        c += 1

    except Timeout:
        print(f'{host} | Inacessível (Timeout)')

    except KeyboardInterrupt:
        print('\nCTRL + C detectado. Saindo ...')
        sys.exit(1)

    except Exception:
        print(f'{host} | caiu')

en = time.time()
print(f'\nTempo gasto: {round(en - strt, 2)} segundos')
print(f'Hits: {c}/{len(total_hosts)}\n')

if resultados_validos:
    with open('resultados.txt', 'w') as f:
        f.write('Hosts válidos encontrados:\n')
        f.write('\n'.join(resultados_validos))
    print('Resultados salvos em: resultados.txt\n')
else:
    print('Nenhum host válido encontrado. Nada salvo.')