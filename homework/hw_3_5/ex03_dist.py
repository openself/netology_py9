import sys
from zeep import Client


def calc_distance(source_file):
    client = Client('http://www.webservicex.net/length.asmx?WSDL')
    distance_miles = 0

    with open(source_file) as f:
        for line in f:
            distance_miles += float(line.split()[1].replace(',', ''))

    result_km = client.service.ChangeLengthUnit(
        distance_miles,
        'Miles',
        'Kilometers'
        )

    result_km = round(result_km, 2)
    print('Расстояние в милях:', distance_miles)
    print('Расстояние в километрах:', result_km)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        calc_distance(sys.argv[1])
    else:
        print('Не указан путь к файлу с данными в параметре')
