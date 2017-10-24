import os
import chardet
from bs4 import BeautifulSoup
from collections import Counter
import json

def print_top_ten_words_json():
    'Выводит топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого json-файла'
    json_files = [name for name in os.listdir('.') if name.endswith('.json')]
    for current_file in json_files:
        with open(current_file, 'rb') as file:
            data_raw = file.read()
            result = chardet.detect(data_raw)
            data_decoded = data_raw.decode(result['encoding'])
            dict_parsed = json.loads(data_decoded)
            news_items = dict_parsed['rss']['channel']['items']
            text_news = ''
            for news_item in news_items:
                text_news += news_item['description'] + ' '

            big_words = [word for word in text_news.split() if len(word) > 6]
            top_words_list = [word_counter[0] for word_counter in Counter(big_words).most_common(10)]
            string_top_words = ", ".join(top_words_list)
            print(current_file, ' - топ 10 слов:', string_top_words)


def print_top_ten_words_xml():
    'Выводит топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого xml-файла'
    xml_files = [name for name in os.listdir('.') if name.endswith('.xml')]
    for current_file in xml_files:
        with open(current_file, 'rb') as file:
            data_raw = file.read()
            soup = BeautifulSoup(data_raw, 'html5lib')
            text = soup.get_text()
            text = text.replace('<br>', ' ')
            text = text.replace('<', ' ')
            text = text.replace('>', ' ')
            text = text.replace('/', ' ')
            text = text.replace('=', ' ')
            text = text.replace(']', ' ')
            text = text.replace(',', ' ')
            text = text.replace('вОтпуск.ру', ' ')
            text = text.replace('www.votpusk.ru', ' ')
            text = text.replace('.asp?', ' ')

            big_words = [word for word in text.split() if len(word) > 6]
            top_words_list = [word_counter[0] for word_counter in Counter(big_words).most_common(10)]
            string_top_words = ", ".join(top_words_list)
            print(current_file, ' - топ 10 слов:', string_top_words)


if __name__ == '__main__':
    print_top_ten_words_json()
    print_top_ten_words_xml()