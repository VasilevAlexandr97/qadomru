from behave import *
import requests
import json
import time

@given('website "{url}"')
def step(context, url):
    context.url = url


# Проверка успешной авторизации
@then('check authorization success')
def step(context):
    params = {
        'client_id': 'er_ottweb_device',
        'timestamp': int(time.time()), 
        'device_id':'user123'
    }
    r = requests.get(f'{context.url}', params=params)
    content = json.loads(r.content)
    assert content['result'] == 1


# передаем неправильный client_id
@then('pass incorrect client_id')
def step(context):
    params = {
        'client_id': 'ottweb_device',
        'timestamp': int(time.time()), 
        'device_id':'user123'
    }
    r = requests.get(f'{context.url}', params=params)
    content = json.loads(r.content)
    assert content['result'] == 0

"""
# Передаем неправильный device_id
@then('pass incorrect device_id')
def step(context):
    params = {
        'client_id': 'er_ottweb_device',
        'timestamp': int(time.time()), 
        'device_id':'user12'
    }
    r = requests.get(f'{context.url}', params=params)
    content = json.loads(r.content)
    assert content['result'] == 0
"""
# Передаем только 1 парамет в запрос
@then('pass one parametr')
def step(context):
    params = {
        'client_id': 'er_ottweb_device',
        'timestamp': int(time.time()), 
        'device_id':'user123'
    }

    parametr_list = [{item:params[item]} for item in params]

    for item in parametr_list:
        r = requests.get(f'{context.url}', params=item)
        content = json.loads(r.content)
        assert content['result'] == 0


# Передаем неправильные параметры в запрос
@then('pass incorrect parameters')
def step(context):
    params = {
        'client_id': 'device',
        'timestamp': int(time.time()),
        'device_id': 'user'
    }

    r = requests.get(f'{context.url}', params=params)
    content = json.loads(r.content)
    assert content['result'] == 0


# Передаем только 2 параметра
@then('pass two parameters')
def step(context):
    params = {
        'client_id': 'device',
        'timestamp': int(time.time()),
    }

    r = requests.get(f'{context.url}', params=params)
    content = json.loads(r.content)
    assert content['result'] == 0


# Передаем время в float типе
@then('pass time float')
def step(context):
    params = {
        'client_id': 'er_ottweb_device',
        'timestamp': time.time(), 
        'device_id':'user123'
    }

    r = requests.get(f'{context.url}', params=params)
    content = json.loads(r.content)
    assert content['result'] == 0