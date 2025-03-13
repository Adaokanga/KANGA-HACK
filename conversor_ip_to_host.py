import socket

def exibir_matriz():
    # Cores ANSI para terminal
    azul = "\033[34m"
    reset = "\033[0m"
    
    matriz = f"""
{azul}██╗  ██╗ █████╗ ███╗   ██╗  ██████╗  █████╗     
██║ ██╔╝██╔══██╗████╗  ██║ ██╔════╝ ██╔══██╗    
█████╔╝ ███████║██╔██╗ ██║ ██║  ███╗███████║    
██╔═██╗ ██╔══██║██║╚██╗██║ ██║   ██║██╔══██║    
██║  ██╗██║  ██║██║ ╚████║ ╚██████╔╝██║  ██║    
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═════╝ ╚═╝  ╚═╝    
                                            
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗  █████╗     
██║ ██╔╝██╔══██╗████╗  ██║██╔════╝ ██╔══██╗    
█████╔╝ ███████║██╔██╗ ██║██║  ███╗███████║    
██╔═██╗ ██╔══██║██║╚██╗██║██║   ██║██╔══██║    
██║  ██╗██║  ██║██║ ╚████║╚██████╔╝██║  ██║    
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝    
                                            
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗  █████╗     
██║ ██╔╝██╔══██╗████╗  ██║██╔════╝ ██╔══██╗    
█████╔╝ ███████║██╔██╗ ██║██║  ███╗███████║    
██╔═██╗ ██╔══██║██║╚██╗██║██║   ██║██╔══██║    
██║  ██╗██║  ██║██║ ╚████║╚██████╔╝██║  ██║    
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝    
                                            
       Powered by Python{reset}
    """
    print(matriz)

def resolver_ips(arquivo_entrada, arquivo_saida):
    try:
        with open(arquivo_entrada, 'r') as file:
            ips = file.readlines()
        
        with open(arquivo_saida, 'w') as output_file:
            for ip in ips:
                ip = ip.strip()
                if ip:
                    try:
                        dominio = socket.gethostbyaddr(ip)[0]
                        output_file.write(f"{ip} -> {dominio}\n")
                        print(f"[✔] {ip} -> {dominio}")
                    except socket.herror:
                        output_file.write(f"{ip} -> Não foi possível resolver\n")
                        print(f"[✖] {ip} -> Não foi possível resolver")
        
        print(f"\n[✔] Resultados salvos em: {arquivo_saida}")
    
    except FileNotFoundError:
        print(f"[!] Arquivo '{arquivo_entrada}' não encontrado!")

if __name__ == "__main__":
    exibir_matriz()  # Exibe a matriz antes de solicitar o arquivo
    arquivo_entrada = input("Digite o nome do arquivo de entrada (com IPs): ").strip()
    arquivo_saida = "dominios.txt"  # Arquivo onde serão salvos os resultados
    resolver_ips(arquivo_entrada, arquivo_saida)
