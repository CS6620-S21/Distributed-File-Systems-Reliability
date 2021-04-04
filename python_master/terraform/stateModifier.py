import json
import random
import time
import math
count = random.randint(1,9999999)

timestamp = math.floor(time.time())

numberOfClients = 0
numberOfMetaloggers = 0
numberOfMasters = 0

clientServerInstance = {}

metaLoggerInstance = {}

volumeAttachInstance = {}

volumeInstance = {}

chunkServerInstance = {}

masterInstance = {}

def updateGlobalInstance():

    global clientServerInstance
    clientServerInstance = {
        "openstack_compute_instance_v2": [
            {
                "client" + str(random.randint(1,9999999)): [
                    {
                        "flavor_name": "m1.tiny",
                        "image_name": "ubuntu_dummy_config_snap101",
                        "name": "client" + str(random.randint(1,9999999)),
                        "security_groups": [
                            "default"
                        ]
                    }
                ]
            }
        ]
    }

    global metaLoggerInstance
    metaLoggerInstance  = {
        "openstack_compute_instance_v2": [
            {
                "metalogger" + str(random.randint(1,9999999)): [
                    {
                        "flavor_name": "m1.tiny",
                        "image_name": "ubuntu_dummy_config_snap101",
                        "name": "metalogger" + str(random.randint(1,9999999)),
                        "security_groups": [
                            "default"
                        ]
                    }
                ]
            }
        ]
    }
    global volumeAttachInstance
    volumeAttachInstance  = {
        "openstack_compute_volume_attach_v2": [
            {
                "va" + str(random.randint(1,9999999)): [
                    {
                        "instance_id": "${openstack_compute_instance_v2.chunkserver3.id}",
                        "volume_id": "${openstack_blockstorage_volume_v2.chunkserver3_volume.id}"
                    }
                ]
            }
        ]
    }
    global volumeInstance
    volumeInstance = {
        "openstack_blockstorage_volume_v2": [
            {
                "chunkserver_volume" + str(random.randint(1,9999999)): [
                    {
                        "name": "chunkserver_volume" + str(random.randint(1,9999999)),
                        "size": 10
                    }
                ]
            }
        ]
    }
    global chunkServerInstance
    chunkServerInstance = {
        "openstack_compute_instance_v2": [
            {
                "chunkserver" + str(random.randint(1,9999999)): [
                    {
                        "flavor_name": "m1.tiny",
                        "image_name": "ubuntu_dummy_config_snap101",
                        "name": "chunkserver" + str(random.randint(1,9999999)),
                        "security_groups": [
                            "default"
                        ]
                    }
                ]
            }
        ]
    }
    global masterInstance
    masterInstance = {
        "openstack_compute_instance_v2": [
            {
                "master1" + str(random.randint(1,9999999)): [
                    {
                        "flavor_name": "m1.tiny",
                        "image_name": "ubuntu_dummy_config_snap101",
                        "name": "master1" + str(random.randint(1,9999999)),
                        "security_groups": [
                            "default"
                        ]
                    }
                ]
            }
        ]
    }

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

    clientInstanceID = "CLIENT_" + str(numberOfClients) + "_" + str(timestamp)

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
        clientInstanceID : [
            {
                "value": "${openstack_compute_instance_v2." + clientInstanceID + ".access_ip_v4}"
            }
        ]

    })

    updateCurrentState(json_object)

def addMetalogger():

    global numberOfMetaloggers
    global timestamp

    numberOfMetaloggers += 1

    metaloggerInstanceID = "METALOGGER_" + str(numberOfMetaloggers) + "_" + str(timestamp)

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
        metaloggerInstanceID : [
            {
                "value": "${openstack_compute_instance_v2." + metaloggerInstanceID + ".access_ip_v4}"
            }
        ]

    })

    updateCurrentState(json_object)

def addMasterServer():

    global numberOfMasters
    global timestamp

    numberOfMasters += 1

    masterInstanceID = "MASTER" + str(numberOfMasters) + "_" + str(timestamp)

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
        masterInstanceID : [
            {
                "value": "${openstack_compute_instance_v2." + masterInstanceID + ".access_ip_v4}"
            }
        ]

    })

    updateCurrentState(json_object)


def addChunkServer():
    updateGlobalInstance()
    chunkServer = chunkServerInstance
    volume = volumeInstance
    volumeAttach = volumeAttachInstance

    chunkServerid  = ""
    volumeid  = ""
    volumeAttachid = ""


    dict = chunkServer["openstack_compute_instance_v2"][0]

    for key in dict:
        chunkServerid = key


    dict = volume["openstack_blockstorage_volume_v2"][0]

    for key in dict:
        volumeid = key


    dict = volumeAttach["openstack_compute_volume_attach_v2"][0]
    for key in dict:
        volumeAttachid = key

    dict = volumeAttach["openstack_compute_volume_attach_v2"][0][volumeAttachid][0]
    dict["instance_id"] = "${openstack_compute_instance_v2." + chunkServerid + ".id}"
    dict["volume_id"] = "${openstack_blockstorage_volume_v2." + volumeid + ".id}"

    a_file = open("./terraform/sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()


    # Code for updating output node in sample.json.tf

    instanceId = ""
    instanceDetails = chunkServer["openstack_compute_instance_v2"][0]
    for key in instanceDetails: instanceId = key

    json_object["output"].append({
        instanceId : [
            {
                "value": "${openstack_compute_instance_v2."+ instanceId + ".access_ip_v4}"
            }
        ]

    })

    json_object["resource"].append(chunkServer)
    json_object["resource"].append(volume)
    json_object["resource"].append(volumeAttach)


    a_file = open("./terraform/sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

def removeChunkServer():

    a_file = open("./terraform/sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    # print(json_object["resource"][0])

    n = len(json_object["resource"])
    for i in range(0, n):
        if("openstack_compute_instance_v2" in json_object["resource"][i].keys()):
            print(json_object["resource"][i]["openstack_compute_instance_v2"][0])

def resetState():
    a_file = open("./terraform/sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    json_object["resource"] = []
    json_object["output"] = []

    a_file = open("./terraform/sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

