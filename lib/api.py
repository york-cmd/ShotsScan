import requests
import config
import json


def get(target):
    url = ''
    data = {}
    if target == 'ip':
        url = config.get_ip_url
    elif target == 'domain':
        url = config.get_domain_url
    elif target == 'subdomain':
        url = config.get_subdomain_url
    if url:
        url = url + f'?key={config.key}'
        try:
            r = requests.post(url, timeout=3)
            data = r.json()
            if data['code'] == 1:
                return data
            elif data['code'] == 0:
                return data
        except Exception as e:
            data['code'] = 0
            data['msg'] = e
        return data


def put_alive(alive_data):
    try:
        url = config.put_alive_url + f'?key={config.key}'
        # print(json.dumps(alive_data))
        r = requests.post(url, data=json.dumps(alive_data))
        return r.json()
    except Exception as e:
        return e


def put_port(port_data):
    try:
        url = config.put_port_url + f'?key={config.key}'
        # print(json.dumps(port_data))
        r = requests.post(url, data=json.dumps(port_data))
        # print(r.text)
        return r.json()
    except Exception as e:
        return e


def put_subdomain(domain_data):
    try:
        url = config.put_subdomain_url + f'?key={config.key}'
        r = requests.post(url, data=json.dumps(domain_data))
        # print(json.dumps(domain_data))
        return r.json()
    except Exception as e:
        return e

