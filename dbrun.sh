#!/usr/bin/bash
red='\033[0;31m'
RED='\033[1;31m'
GREEN='\033[1;32m'
green='\033[0;32m'
blue='\033[0;34m'
BLUE='\033[1;34m'
cyan='\033[0;36m'
CYAN='\033[1;36m'
NC='\033[0m' # No Color
cd ~/Code/Sublime/cf
g++ -std=c++17 -w -O2 -DRAHKIN solution.cpp
# MAX_N=50
IN="debug.txt"
echo
# for (( i=1; i<=1; i++)) do
#   TEST_CASE_IN=`echo $IN | sed "s/#/$i/g"`
#   # If i-th test case doesn't exist then stop here.
#   if [ ! -e $TEST_CASE_IN ]
#   then
#     break
#   fi
# 	echo -e "${CYAN}Test Case $i:${NC}"
./a.out < debug.txt     
echo
