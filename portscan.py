from tools.portscan.portscan import PortScan
from lib.api import get, put_port
from tools.oneforall.config import logger
import time
import datetime


def scan(ip, is_scan):
    port_data = {'code': 0, 'reason': '', 'data': []}
    try:
        if not is_scan:
            app = PortScan(ip)
            app.run()
            for i in app.data:
                ip_info = app.data.get(i)
                ip = ip_info['ip']
                port = ip_info['port']
                name = ip_info['name']
                product = ip_info['product']
                version = ip_info['version']
                port_data['data'].append(
                    {"ip": ip, "port": port, "service": name, "product": product, "version": version}
                )
            port_data['code'] = 1
        else:
            port_data['reason'] = '该IP端口数据已被录入'
    except Exception as e:
        port_data['code'] = 0
        port_data['reason'] = str(e)
    finally:
        return port_data


def run():
    while True:
        data = get('ip')
        if data['code'] == 0:
            logger.log('ERROR', data['msg'])
            time.sleep(30)
        else:
            ip = data['data'].get('ip')
            subdomain = data['data'].get('subdomain')
            is_scan = data['data'].get('is_scan')
            start = datetime.datetime.now()
            port_data = scan(ip, is_scan)
            end = datetime.datetime.now()
            port_data['time'] = (end-start).seconds
            port_data['domain'] = subdomain
            put_port(port_data)


if __name__ == '__main__':
    run()
