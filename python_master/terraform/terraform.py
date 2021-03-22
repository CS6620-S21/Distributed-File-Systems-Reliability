import jsonCode
import os
import subprocess


# The driver scripts
# subprocess.call(['sh', './terraform.runner.sh'])
# subprocess.call(['sh', './terraform.destroy.sh'])

def init():
    os.system("terraform init")


def run():
    subprocess.call(['sh', './terraform.runner.sh'])


def destroy():
    subprocess.call(['sh', './terraform.destroy.sh'])


# subprocess.call(['sh', './terraform.runner.sh'])

# Text
# os.system('terraform init')
# os.system('terraform init')
# os.system('terraform destroy')
# os.system('terraform plan')
# mnt/C/Users/aksha/PycharmProjects/terraform
