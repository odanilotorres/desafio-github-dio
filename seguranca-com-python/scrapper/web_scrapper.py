from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content
#objeto site recebendo o conteudo do site passado.

soup = BeautifulSoup(site, "html.parser")
# objeto soup baixo o html do site
#print(soup.prettify())

#print(soup.a)
#primeira tag que encontra de ancora

print(soup.p.string)

print(soup.find('admin'))
