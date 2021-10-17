import requests
from bs4 import BeautifulSoup

def crawNewsData(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    products = soup.findAll(class_='product')
    data = []
    for product in products:
        image = 'https://vuoncayviet.com' + product.find(class_='pic-news').find("a").find("img").attrs["src"][2:]
        name = product.find("h3").find("a").text
        # price = int(product.find(class_='price-product').text.replace(",", "").split()[0])
        price = product.find(class_='price-product').text
        data.append({
            "TreeName": name,
            "TreeImage": image,
            "TreePrice": price,
        })
    return data
# print(crawNewsData("https://vuoncayviet.com"))
