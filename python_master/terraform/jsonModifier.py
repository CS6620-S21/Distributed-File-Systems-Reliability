import json
import random

masterInstance = {
    "openstack_compute_instance_v2": [
        {
            "master1" + str(random.randint(1,99999)): [
                {
                    "flavor_name": "m1.tiny",
                    "image_name": "testVMSnap1",
                    "name": "master1" + str(random.randint(1,99999)),
                    "security_groups": [
                        "default"
                    ]
                }
            ]
        }
    ]
}

def addMasterInstance():
    a_file = open("./sample.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()

    json_object["resource"].append(masterInstance)
    print(json_object)

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

def deleteresource():
    print("Resource deleted")
