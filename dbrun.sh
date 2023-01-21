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
echo -e "${CYAN}Test Case:${NC}"
cat debug.txt
echo 
echo -e "${CYAN}Your Answer:${NC}"
./a.out < debug.txt
echo
