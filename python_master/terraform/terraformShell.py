
# This file interact with the shell script for the terraform
# These shell files just contains the command required to be triggered for terraform to function

import os
import subprocess

def init():
    subprocess.call(['sh', './terraform/terraform.starter.sh'], cwd="/terraform")

def run():
    subprocess.call(['sh', './terraform/terraform.runner1.sh'], cwd="/terraform")


def destroy():
    subprocess.call(['sh', './terraform/terraform.destroy1.sh'], cwd="/terraform")

def output():
    subprocess.call(['sh', './terraform/terraform.output.sh'], cwd="/terraform")

