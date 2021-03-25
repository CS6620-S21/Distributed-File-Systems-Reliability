
import os
import subprocess

def init():
    os.system("terraform init")

def run():
    subprocess.call(['sh', './terraform/terraform.runner1.sh'])


def destroy():
    subprocess.call(['sh', './terraform/terraform.destroy1.sh'])

def output():
    subprocess.call(['sh', './terraform/terraform.output.sh'])

