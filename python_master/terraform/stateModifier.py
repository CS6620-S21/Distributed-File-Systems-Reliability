import json
import random
import time


clientServerInstance = {
    "openstack_compute_instance_v2": [
        {
            "client" + str(random.randint(1, 99999)): [
                {
                    "flavor_name": "m1.tiny",
                    "image_name": "testVMSnap1",
                    "name": "client" + str(random.randint(1, 99999)),
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
            "metalogger" + str(random.randint(1, 99999)): [
                {
                    "flavor_name": "m1.tiny",
                    "image_name": "testVMSnap1",
                    "name": "metalogger" + str(random.randint(1, 99999)),
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
            "va" + str(random.randint(1, 99999)): [
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
            "chunkserver_volume" + str(random.randint(1, 99999)): [
                {
                    "name": "chunkserver_volume" + str(random.randint(1, 99999)),
                    "size": 10
                }
            ]
        }
    ]
}

chunkServerInstance = {
  "openstack_compute_instance_v2": [
      {
          "chunkserver" + str(random.randint(1, 99999)): [
              {
                  "flavor_name": "m1.tiny",
                  "image_name": "testVMSnap1",
                  "name": "chunkserver" + str(random.randint(1, 99999)),
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
            "master1" + str(random.randint(1, 99999)): [
                {
                    "flavor_name": "m1.tiny",
                    "image_name": "testVMSnap1",
                    "name": "master1" + str(random.randint(1, 99999)),
                    "security_groups": [
                        "default"
                    ]
                }
            ]
        }
    ]
}

def addClientServer():
    a_file = open("./sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    json_object["resource"].append(clientServerInstance)
    print(json_object)

    a_file = open("sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()



def addMetalogger():
    a_file = open("./sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    json_object["resource"].append(metaLoggerInstance)
    print(json_object)

    a_file = open("sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()


def addMasterServer():
    a_file = open("./sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    json_object["resource"].append(masterInstance)
    print(json_object)

    a_file = open("sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()



def addChunkServer():

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


def addresource():
    a_file = open("./sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()


    ll = json_object["resource"][0]
    json_object["resource"].pop()
    print(json_object)
    a_file = open("sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()


def deleteresource(id):
    a_file = open("./sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    print("Resource deleted")


def resetState():
    a_file = open("./sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    json_object["resource"] = []

    a_file = open("sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()
