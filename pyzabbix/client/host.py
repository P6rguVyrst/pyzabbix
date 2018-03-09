
class Host:


    def __init__(self):
        pass

    def check_mandatory_parameters(self, mandatory, arguments):
        for param in mandatory:
            if param not in arguments.keys():
                raise KeyError('Missing kwargs:', param)

    def check_interface_mandatory_parameters(self, inteface):
        """
        """
        mandatory_params = ['type', 'main', 'useip', 'ip', 'dns', 'port']


    def get(self):
        """
        """
        pass

    def create(self, host=None, name=None, proxy_hostid=None,
        interfaces=[], groups=[], templates=[], macros=[],
        inventory=[], inventory_mode=1):
        """
        """
        mandatory_parameters = ['host', 'groups', 'interfaces']
        arguments = locals()
        del arguments['self']
        host_data = {k: v for k, v in arguments.items() if v}
        self.check_mandatory_parameters(
            mandatory_parameters, host_data
        )
        return host_data

    def update(self):
        """
        """
        pass

    def delete(self):
        """
        """
        pass

