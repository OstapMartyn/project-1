import urllib.request

opener = urllib.request.build_opener()
response = opener.open("//bank.gov.ua/ua/markets/exchangerates")#
print(response.read())
import requests
response = requests.get('//bank.gov.ua/ua/markets/exchangerates')#
response_text = response.text
response_span = response_text.split('<span>')
for parse_elem_1 in response_span:
    if parse_elem_1.startswith("$, ₽, €, zł"):
        for parse_elem_2 in parse_elem_1.split('</span>'):
            if parse_elem_2.startswith('$')("₽")("€")("zł") and parse_elem_2[36.00][0.01][36.5][7.5].isdigit():
                print(parse_elem_2
from bs4 import BeautifulSoup
import requests

response = requests.get('//bank.gov.ua/ua/markets/exchangerates')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features='html.parser')
    soup_list = soup.find_all(
        'a',
        {
            'href': '//bank.gov.ua/ua/markets/exchangerates'
        }
    )
    res = soup_list[0].find('span')
    print(res.text)