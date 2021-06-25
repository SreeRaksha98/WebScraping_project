import requests
from bs4 import BeautifulSoup              # Beautifu soap : This is used to parse the content of web page

prod_list = [
    {
        "URL" : "https://www.amazon.in/Elements-Portable-External-Drive-Black/dp/B06XDKWLJH/ref=sr_1_4?dchild=1&keywords=Hard+dis&qid=1624430199&s=electronics&sr=1-4",
        "name" : "Western Digital Elements 1.5 TB Portable External Hard Drive (Black)",
        "target_price" : 5000
    },
    {
        "URL" : "https://www.amazon.in/Dell-External-Slimmest-Superfast-Platinum/dp/B07LGGMW41/ref=sr_1_2?dchild=1&keywords=Hard+disk+dell&qid=1624430342&s=electronics&sr=1-2",
        "name" : "Dell External SSD 250GB External Hard Drive- 550Mbps",
        "target_price" : 5000
    },
    {
        "URL" : "https://www.amazon.in/Samsung-10Gbps-External-Portable-MU-PC1T0H/dp/B087DF1L2J/ref=sr_1_5?dchild=1&keywords=Hard+disk+samsung&qid=1624430285&s=electronics&sr=1-5",
        "name" : "Samsung T7 1TB Up to 1,050MB/s USB 3.2 Gen 2",
        "target_price" : 10000
    },
    {
        "URL" : "https://www.amazon.in/Lenovo-Portable-External-Hard-Drive/dp/B08K7JBD76/ref=sr_1_2?dchild=1&keywords=Hard+disk+lenovo&qid=1624430262&s=electronics&sr=1-2",
        "name" : "Lenovo Portable 1TB External Hard Disk Drive HDD – USB 3.0",
        "target_price" : 4000
    },
    {
        "URL": "https://www.amazon.in/Seagate-Expansion-Portable-External-Playstation/dp/B007IREFE0/ref=sr_1_3?crid=157PD7OICKJ6H&dchild=1&keywords=hard+disk+seagate&qid=1624430724&sprefix=hard+disk+sea%2Celectronics%2C326&sr=8-3",
        "name": "Seagate Expansion 1.5 TB External HDD",
        "target_price": 4000
    }
]

def run_product_price(URL):
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }
    page = requests.get(URL, headers = headers)
    page_content = BeautifulSoup(page.content, 'html.parser')    #Web scraping using BeautifulSoup

    product_price = page_content.find(id="priceblock_ourprice")
    if product_price == None:
        product_price = page_content.find(id='priceblock_dealprice')
    return product_price.getText()

result_file = open('price.txt', 'w')   #opening the file

try:
    for i in prod_list:
        price = run_product_price(i.get("URL"))
        print(price +'--> Model -->'+ i.get('name'))

        my_prod_price = price[2:]
        my_prod_price = my_prod_price.replace(',','')
        my_prod_price = int(float(my_prod_price))

        print(my_prod_price)
        if my_prod_price <= i.get('target_price'):
            print("Available!!!! '\n' the product is :" +i.get('name')+ '\n')
            result_file.write(f"The model is {i.get('name')} and the price is {my_prod_price} \n")
        else:
            print("Not availabe!!!!!")

finally:
    result_file.close()