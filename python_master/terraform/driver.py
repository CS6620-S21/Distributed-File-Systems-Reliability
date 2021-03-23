
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

    run()


def destroyInfrastructure():
    destroy()
    resetState()

# resetState()
# createInfrastructure(1, 1, 1, 1)
destroyInfrastructure()
