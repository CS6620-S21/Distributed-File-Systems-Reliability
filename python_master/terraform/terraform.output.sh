#!/usr/bin/env bash

terraform output -json | tee output.json | grep bar
