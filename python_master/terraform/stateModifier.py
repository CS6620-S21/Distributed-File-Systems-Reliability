import json
import random
count = random.randint(1,9999999)



clientServerInstance = {
    "openstack_compute_instance_v2": [
        {
            "client" + str(random.randint(1,9999999)): [
                {
                    "flavor_name": "m1.tiny",
                    "image_name": "testVMSnap1",
                    "name": "client" + str(random.randint(1,9999999)),
                    "security_groups": [
                        "default"
                    ]
                }
            ]
        }
    ]
}

metaLoggerInstance = {
    "openstack_compute_instance_v2": [
        {
            "metalogger" + str(random.randint(1,9999999)): [
                {
                    "flavor_name": "m1.tiny",
                    "image_name": "testVMSnap1",
                    "name": "metalogger" + str(random.randint(1,9999999)),
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
            "va" + str(random.randint(1,9999999)): [
                {
                    "instance_id": "${openstack_compute_instance_v2.chunkserver3.id}",
                    "volume_id": "${openstack_blockstorage_volume_v2.chunkserver3_volume.id}"
                }
            ]
        }
    ]
}

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

chunkServerInstance = {
  "openstack_compute_instance_v2": [
      {
          "chunkserver" + str(random.randint(1,9999999)): [
              {
                  "flavor_name": "m1.tiny",
                  "image_name": "testVMSnap1",
                  "name": "chunkserver" + str(random.randint(1,9999999)),
                  "security_groups": [
                      "default"
                  ]
              }
          ]
      }
  ]
}

masterInstance = {
    "openstack_compute_instance_v2": [
        {
            "master1" + str(random.randint(1,9999999)): [
                {
                    "flavor_name": "m1.tiny",
                    "image_name": "testVMSnap1",
                    "name": "master1" + str(random.randint(1,9999999)),
                    "security_groups": [
                        "default"
                    ]
                }
            ]
        }
    ]
}

def updateGlobalInstance():

    global clientServerInstance
    clientServerInstance = {
        "openstack_compute_instance_v2": [
            {
                "client" + str(random.randint(1,9999999)): [
                    {
                        "flavor_name": "m1.tiny",
                        "image_name": "testVMSnap1",
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
                        "image_name": "testVMSnap1",
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
                        "image_name": "testVMSnap1",
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
                        "image_name": "testVMSnap1",
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

    json_object["resource"].append(metaLoggerInstance)


    a_file = open("sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()


def addMasterServer():
    updateGlobalInstance()
    a_file = open("./sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    json_object["resource"].append(masterInstance)

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


    json_object["resource"].append(chunkServer)
    json_object["resource"].append(volume)
    json_object["resource"].append(volumeAttach)


    a_file = open("sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()



def resetState():
    a_file = open("./sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    json_object["resource"] = []
    json_object["output"] = []

    a_file = open("sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

def getoutput():
    a_file = open("./sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    return json_object
