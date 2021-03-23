
from terraformShell import *
from stateModifier import *



def createInfrastructure(masterservers, chunkservers, metaloggers, clientservers):
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
    output()
    a_file = open("./output.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    return json_object




# destroyInfrastructure()
# createInfrastructure(1, 2, 1, 2)
# getIPs()
