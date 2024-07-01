import requests

# Estrutura do dicionário com nome e CEP de cada integrante
squad = [
    {"nome": "Dione Braga", "cep": "11630141"},
    {"nome": "Diony Costa", "cep": "11633422"},
   
]

def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Consultar e imprimir nome e cidade de cada integrante
for integrante in squad:
    dados = consultar_cep(integrante["cep"])
    if dados:
        print(f'Nome: {integrante["nome"]}, Cidade: {dados["localidade"]}')
    else:
        print(f'Erro ao consultar CEP de {integrante["nome"]}')

