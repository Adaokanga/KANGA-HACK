import http.client
import threading
import time
import pyfiglet
import rich
from rich.console import Console
from collections import defaultdict, deque
import os

# Função para exibir a matriz personalizada
def exibir_matriz():
    roxo = "\033[35m"
    reset = "\033[0m"
    matriz = f"""
{roxo}██╗  ██╗ █████╗ ███╗   ██╗ ██████╗  █████╗     
██║ ██╔╝██╔══██╗████╗  ██║██╔════╝ ██╔══██╗    
█████╔╝ ███████║██╔██╗ ██║██║  ███╗███████║    
██╔═██╗ ██╔══██║██║╚██╗██║██║   ██║██╔══██║    
██║  ██╗██║  ██║██║ ╚████║╚██████╔╝██║  ██║    
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝    
       Kanga Hack - Powered by Python{reset}
    """
    print(matriz)

# Exibe a matriz no início
exibir_matriz()

# Exibe os banners do scanner
esp = ' '
banner1 = pyfiglet.figlet_format(f'{esp*4}S c a n', font='slant')
banner2 = pyfiglet.figlet_format(f'{esp*5}F l a r e', font='slant')
banner3 = pyfiglet.figlet_format(f'{esp*5}F r o n t', font='slant')
rich.print(f'[magenta]{banner1}[/magenta]')
rich.print(f'[magenta]{banner2}[/magenta]')
rich.print(f'[magenta]{banner3}[/magenta]')
print('\033[1;44mFeito por https://t.me/Denny_a_Gvo\033[m\n')
time.sleep(2)

# Solicita o nome do arquivo com proxies ao usuário
while True:
    try:
        arquivo_hosts = input('\033[1;34mDigite o nome do arquivo com os proxies (ex: allhosts.txt): \033[m').strip()
        if os.path.exists(arquivo_hosts):  # Verifica se o arquivo existe
            break
        else:
            print(f"\033[1;31m[Erro]\033[m O arquivo '{arquivo_hosts}' não foi encontrado. Tente novamente.")
    except KeyboardInterrupt:
        print("\n\033[1;31m[Interrompido]\033[m Saindo...")
        exit(1)

# Lê os proxies do arquivo informado pelo usuário
with open(arquivo_hosts, "r") as allhosts:
    linhas = [line.strip() for line in allhosts if line.strip()]

# Solicita o domínio do usuário
server_host = str(input('Digite seu Dominio: '))

# Solicita o nome do arquivo para salvar os resultados
while True:
    output_file = input('\033[1;34mDigite o nome do arquivo para salvar os resultados (ex: resultados.txt): \033[m').strip()
    if not output_file.endswith('.txt'):
        print("\033[1;31m[Erro]\033[m O arquivo deve ter a extensão '.txt'.")
    elif os.path.exists(output_file):
        confirmar = input(f"\033[1;33m[Aviso]\033[m O arquivo '{output_file}' já existe. Deseja sobrescrever? (s/n): ").strip().lower()
        if confirmar == 's':
            open(output_file, "w").close()  # Limpa o arquivo existente
            break
    else:
        open(output_file, "w").close()  # Cria o arquivo
        break

results_lock = threading.Lock()
print_lock = threading.Lock()

proxy_order = {proxy: {'HEAD': None, 'PATCH': None, 'PUT': None, 'DELETE': None, 'OPTIONS': None} for proxy in linhas}

console = Console()

# Função para processar cada proxy
def scan_proxy(proxy):
    proxy_host = proxy.split(':')[0]
    proxy_port = int(proxy.split(':')[1]) if ':' in proxy else 80

    success_methods = []
    failed_methods = []

    for method in ['HEAD', 'PATCH', 'PUT', 'DELETE', 'OPTIONS']:
        try:
            conn = http.client.HTTPConnection(proxy_host, proxy_port, timeout=3)
            conn.request(method, "/", headers={"Host": server_host})

            response = conn.getresponse()
            status = response.status
            status_message = f"Status {status}"
            
            result_line = f"Escaneando {method} {proxy} {status_message} Host Salvo"
            
            if status == 101 or status == 200:
                with results_lock:
                    proxy_order[proxy][method] = status_message
                    success_methods.append(method)
                    with open(output_file, "a") as file:
                        file.write(f"{method} {proxy} {status_message}\n")  # Salva diretamente no arquivo
                    with print_lock:
                        print(f"\033[1;33m{result_line}\033[m")  
            else:
                failed_methods.append(method)
        except Exception as e:
            failed_methods.append(method)

    with print_lock:
        success_str = ', '.join(success_methods) if success_methods else 'Nenhum'
        failed_str = ', '.join(failed_methods) if failed_methods else 'Nenhum'
        console.print(f"[grey60]Métodos que funcionaram para o Proxy {proxy}: {success_str}[/grey60]")
        console.print(f"[red]Métodos que falharam: {failed_str}[/red]")

def worker(proxy):
    scan_proxy(proxy)

def main():
    threads = []

    for proxy in linhas:
        thread = threading.Thread(target=worker, args=(proxy,))
        thread.start()
        threads.append(thread)
        
        if len(threads) >= 10:
            for thread in threads:
                thread.join()
            threads = []

    for thread in threads:
        thread.join()

    print(f"\033[1;32m[✔] Escaneamento finalizado. Resultados salvos em '{output_file}'.\033[m")

if __name__ == "__main__":
    main()
