import requests
from bs4 import BeautifulSoup

# Site e palavra-chave para buscar
URL = "https://news.ycombinator.com/"  # Site de notícias tech
PALAVRA_CHAVE = "AI"

# Fazer a requisição HTTP
response = requests.get(URL)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parsear o HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Contar a incidência da palavra-chave no texto da página
    ocorrencias = soup.get_text().lower().count(PALAVRA_CHAVE.lower())

    print(f'A palavra "{PALAVRA_CHAVE}" aparece {ocorrencias} vezes no site {URL}')
else:
    print(f"Erro ao acessar o site! Código de status: {response.status_code}")
