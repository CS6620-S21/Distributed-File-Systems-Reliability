cd /mnt/mfs/
mfssetgoal -r 2 /mnt/mfs
mkdir scenario2_test_2
touch scenario2_test_2/testfile.txt
base64 /dev/urandom | head -c 10240000 > scenario2_test_2/testfile.txt