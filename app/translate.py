import json
import requests
from flask import current_app


def translate(text, source_language, dest_language):
    if 'YA_TRANSLATOR_KEY' not in current_app.config or not current_app.config['YA_TRANSLATOR_KEY']:
        return 'Error: the translation service is not configured'

    ya_api_key = current_app.config['YA_TRANSLATOR_KEY']

    r = requests.get(
        'https://translate.yandex.net/api/v1.5/tr.json/translate?key={0}&text={1}&lang={2}-{3}'.format(ya_api_key, text,
                                                                                                       source_language,
                                                                                                       dest_language))

    if r.status_code != 200:
        return 'Error: the translation service failed'
    return json.loads(r.content.decode('utf-8-sig'))


def detected_language(text):
    ya_api_key = current_app.config['YA_TRANSLATOR_KEY']

    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/detect?key={0}&text={1}'.format(ya_api_key, text))

    if r.status_code != 200:
        return 'UNKNOWN'
    return json.loads(r.content.decode('utf-8'))['lang']
