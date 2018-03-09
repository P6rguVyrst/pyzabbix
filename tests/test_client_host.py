from pprint import pprint as pp


class TestZabbixHostCreate:

    def test_min_requirements_success(self, host):
        snmp_interface = {
            'type': 2,
            'main': 1,
            'useip': 1,
            'ip': '127.0.0.1',
            'dns': 'localhost',
            'port': 161
        }
        r = host.create(
            host='MY-TEST-APPLICATION',
            groups=[123],
            interfaces=[snmp_interface]
        )
        pp(r)

def test_host_get(host):
    host.get()

def test_host_update(host):
    host.update()

def test_host_delete(host):
    host.delete()



