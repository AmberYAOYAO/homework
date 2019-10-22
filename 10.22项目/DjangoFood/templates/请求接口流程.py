import requests
from lxml import etree
import random

url = "https://www.meishij.net/chufang/diy/"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}
response = requests.get(url,headers=headers)

html = etree.HTML(response.content.decode())
name = html.xpath("//strong")

url = "http://127.0.0.1:8000/foods/"
data = {"name":"酸辣土豆丝","price":"10","picture":"1.jpg","description":"土豆","type_id":"6"}