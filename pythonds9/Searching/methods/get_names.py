import requests

def get_names():
    url = 'http://www.pas.rochester.edu/~rsarkis/csc161/_static/data/'\
            'census-dist-female-first.txt'
    text = requests.get(url).text.split('\r\n')
    return text
