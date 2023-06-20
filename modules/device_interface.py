class DeviceInterface:
    def __init__(self, id, name, description,
                 config, mtu, port_ide=None, connection=None,
                 infra_type=None, type=None):
        self.id = id
        self.connection = connection
        self.name = name
        self.description = description
        self.config = config
        self.type = type
        self.mtu = mtu
        self.port_ide = port_ide
        self.infra_type = infra_type
