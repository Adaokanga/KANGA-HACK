import socket

# Cores ANSI para terminal
azul = "\033[34m"
verde = "\033[32m"
vermelho = "\033[31m"
reset = "\033[0m"

def exibir_matriz():
    matriz = f"""
{azul}██╗  ██╗ █████╗ ███╗   ██╗  ██████╗  █████╗     
██║ ██╔╝██╔══██╗████╗  ██║ ██╔════╝ ██╔══██╗    
█████╔╝ ███████║██╔██╗ ██║ ██║  ███╗███████║    
██╔═██╗ ██╔══██║██║╚██╗██║ ██║   ██║██╔══██║    
██║  ██╗██║  ██║██║ ╚████║ ╚██████╔╝██║  ██║    
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═════╝ ╚═╝  ╚═╝    
                                            
       Powered by Python{reset}
    """
    print(matriz)

def resolver_ips(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, 'r') as file:
            ips = file.readlines()
        
        dominios = set()  # Usamos um conjunto para evitar duplicatas
        
        for ip in ips:
            ip = ip.strip()
            if ip:
                try:
                    dominio = socket.gethostbyaddr(ip)[0]
                    dominios.add(dominio)
                    print(f"{verde}[✔] {ip} -> {dominio}{reset}")
                except socket.herror:
                    print(f"{vermelho}[✖] {ip} -> Não foi possível resolver{reset}")
        
        # Salvar apenas os domínios positivos ordenados
        with open(arquivo_saida, 'w') as output_file:
            for dominio in sorted(dominios):
                output_file.write(f"{dominio}\n")
        
        print(f"\n{verde}[✔] Resultados salvos em: {arquivo_saida}{reset}")
    
    except FileNotFoundError:
        print(f"{vermelho}[!] Arquivo '{arquivo_entrada}' não encontrado!{reset}")

if __name__ == "__main__":
    exibir_matriz()  # Exibe a matriz antes de solicitar o arquivo
    arquivo_entrada = input("Digite o nome do arquivo de entrada (com IPs): ").strip()
    arquivo_saida = "dominios.txt"  # Arquivo onde serão salvos os resultados
    resolver_ips(arquivo_entrada, arquivo_saida)
