import json
from modules.device_interface import DeviceInterface


interfaces = []

# load interface to class
def to_class(name, unit, id):

    name = name + str(unit["name"])

    if "description" in unit:
        description = str(unit["description"])
    else:
        description = None

    if "mtu" in unit:
        mtu = unit["mtu"]
    else:
        mtu = None

    port_ide = None
    
    # check for id of portchannel
    if "Cisco-IOS-XE-ethernet:channel-group" in unit:
        port_ide_name = 'Port-channel' + \
            str(unit["Cisco-IOS-XE-ethernet:channel-group"]["number"])
        for obj in interfaces:
            if obj.name == port_ide_name:
                port_ide = obj.id
                break
    else:
        port_ide_name = None

    return DeviceInterface(id, name, description, unit, mtu, port_ide)


def extract_json():

    with open('modules/configClear_v2.json') as file:
        
        content = json.load(file)
        id = 0

        interface_layer = (content["frinx-uniconfig-topology:configuration"]
                                  ["Cisco-IOS-XE-native:native"]
                                  ["interface"])

        # these interfaces can be added later to dictionary
        bdi_dict = interface_layer["BDI"]                      
        loopback = interface_layer["Loopback"]  

        port_channel = interface_layer["Port-channel"]
        tengigabit = interface_layer["TenGigabitEthernet"]
        gigabit = interface_layer["GigabitEthernet"]

        interfaces_to_parse = {"Port-channel" : port_channel,
                               "TenGigabitEthernet": tengigabit,
                               "GigabitEthernet": gigabit}

        for name, interface in interfaces_to_parse.items():
            for unit in interface:
                interfaces.append(to_class(name, unit, id))
                id += 1

# return list of classes with information about interfaces
def get_list_of_interfaces():
    return interfaces
