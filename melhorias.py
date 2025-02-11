import requests
from bs4 import BeautifulSoup

def coletar_ocorrencias(url, palavra_chave):
    resposta = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if resposta.status_code != 200:
        return f"Erro ao acessar a página: {resposta.status_code}"
    
    pagina = BeautifulSoup(resposta.text, "html.parser")
    ocorrencias = pagina.get_text().lower().count(palavra_chave.lower())
    
    return f'A palavra "{palavra_chave}" aparece {ocorrencias} vezes no site {url}'

# Exemplo de uso
site_url = "https://news.ycombinator.com/"
palavra = "AI"

resultado = coletar_ocorrencias(site_url, palavra)
print(resultado)