import requests

def count_word_at_url(url):
    #функция для примеры как вызывается async
    resource = requests.get(url)

    print(len(responce.text.split()))
    return len(response.text.split())
