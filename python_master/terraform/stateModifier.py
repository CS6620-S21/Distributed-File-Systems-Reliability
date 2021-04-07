# This file contains a combination of methods which can be used by the terraform_driver file
# Here the methods are an amalgamation of three abstraction
# Terraform itself for specifying type of vms with volume, without volume, only volumes, mounting
# MooseFS vm types here client server, metalogger, chunkserver, master server
# And finally methods to modify the json file itself
# For the purpose of simplicity these three abstraction are condensed into one monolith may be updated
# Based on the need and requirement


import json
import random
import time
import math

timestamp = math.floor(time.time())
numberOfClients = 0
numberOfMetaloggers = 0
numberOfMasters = 0
numberOfChunkServers = 0
numberOfVolumes = 0
numberOfVolumeAttach = 0


# Fetches the current state of the terraform state
def fetchCurrentState():
    a_file = open("./terraform/sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    return json_object


# Updates the current state of the terraform state
def updateCurrentState(json_object):
    a_file = open("./terraform/sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()


# Adds a Client Instance in the terraform state
def addClientInstance():
    global numberOfClients
    global timestamp

    numberOfClients += 1

    clientInstanceID = "CLUSTER_" + str(timestamp) + "_CLIENT_" + str(numberOfClients)

    json_object = fetchCurrentState()

    clientServerInstance = {
        "openstack_compute_instance_v2": [
            {
                clientInstanceID: [
                    {
                        "flavor_name": "m1.tiny",
                        "image_name": "ubuntu_dummy_config_snap101",
                        "name": clientInstanceID,
                        "security_groups": [
                            "default"
                        ]
                    }
                ]
            }
        ]
    }

    json_object["resource"].append(clientServerInstance)

    json_object["output"].append({
        clientInstanceID: [
            {
                "value": "${openstack_compute_instance_v2." + clientInstanceID + ".access_ip_v4}"
            }
        ]

    })

    updateCurrentState(json_object)


# Adds a Metalogger Instance in the terraform state
def addMetalogger():
    global numberOfMetaloggers
    global timestamp

    numberOfMetaloggers += 1

    metaloggerInstanceID = "CLUSTER_" + str(timestamp) + "_METALOGGER_" + str(numberOfMetaloggers)

    json_object = fetchCurrentState()

    metaloggerInstance = {
        "openstack_compute_instance_v2": [
            {
                metaloggerInstanceID: [
                    {
                        "flavor_name": "m1.tiny",
                        "image_name": "ubuntu_dummy_config_snap101",
                        "name": metaloggerInstanceID,
                        "security_groups": [
                            "default"
                        ]
                    }
                ]
            }
        ]
    }

    json_object["resource"].append(metaloggerInstance)

    json_object["output"].append({
        metaloggerInstanceID: [
            {
                "value": "${openstack_compute_instance_v2." + metaloggerInstanceID + ".access_ip_v4}"
            }
        ]

    })

    updateCurrentState(json_object)


# Adds a MasterServer Instance in the terraform state
def addMasterServer():
    global numberOfMasters
    global timestamp

    numberOfMasters += 1

    masterInstanceID = "CLUSTER_" + str(timestamp) + "_MASTER_" + str(numberOfMasters)

    json_object = fetchCurrentState()

    masterServerInstance = {
        "openstack_compute_instance_v2": [
            {
                masterInstanceID: [
                    {
                        "flavor_name": "m1.tiny",
                        "image_name": "ubuntu_dummy_config_snap101",
                        "name": masterInstanceID,
                        "security_groups": [
                            "default"
                        ]
                    }
                ]
            }
        ]
    }

    json_object["resource"].append(masterServerInstance)

    json_object["output"].append({
        masterInstanceID: [
            {
                "value": "${openstack_compute_instance_v2." + masterInstanceID + ".access_ip_v4}"
            }
        ]

    })

    updateCurrentState(json_object)


# Adds a MasterServer Instance in the terraform state
def addChunkServer():
    global numberOfChunkServers
    global numberOfVolumes
    global numberOfVolumeAttach
    global timestamp

    numberOfChunkServers += 1
    numberOfVolumes += 1
    numberOfVolumeAttach += 1

    chunkServerInstanceID = "CLUSTER_" + str(timestamp) + "_CHUNKSERVER_" + str(numberOfChunkServers)
    volumeInstanceID = chunkServerInstanceID + "_VOLUME_" + str(numberOfVolumes)
    volumeAttachInstanceID = chunkServerInstanceID + "_VOLUMEATTACH_" + str(numberOfVolumeAttach)

    json_object = fetchCurrentState()

    volumeInstance = {
        "openstack_blockstorage_volume_v2": [
            {
                volumeInstanceID: [
                    {
                        "name": volumeInstanceID,
                        "size": 10
                    }
                ]
            }
        ]
    }

    chunkServerInstance = {
        "openstack_compute_instance_v2": [
            {
                chunkServerInstanceID: [
                    {
                        "flavor_name": "m1.tiny",
                        "image_name": "ubuntu_dummy_config_snap101",
                        "name": chunkServerInstanceID,
                        "security_groups": [
                            "default"
                        ]
                    }
                ]
            }
        ]
    }

    volumeAttachInstance = {
        "openstack_compute_volume_attach_v2": [
            {
                volumeAttachInstanceID: [
                    {
                        "instance_id": "${openstack_compute_instance_v2." + chunkServerInstanceID + ".id}",
                        "volume_id": "${openstack_blockstorage_volume_v2." + volumeInstanceID + ".id}"
                    }
                ]
            }
        ]
    }

    json_object["resource"].append(chunkServerInstance)
    json_object["resource"].append(volumeInstance)
    json_object["resource"].append(volumeAttachInstance)

    json_object["output"].append({
        chunkServerInstanceID: [
            {
                "value": "${openstack_compute_instance_v2." + chunkServerInstanceID + ".access_ip_v4}"
            }
        ]

    })

    updateCurrentState(json_object)


def removeResource(resourceid):
    resource = []
    output = []
    json_object = fetchCurrentState()

    print("LOGS INPUT")
    print(json_object)
    print(json_object["resource"])

    n = len(json_object["resource"])

    for i in range(0, n):
        data_raw = json_object["resource"][i]
        data = json.dumps(json_object["resource"][i])

        print("DATA")
        print(data)
        if resourceid in data:
            resource.append(data_raw)

    print("LOOK UP")
    print(resource)

    n = len(json_object["output"])

    for i in range(0, n):
        data = json.dumps(json_object["output"][i])
        data_raw = json_object["output"][i]
        if resourceid in data:
            output.append(data_raw)

    for i in range(0, len(resource)):
        print("resource[i]")
        print(resource[i])
        json_object["resource"].remove(resource[i])
        print("json_object")
        print(json_object)

    for i in range(0, len(output)):
        json_object["output"].remove(output[i])

    updateCurrentState(json_object)


# A method that empties the json file representing state
def resetState():
    a_file = open("./terraform/sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    json_object["resource"] = []
    json_object["output"] = []

    a_file = open("./terraform/sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()
