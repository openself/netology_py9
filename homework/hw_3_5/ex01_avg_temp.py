import sys
from zeep import Client


def avg_temp(source_file):
    client = Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    avg_result = 0
    counter = 0

    with open(source_file) as f:
        for line in f:
            degree_fahrenheit = int(line.split()[0])
            avg_result += degree_fahrenheit
            counter += 1

    if counter != 0:
        avg_result = avg_result / counter
        result_cel = client.service.ConvertTemp(
            avg_result,
            'degreeFahrenheit',
            'degreeCelsius'
        )
        result_cel = round(result_cel)
        print('Средняя температура в градусах Цельсия:', result_cel)
    else:
        print('Файл с даннными пустой или имеет неверный формат.')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        avg_temp(sys.argv[1])
    else:
        print('Не указан путь к файлу с данными в параметре')
