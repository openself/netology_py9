import requests
import os

API_KEY = 'trnsl.1.1.20171108T185912Z.67e52e22beceb0a0.f58990230ef92608faae297f1a2a7afc9122afa0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_it(file_text, file_result, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param to_lang:
    :return:
    """

    with open(file_text, encoding='utf-8') as file:
        source = file.read()

    params = {
            'key': API_KEY,
            'text': source,
            'lang': '{}-{}'.format(from_lang, to_lang),
        }
    response = requests.get(URL, params=params)
    json_ = response.json()
    result = ''.join(json_['text'])

    with open(file_result, 'wt', encoding='utf-8') as f:
        f.write(result)


if __name__ == '__main__':
    translate_it('DE.txt', 'DE_RU.txt', 'de', 'ru')
    translate_it('ES.txt', 'ES_RU.txt', 'es', 'ru')
    translate_it('FR.txt', 'FR_RU.txt', 'fr', 'ru')

