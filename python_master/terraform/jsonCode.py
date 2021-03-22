import json


def addresource():
    a_file = open("../../terraform_state/terraform.tf.json", "r")
    json_object = json.load(a_file)
    a_file.close()


    val = json_object["resource"][0]
    json_object.append(val)


    print(json_object)
    print(len(val))
    print(val)
    # json_object["resources"][0]
    #
    # a_file = open("samle_file.json", "w")
    # json.dump(json_object, a_file)
    # a_file.close()


def deleteresource():
    print("Resource deleted")


addresource()

# terraform_plan = { "openstack_compute_instance_v2":
#     [
#         {
#             "master2": [
#                 {
#                         "flavor_name": "m1.tiny",
#                         "image_name": "testVMSnap1",
#                         "name": "master1",
#                         "security_groups": [
#                             "default"
#                         ]
#                     }
#                 ]
#             }
#         ]
#     }
#
# json_object["resource"] = terraform_plan
#
#
# a_file = open("sample_file.json", "w")
# json.dump(json_object, a_file)
# a_file.close()





