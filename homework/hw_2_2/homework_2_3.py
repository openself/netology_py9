import os
import chardet
from collections import Counter

def print_top_ten_words():
    'Выводит топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла'
    txt_files = [name for name in os.listdir('.') if name.endswith('.txt')]
    for current_file in txt_files:
        with open(current_file, 'rb') as file:
            data_raw = file.read()
            result = chardet.detect(data_raw)
            data_decoded = data_raw.decode(result['encoding'])

            big_words = [word for word in data_decoded.split() if len(word) > 6]
            top_words_list = Counter(big_words).most_common(10)

            string_top_words = ''
            for top_word in top_words_list:
                string_top_words += top_word[0] + ', '
            string_top_words = string_top_words[: -2]

            print(current_file, ' - топ 10 слов:', string_top_words)


if __name__ == '__main__':
    print_top_ten_words()