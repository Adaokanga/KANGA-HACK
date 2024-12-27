import requests
import json

# Função para exibir a matriz personalizada
def exibir_matriz():
    # Matriz personalizada com cor roxa
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

# Função principal para listar subdomínios
def main():
    exibir_matriz()  # Exibir a matriz personalizada

    # Solicitar o domínio ao usuário
    dominio = input("Digite o domínio: ")

    # URL da API e cabeçalhos
    url = f'https://api.securitytrails.com/v1/domain/{dominio}/subdomains?children_only=false&include_inactive=true'
    headers = {
        'APIKEY': '5qynVQOxn612qWJBKo52m8zDWwgESdso',  # API Key fornecida
        'accept': 'application/json'
    }

    # Requisição à API
    response = requests.get(url, headers=headers)

    # Verificar a resposta
    if response.status_code == 200:
        data = response.json()
        
        if 'subdomains' in data:
            subdomains = data['subdomains']

            # Salvar subdomínios em um arquivo
            with open('subdominios.txt', 'w') as file:
                for subdomain in subdomains:
                    print(f'{subdomain}.{dominio}')
                    file.write(f'{subdomain}.{dominio}\n')

            print(f"\n[✔] Subdomínios salvos em 'subdominios.txt' com sucesso para o domínio {dominio}!")
        else:
            print("\n[✘] Não foram encontrados subdomínios na resposta.")
    else:
        print(f"\n[✘] Erro ao realizar a requisição: {response.status_code}")

if __name__ == "__main__":
    main()

