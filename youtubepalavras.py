import requests
from bs4 import BeautifulSoup

def coletar_ocorrencias_youtube(channel_id, palavra_chave):
    url_rss = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    resposta = requests.get(url_rss, headers={"User-Agent": "Mozilla/5.0"})
    
    if resposta.status_code != 200:
        return f"Erro ao acessar o feed RSS do canal: {resposta.status_code}"
    
    pagina = BeautifulSoup(resposta.text, "xml")
    videos = pagina.find_all("entry")
    
    ocorrencias = 0
    for video in videos:
        titulo = video.find("title").text if video.find("title") else ""
        descricao = video.find("media:description").text if video.find("media:description") else ""
        
        ocorrencias += titulo.lower().count(palavra_chave.lower())
        ocorrencias += descricao.lower().count(palavra_chave.lower())
    
    return f'A palavra "{palavra_chave}" aparece {ocorrencias} vezes nos títulos e descrições dos vídeos do canal.'

# Exemplo de uso
channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"  # Exemplo: canal do Google Developers
palavra = "AI"

resultado = coletar_ocorrencias_youtube(channel_id, palavra)
print(resultado)
