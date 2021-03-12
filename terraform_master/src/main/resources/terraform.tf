# Define required providers
terraform {
  required_version = ">= 0.14.0"
  required_providers {
    openstack = {
      source  = "terraform-provider-openstack/openstack"
      version = "~> 1.35.0"
    }
  }
}


provider "openstack" {
}


resource "openstack_compute_instance_v2" "master1" {
  name            = "master1"
  image_name      = "ansibleChildnodeVMSnap101"
  flavor_name     = "m1.tiny"
  security_groups = ["default"]
}

resource "openstack_compute_instance_v2" "metalogger1" {
  name            = "metalogger1"
  image_name      = "ansibleChildnodeVMSnap101"
  flavor_name     = "m1.tiny"
  security_groups = ["default"]
}

resource "openstack_compute_instance_v2" "client1" {
  name            = "client1"
  image_name      = "ansibleChildnodeVMSnap101"
  flavor_name     = "m1.tiny"
  security_groups = ["default"]
}

resource "openstack_compute_instance_v2" "client2" {
  name            = "client2"
  image_name      = "ansibleChildnodeVMSnap101"
  flavor_name     = "m1.tiny"
  security_groups = ["default"]
}

resource "openstack_compute_instance_v2" "client3" {
  name            = "client3"
  image_name      = "ansibleChildnodeVMSnap101"
  flavor_name     = "m1.tiny"
  security_groups = ["default"]
}


resource "openstack_compute_instance_v2" "chunkserver1" {
  name            = "chunkserver1"
  image_name      = "centos-8-x86_64"
  flavor_name     = "m1.tiny"
  security_groups = ["default"]
}

resource "openstack_compute_instance_v2" "chunkserver2" {
  name            = "chunkserver2"
  image_name      = "centos-8-x86_64"
  flavor_name     = "m1.tiny"
  security_groups = ["default"]
}


resource "openstack_compute_instance_v2" "chunkserver3" {
  name            = "chunkserver3"
  image_name      = "centos-8-x86_64"
  flavor_name     = "m1.tiny"
  access_ip_v4    = "10.10.10.69"
  security_groups = ["default"]
}

resource "openstack_blockstorage_volume_v2" "chunkserver1_volume" {
  name = "chunkserver1_volume"
  size = 5
}

resource "openstack_blockstorage_volume_v2" "chunkserver2_volume" {
  name = "chunkserver2_volume"
  size = 5
}

resource "openstack_blockstorage_volume_v2" "chunkserver3_volume" {
  name = "chunkserver3_volume"
  size = 5
}

resource "openstack_compute_volume_attach_v2" "va_1" {
  instance_id = "${openstack_compute_instance_v2.chunkserver1.id}"
  volume_id   = "${openstack_blockstorage_volume_v2.chunkserver1_volume.id}"
}

resource "openstack_compute_volume_attach_v2" "va_1" {
  instance_id = "${openstack_compute_instance_v2.chunkserver2.id}"
  volume_id   = "${openstack_blockstorage_volume_v2.chunkserver2_volume.id}"
}

resource "openstack_compute_volume_attach_v2" "va_1" {
  instance_id = "${openstack_compute_instance_v2.chunkserver3.id}"
  volume_id   = "${openstack_blockstorage_volume_v2.chunkserver3_volume.id}"
}


