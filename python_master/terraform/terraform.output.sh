#!/usr/bin/env bash

cd terraform
terraform output -json | tee output.json | grep bar
