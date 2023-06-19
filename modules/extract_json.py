import json
from modules.device_interface import DeviceInterface

interfaces = []


def port_channel_to_class(unit, id):
    name = 'Port-channel' + str(unit["name"])
    print(name)

    if "description" in unit:
        description = str(unit["description"])
    else:
        description = None
    if "mtu" in unit:
        mtu = unit["mtu"]
    else:
        mtu = None
    return DeviceInterface(id, name, description, unit, mtu)


def tengigabit_to_class(unit, id):
    name = 'TenGigabitEthernet' + str(unit["name"])
    if "description" in unit:
        description = str(unit["description"])
    else:
        description = None
    if "mtu" in unit:
        mtu = unit["mtu"]
    else:
        mtu = None

    if "Cisco-IOS-XE-ethernet:channel-group" in unit:
        port_ide_name = 'Port-channel' + \
            str(unit["Cisco-IOS-XE-ethernet:channel-group"]["number"])
    else:
        port_ide_name = None

    port_ide = None

    for obj in interfaces:
        if obj.name == port_ide_name:
            port_ide = obj.id
            break

    return DeviceInterface(id, name, description, unit, mtu, port_ide)

def extract_json():
    with open('modules/configClear_v2.json') as file:
        content = json.load(file)
        id = 0
        interface_layer = content["frinx-uniconfig-topology:configuration"]["Cisco-IOS-XE-native:native"]["interface"]

        bdi_dict = interface_layer["BDI"]
        loopback = interface_layer["Loopback"]
        port_channel = interface_layer["Port-channel"]
        tengigabit = interface_layer["TenGigabitEthernet"]
        gigabit = interface_layer["GigabitEthernet"]

        for unit in port_channel:
            interfaces.append(port_channel_to_class(unit, id))
            id += 1
        for unit in tengigabit:
            interfaces.append(tengigabit_to_class(unit, id))
            id += 1
        for unit in gigabit:
            interfaces.append(tengigabit_to_class(unit, id))
            id += 1

    # for i in interfaces:
    #     print()
    #     print(i.id, " ", i.name, " ", i.description, " ", i.config, " ", i.port_ide," ",i.mtu)
    #     print( )


def get_list_of_interfaces():
    return interfaces
