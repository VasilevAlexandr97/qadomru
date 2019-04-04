from behave import *
import requests
import time
import json

@given('get token "{url}"')
def step(context, url):
    context.url = url
    params = {
        'client_id': 'er_ottweb_device',
        'timestamp': int(time.time()), 
        'device_id':'user123'
    }

    r = requests.get("http://discovery-preprod.ertelecom.ru/api/token/device", params=params)

    context.token = json.loads(r.content)['token']


# Передаем правильный токен
@then('pass correct token')
def step(context):
    headers = {
        'X-Auth-Token': context.token
    }

    r = requests.get(f'{context.url}', headers=headers)
    assert json.loads(r.content)['result'] == 1


# Передаем не правильный токен
@then('pass incorrect token')
def step(context):
    headers = {
        'X-Auth-Token': context.token + '1'
    }

    r = requests.get(f'{context.url}', headers=headers)
    assert json.loads(r.content)['result'] == 0