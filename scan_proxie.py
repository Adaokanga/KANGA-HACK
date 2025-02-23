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
  Expansão de Intervalos IP - Powered by Denny-a Gvo{reset}
    """)

def expandir_intervalo(ip_inicial, ip_final):
    """Expande um intervalo de IPs na forma X.X.X.X - Y.Y.Y.Y."""
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

def salvar_em_arquivo(lista, nome_arquivo):
    """Salva uma lista de IPs em um arquivo."""
    with open(nome_arquivo, "w") as file:
        file.write("\n".join(lista))
    print(f"[✔] Intervalo expandido salvo em '{nome_arquivo}'.")

def main():
    exibir_cabecalho()

    while True:
        print("\nSelecione uma opção:")
        print("[1] Expandir intervalo de IP (exemplo: 127.0.0.0-127.255.255.255)")
        print("[2] Sair")
        opcao = input("Sua escolha: ").strip()

        if opcao == "1":
            intervalo = input("Digite o intervalo de IP (exemplo: 127.0.0.0-127.255.255.255): ").strip()
            try:
                ip_inicial, ip_final = intervalo.split("-")
                ip_inicial = ip_inicial.strip()
                ip_final = ip_final.strip()

                ips_expandidos = expandir_intervalo(ip_inicial, ip_final)
                if ips_expandidos:
                    print(f"\n{len(ips_expandidos)} IPs encontrados no intervalo:")
                    for ip in ips_expandidos[:10]:  # Exibir os 10 primeiros IPs como exemplo
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
            print("Saindo...")
            break
        else:
            print("[✘] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
