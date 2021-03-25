
import os
import subprocess

def init():
    os.system("terraform init")

def run():
    subprocess.call(['sh', 'terraform.runner1.sh'])


def destroy():
    subprocess.call(['sh', 'terraform.destroy1.sh'])

def output():
    subprocess.call(['sh', 'terraform.output.sh'])

