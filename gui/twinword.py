import requests

def get_word_difficulty(word):
    # Считываем API ключ и X-RapidAPI-Host из файла
    with open('apikey.txt', 'r') as f:
        lines = f.readlines()
        headers = {line.split(':')[0].strip(): line.split(':')[1].strip() for line in lines}

    url = "https://twinword-twinword-bundle-v1.p.rapidapi.com/score_word/"
    querystring = {"entry": word}

    print(f'Отправка запроса к API Twinword для слова "{word}"...')

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        print(f'Получен ответ от API Twinword: {data}')
        return data.get('ten_degree', 11)  # Если 'ten_degree' не найден, возвращаем 0
    else:
        print(f'An error occured while getting words difficulty: {response.status_code}')
        return 0  # Если произошла ошибка, возвращаем 0



