import requests
from urllib.parse import urljoin

APP_ID = 'ab263693a73f437d9ab0fa755752c838'
AUTH_URL = 'https://oauth.yandex.ru/authorize'

auth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}

TOKEN = 'AQAAAAAADaHfAASsSVibd0KuRkLnifGLbrCdIhs'


class YMBase():
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': f'OAuth {self.token}',
            'Content-Type': 'application/x-yametrika+json'
        }


class YMUser(YMBase):
    MANAG_URL = 'https://api-metrika.yandex.ru/management/v1/'

    def get_counters(self):
        query_headers = self.get_headers()
        response = requests.get(
            urljoin(self.MANAG_URL, 'counters'),
            headers=query_headers
        )
        counters = response.json()['counters']
        return [Counter(c['id'], self.token) for c in counters]


class Counter(YMBase):
    STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/data'

    def __init__(self, id, token):
        self.id = id
        super().__init__(token)


    def get_metric_value(self, metrics):
        query_headers = self.get_headers()
        params = {
            'id': self.id,
            'metrics': ','.join(metrics)
        }
        response = requests.get(self.STAT_URL, params, headers=query_headers)
        return response.json()


if __name__ == '__main__':
    COUNTER_ID = '46776849'
    user = YMUser(TOKEN)
    counters = user.get_counters()
    metrics = [
        'ym:s:visits',
        'ym:s:users',
        'ym:s:pageviews',
    ]
    metric_value = counters[0].get_metric_value(metrics)

    print('Визиты', metric_value['max'][0])
    print('Посетители', metric_value['max'][1])
    print('Просмотры', metric_value['max'][2])