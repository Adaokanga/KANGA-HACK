import re
import os

# Função para exibir um cabeçalho com cor magenta
def exibir_cabecalho():
    magenta = "\033[35m"
    reset = "\033[0m"
    print(f"""
{magenta}██╗██████╗      █████╗ ██████╗ ███████╗
██║██╔══██╗    ██╔══██╗██╔══██╗██╔════╝
██║██████╔╝    ███████║██████╔╝███████╗
██║██╔═══╝     ██╔══██║██╔═══╝ ╚════██║
██║██║         ██║  ██║██║     ███████║
╚═╝╚═╝         ╚═╝  ╚═╝╚═╝     ╚══════╝
       Extrator de IPs e Hosts - KANGA{reset}
    """)

# Expressões Regulares para IPs e Hosts
regex_ipv4 = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
regex_ipv6 = r'\b(?:[a-fA-F0-9:]+:+)+[a-fA-F0-9]+\b'
regex_hosts = r'\b[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

# Função para extrair padrões do texto
def extrair_padroes(conteudo, padrao):
    return re.findall(padrao, conteudo)

# Função principal
def main():
    exibir_cabecalho()

    roxo = "\033[34m"  # Cor roxa
    reset = "\033[0m"

    # Solicita o arquivo ao usuário
    while True:
        arquivo_entrada = input(f"{roxo}Digite o nome do arquivo de entrada (ex: input.txt): {reset}").strip()
        if os.path.exists(arquivo_entrada):
            break
        else:
            print("[✘] Arquivo não encontrado. Tente novamente.")

    # Lê o conteúdo do arquivo
    with open(arquivo_entrada, "r") as file:
        conteudo = file.read()

    # Extrai os padrões
    print(f"{roxo}[...] Extraindo IPv4...{reset}")
    ips_v4 = extrair_padroes(conteudo, regex_ipv4)

    print(f"{roxo}[...] Extraindo IPv6...{reset}")
    ips_v6 = extrair_padroes(conteudo, regex_ipv6)

    print(f"{roxo}[...] Extraindo Hosts...{reset}")
    hosts = extrair_padroes(conteudo, regex_hosts)

    # Combina todos os resultados, sem remover duplicados
    todos_resultados = ips_v4 + ips_v6 + hosts

    # Salva os resultados em um único arquivo
    if todos_resultados:
        nome_arquivo_saida = "resultado_extracao.txt"
        with open(nome_arquivo_saida, "w") as file:
            file.write("\n".join(todos_resultados))
        print(f"{roxo}[✔] {len(todos_resultados)} IPs e Hosts salvos em '{nome_arquivo_saida}'.{reset}")
    else:
        print(f"{roxo}[✘] Nenhum IP ou host foi encontrado no arquivo.{reset}")

if __name__ == "__main__":
    main()
    
