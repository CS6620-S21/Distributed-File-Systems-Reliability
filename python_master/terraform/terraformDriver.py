# This file is the first point of contact for the main_driver it provides methods to be used by it
# Here the methods are a combination of state modifier function and terraform shell



from terraform.terraformShell import *
from terraform.stateModifier import *

# from python_master.terraform.stateModifier import removeChunkServer




def createInfrastructure(masterservers, chunkservers, metaloggers, clientservers):
    resetState()
    for i in range(0, masterservers):
        addMasterServer()
    for i in range(0, chunkservers):
        addChunkServer()
    for i in range(0, metaloggers):
        addMetalogger()
    for i in range(0, clientservers):
        addClientInstance()
    init()
    run()


def destroyInfrastructure():
    destroy()
    resetState()


def getIPs():
    output()
    a_file = open("./terraform/output.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    hosts_inventory_dict = {'master': {},
                            'metalogger': {}, 'chunkserver': {}, 'client': {}}

    for val in json_object.keys():

        if("CHUNKSERVER" in val):
            hosts_inventory_dict["chunkserver"][val] = json_object[val]["value"]

        if("METALOGGER" in val):
            hosts_inventory_dict["metalogger"][val] = json_object[val]["value"]

        if("CLIENT" in val):
            hosts_inventory_dict["client"][val] = json_object[val]["value"]

        if("MASTER" in val):
            hosts_inventory_dict["master"][val] = json_object[val]["value"]

    return hosts_inventory_dict


def deleteClientInstance():
    removeClientInstance()
    init()
    run()

def deleteChunkServer():
    print("Chunk server Destroyed")
