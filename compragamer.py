import requests
from pprint import pprint
from bs4 import BeautifulSoup

url = 'https://compragamer.com/index.php?criterio=rx+5700+xt&seccion=3'
req = requests.get(url=url,params={
  'criterio': '5700',
  'seccion': '3'
})
soup = BeautifulSoup(req.text, 'html.parser')
items = soup.findAll('li',attrs={'class':'products__item'})
articulos = []
for item in items:
  producto = item \
    .findChild('div',attrs={'class':'products__wrap clearfix'})
  tipo_boton = producto \
    .findChild('footer',attrs={'class':'products-btns'}) \
    .findChild()
  if (tipo_boton.name == 'div'):
    continue # Si no hay stock, sigo con el proximo producto
    
  descripcion = producto \
    .findChild('h4',attrs={'class':'products__name'}) \
    .findChild('a') \
    .contents[0].strip()
  
  valor = producto \
    .findChild('div',attrs={'class':'products__inner'}) \
    .findChild('span',attrs={'class':'products__price-new'}) \
    .findChild('font') \
    .contents[0].strip()

  articulos.append((descripcion,valor)) 


pprint(articulos)