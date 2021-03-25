
from terraformShell import *
from stateModifier import *

from python_master.terraform.stateModifier import removeChunkServer


def createInfrastructure(masterservers, chunkservers, metaloggers, clientservers):
    resetState()
    for i in range(0, masterservers):
        addMasterServer()
    for i in range(0, chunkservers):
        addChunkServer()
    for i in range(0, metaloggers):
        addMetalogger()
    for i in range(0, clientservers):
        addClientServer()
    init()
    run()

def destroyInfrastructure():
    destroy()
    resetState()

def getIPs():
    # output()
    a_file = open("./output.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    hosts_inventory_dict = {'master': {},'metalogger': {},'chunkserver': {},'client': {}}

    for val in  json_object.keys():

        if("chunkserver" in val):
            hosts_inventory_dict["chunkserver"][val] = json_object[val]["value"]

        if("metalogger" in val):
            hosts_inventory_dict["metalogger"][val] = json_object[val]["value"]

        if("client" in val):
            hosts_inventory_dict["client"][val] = json_object[val]["value"]

        if("master" in val):
            hosts_inventory_dict["master"][val] = json_object[val]["value"]

    return hosts_inventory_dict


def deleteChunkServer():
    print("Client Destroyed")



# addChunkServer()
# removeChunkServer()
# Users/aksha/OneDrive/Documents/projects/git/Distributed-File-Systems-Reliability/python_master/terraform
# destroyInfrastructure()
# createInfrastructure(1, 0, 1, 1)
# print(getIPs())
# getIPs()
