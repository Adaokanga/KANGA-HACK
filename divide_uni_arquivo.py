import os

# Códigos ANSI para cores no terminal
GREEN = "\033[92m"
RESET = "\033[0m"

def dividir_arquivo(nome_arquivo):
    """Divide um arquivo .txt em dois arquivos menores."""
    if not os.path.isfile(nome_arquivo):
        print("Arquivo não encontrado.")
        return

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    meio = len(linhas) // 2
    parte1 = nome_arquivo.replace(".txt", "_parte1.txt")
    parte2 = nome_arquivo.replace(".txt", "_parte2.txt")

    with open(parte1, "w", encoding="utf-8") as p1:
        p1.writelines(linhas[:meio])
    
    with open(parte2, "w", encoding="utf-8") as p2:
        p2.writelines(linhas[meio:])

    print(f"{GREEN}Arquivo dividido com sucesso!{RESET}")
    print(f"Parte 1: {parte1}")
    print(f"Parte 2: {parte2}")

def unir_arquivos():
    """Une dois arquivos .txt informados pelo usuário."""
    arquivo1 = input("Digite o nome do primeiro arquivo: ").strip()
    arquivo2 = input("Digite o nome do segundo arquivo: ").strip()

    if not os.path.isfile(arquivo1) or not os.path.isfile(arquivo2):
        print("Um ou ambos os arquivos não foram encontrados.")
        return

    nome_saida = "arquivo_unido.txt"

    with open(nome_saida, "w", encoding="utf-8") as arquivo_saida:
        with open(arquivo1, "r", encoding="utf-8") as p1:
            arquivo_saida.writelines(p1.readlines())

        with open(arquivo2, "r", encoding="utf-8") as p2:
            arquivo_saida.writelines(p2.readlines())

    print(f"{GREEN}Arquivos unidos com sucesso!{RESET}")
    print(f"Arquivo final: {nome_saida}")

# Menu principal
print(f"{GREEN}Bem-vindo ao divisor/unidor de arquivos TXT!{RESET}")
print("Escolha uma opção:")
print("[1] Dividir arquivo")
print("[2] Unir arquivos")
opcao = input("Opção: ").strip()

if opcao == "1":
    nome_arquivo = input("Digite o nome do arquivo a ser dividido: ").strip()
    dividir_arquivo(nome_arquivo)
elif opcao == "2":
    unir_arquivos()
else:
    print("Opção inválida.")
        
