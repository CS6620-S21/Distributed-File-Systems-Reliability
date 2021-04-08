#!/bin/bash
mkdir /mnt/mfs/test7
yes A | dd of=/mnt/mfs/test7/testfile.txt bs=1000 count=1000
yes B | dd of=/mnt/mfs/test7/testfile.txt bs=1000 count=1000