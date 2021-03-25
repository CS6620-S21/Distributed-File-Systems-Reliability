import json
import random
count = random.randint(1,9999999)

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

def addClientServer():
    updateGlobalInstance()
    a_file = open("./sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()


    instance = clientServerInstance
    json_object["resource"].append(instance)

    instanceId = ""
    instanceDetails = clientServerInstance["openstack_compute_instance_v2"][0]
    for key in instanceDetails: instanceId = key

    json_object["output"].append({
        instanceId : [
            {
                "value": "${openstack_compute_instance_v2."+ instanceId + ".access_ip_v4}"
            }
        ]

    })


    a_file = open("sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

def addMetalogger():
    updateGlobalInstance()
    a_file = open("./sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    # Code for updating output node in sample.json.tf
    instance = metaLoggerInstance
    json_object["resource"].append(instance)

    instanceId = ""
    instanceDetails = instance["openstack_compute_instance_v2"][0]
    for key in instanceDetails: instanceId = key

    json_object["output"].append({
        instanceId : [
            {
                "value": "${openstack_compute_instance_v2."+ instanceId + ".access_ip_v4}"
            }
        ]

    })

    # Code for updating output resource in sample.json.tf
    a_file = open("sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

def addMasterServer():
    updateGlobalInstance()
    a_file = open("./sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()


    # Code for updating output node in sample.json.tf
    instance = masterInstance
    json_object["resource"].append(instance)

    instanceId = ""
    instanceDetails = instance["openstack_compute_instance_v2"][0]
    for key in instanceDetails: instanceId = key

    json_object["output"].append({
        instanceId : [
            {
                "value": "${openstack_compute_instance_v2."+ instanceId + ".access_ip_v4}"
            }
        ]

    })




    a_file = open("sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

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

    a_file = open("./sample.tf.json", "r")
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


    a_file = open("sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

def removeChunkServer():

    a_file = open("./sample.tf.json", "r")
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

