
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


output "instance_ip_addr" {
  value = "aws_instance.server.private_ip"
}
resource "openstack_compute_instance_v2" "test" {
  provider        =  "openstack"
  name            = "test-vm"
  image_name      = "centos-8-x86_64"
  flavor_name     = "m1.tiny"
  security_groups = ["default"]

}
