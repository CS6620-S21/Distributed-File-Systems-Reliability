#!/usr/bin/env bash



# Make a copy of this file, add it to your git ignore and use that for testing do not ever add credentials here
# Do not commit


terraform plan

#terraform output

echo "yes" | terraform apply

#echo "yes" | terraform destroy

