import os

# Códigos ANSI para cores no terminal
GREEN = "\033[92m"
ORANGE = "\033[38;5;214m"  # Código ANSI para laranja
RESET = "\033[0m"

def exibir_matriz_laranja():
    """Exibe a matriz 'KANGA' na cor laranja."""
    matriz = f"""
{ORANGE}██╗  ██╗ █████╗ ███╗   ██╗  ██████╗  █████╗     
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

       Powered by Python{RESET}
    """
    print(matriz)

def unir_hosts(nome_arquivo, delimitador):
    """Une hosts ou IPs de um arquivo com o delimitador escolhido e salva em um novo arquivo."""
    if not os.path.isfile(nome_arquivo):
        print("Arquivo não encontrado.")
        return

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = [linha.strip() for linha in arquivo if linha.strip()]  # Remove linhas vazias

    if not linhas:
        print("O arquivo está vazio ou não contém dados válidos.")
        return

    resultado = delimitador.join(linhas)
    nome_saida = f"{nome_arquivo}_unido.txt"

    with open(nome_saida, "w", encoding="utf-8") as arquivo_saida:
        arquivo_saida.write(resultado)

    print(f"{GREEN}Hosts/IPs unidos com sucesso!{RESET}")
    print(f"Arquivo salvo como: {nome_saida}")

# Executa a matriz antes de exibir o menu
exibir_matriz_laranja()

# Menu principal
print(f"{GREEN}Bem-vindo ao unidor de Hosts/IPs!{RESET}")
nome_arquivo = input("Digite o nome do arquivo (com extensão .txt): ").strip()

print("Escolha um delimitador:")
print("[1] # (Exemplo: exemplo.com#exemplo2.com)")
print("[2] @ (Exemplo: exemplo.com@exemplo2.com)")
print("[3] ; (Exemplo: exemplo.com;exemplo2.com)")
opcao = input("Opção: ").strip()

delimitadores = {"1": "#", "2": "@", "3": ";"}
delimitador = delimitadores.get(opcao)

if delimitador:
    unir_hosts(nome_arquivo, delimitador)
else:
    print("Opção inválida.")
