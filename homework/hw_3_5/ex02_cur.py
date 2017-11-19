import sys
from zeep import Client
import time


def calc_sum(source_file):
    client = Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    sum_in_rub = 0

    with open(source_file) as f:
        for line in f:
            data_list = line.split()
            cur_value = int(data_list[1])
            cur_code = data_list[2]

            sum_in_rub += client.service.ConvertToNum(
                toCurrency='RUB',
                fromCurrency=cur_code,
                amount=cur_value,
                rounding=True
            )
            time.sleep(0.05)

    sum_in_rub = round(sum_in_rub)
    print('Сумма в рублях:', sum_in_rub)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        calc_sum(sys.argv[1])
    else:
        print('Не указан путь к файлу с данными в параметре')
