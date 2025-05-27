import ipaddress

def exibir_cabecalho():
    roxo = "\033[35m"
    reset = "\033[0m"
    print(f"""
{roxo}███╗   ███╗ █████╗ ██████╗  ██████╗██╗██████╗ 
████╗ ████║██╔══██╗██╔══██╗██╔════╝██║██╔══██╗
██╔████╔██║███████║██████╔╝██║     ██║██████╔╝
██║╚██╔╝██║██╔══██║██╔═══╝ ██║     ██║██╔═══╝ 
██║ ╚═╝ ██║██║  ██║██║     ╚██████╗██║██║     
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝      ╚═════╝╚═╝╚═╝     
  Expansão de Intervalos IP - Powered by KANGA{reset}
    """)

def expandir_intervalo(ip_inicial, ip_final):
    try:
        start = int(ipaddress.IPv4Address(ip_inicial))
        end = int(ipaddress.IPv4Address(ip_final))
        if start > end:
            print("[✘] O IP inicial não pode ser maior que o IP final.")
            return None
        return [str(ipaddress.IPv4Address(ip)) for ip in range(start, end + 1)]
    except ValueError:
        print("[✘] Endereço IP inválido.")
        return None

def expandir_cidr(cidr):
    try:
        rede = ipaddress.IPv4Network(cidr.strip(), strict=False)
        return [str(ip) for ip in rede.hosts()]
    except ValueError:
        print(f"[✘] CIDR inválido: {cidr}")
        return []

def processar_arquivo_cidr(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as file:
            linhas = file.readlines()
        todos_ips = []
        for linha in linhas:
            linha = linha.strip()
            if linha:
                ips = expandir_cidr(linha)
                todos_ips.extend(ips)
        return todos_ips
    except FileNotFoundError:
        print("[✘] Arquivo não encontrado.")
        return []

def salvar_em_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, "w") as file:
        file.write("\n".join(lista))
    print(f"[✔] Intervalo expandido salvo em '{nome_arquivo}'.")

def main():
    exibir_cabecalho()

    while True:
        print("\nSelecione uma opção:")
        print("[1] Expandir intervalo de IP (exemplo: 127.0.0.0-127.255.255.255)")
        print("[2] Expandir IPs a partir de arquivo com blocos CIDR")
        print("[3] Sair")
        opcao = input("Sua escolha: ").strip()

        if opcao == "1":
            intervalo = input("Digite o intervalo de IP (exemplo: 127.0.0.0-127.255.255.255): ").strip()
            try:
                ip_inicial, ip_final = intervalo.split("-")
                ips_expandidos = expandir_intervalo(ip_inicial.strip(), ip_final.strip())
                if ips_expandidos:
                    print(f"\n{len(ips_expandidos)} IPs encontrados no intervalo:")
                    for ip in ips_expandidos[:10]:
                        print(ip)
                    if len(ips_expandidos) > 10:
                        print("...")
                    salvar = input("\nDeseja salvar os resultados em um arquivo? (s/n): ").strip().lower()
                    if salvar == "s":
                        nome_arquivo = input("Digite o nome do arquivo (ex: resultados.txt): ").strip()
                        salvar_em_arquivo(ips_expandidos, nome_arquivo)
            except ValueError:
                print("[✘] Formato inválido. Use o formato X.X.X.X-Y.Y.Y.Y.")

        elif opcao == "2":
            caminho = input("Digite o caminho do arquivo .txt com blocos CIDR: ").strip()
            ips_expandidos = processar_arquivo_cidr(caminho)
            if ips_expandidos:
                print(f"\n{len(ips_expandidos)} IPs extraídos dos blocos CIDR:")
                for ip in ips_expandidos[:10]:
                    print(ip)
                if len(ips_expandidos) > 10:
                    print("...")
                salvar = input("\nDeseja salvar os resultados em um arquivo? (s/n): ").strip().lower()
                if salvar == "s":
                    nome_arquivo = input("Digite o nome do arquivo (ex: saida_cidr.txt): ").strip()
                    salvar_em_arquivo(ips_expandidos, nome_arquivo)

        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("[✘] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()