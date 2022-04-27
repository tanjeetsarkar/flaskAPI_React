import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/'

def get_info(topic):
    response = requests.get(f'{URL}{topic}')
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    paras = soup.find_all('p')
    try:
        return {
            "message" : 'success',
            "details": f'{paras[1].text} {paras[2].text}'
        }
    except Exception as e:
        return {
            "message": 'error',
            "details": e
        }

if __name__ == "__main__":
    print(get_info('bahamas'))