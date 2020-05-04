from tools.oneforall import oneforall
from lib.api import get, put_subdomain
from tools.oneforall.config import logger
import time
import datetime


def scan(domain):
    domain_data = {'code': 0, 'reason': '', 'data': []}
    try:
        app = oneforall.OneForAll(domain)
        app.run()
        for i in app.data:
            subdomain = i['cname']
            subdomain_ip = i['content']
            city = ''
            if subdomain:
                domain_data['data'].append({'subdomain': subdomain, 'subdomain_ip': subdomain_ip, 'city': city})
        domain_data['code'] = 1
    except Exception as e:
        domain_data['code'] = 0
        domain_data['reason'] = str(e)
    finally:
        return domain_data


def run():
    while True:
        data = get('domain')
        if data['code'] == 0:
            logger.log('ERROR', data['msg'])
            time.sleep(30)
        else:
            domain = data['data']['domain']
            start = datetime.datetime.now()
            domain_data = scan(domain)
            end = datetime.datetime.now()
            domain_data['time'] = (end-start).seconds
            domain_data['domain'] = domain
            put_subdomain(domain_data)


if __name__ == '__main__':
    run()
