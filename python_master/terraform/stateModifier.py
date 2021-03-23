import json

count = 1000000

def updatedcount():
    global count
    count = count + 1
    return count

clientServerInstance = {
    "openstack_compute_instance_v2": [
        {
            "client" + str(updatedcount()): [
                {
                    "flavor_name": "m1.tiny",
                    "image_name": "testVMSnap1",
                    "name": "client" + str(updatedcount()),
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
            "metalogger" + str(updatedcount()): [
                {
                    "flavor_name": "m1.tiny",
                    "image_name": "testVMSnap1",
                    "name": "metalogger" + str(updatedcount()),
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
            "va" + str(updatedcount()): [
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
            "chunkserver_volume" + str(updatedcount()): [
                {
                    "name": "chunkserver_volume" + str(updatedcount()),
                    "size": 10
                }
            ]
        }
    ]
}

chunkServerInstance = {
  "openstack_compute_instance_v2": [
      {
          "chunkserver" + str(updatedcount()): [
              {
                  "flavor_name": "m1.tiny",
                  "image_name": "testVMSnap1",
                  "name": "chunkserver" + str(updatedcount()),
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
            "master1" + str(updatedcount()): [
                {
                    "flavor_name": "m1.tiny",
                    "image_name": "testVMSnap1",
                    "name": "master1" + str(updatedcount()),
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



def resetState():
    a_file = open("./sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    json_object["resource"] = []

    a_file = open("sample.tf.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

