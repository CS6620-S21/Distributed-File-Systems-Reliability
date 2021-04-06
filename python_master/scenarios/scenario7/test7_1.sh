#!/bin/bash
mkdir /mnt/mfs/test7
yes A | dd of=/mnt/mfs/test7/testfile.txt bs=10 count=1000
