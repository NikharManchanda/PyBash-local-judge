#!/usr/bin/bash
CYAN='\033[1;36m'
NC='\033[0m' # No Color
cd ~/Code/Sublime/
g++ -std=c++17 -w -O2 -DRAHKIN solution.cpp
echo -e "${CYAN}Test Case:${NC}"
touch debug.txt
cat debug.txt
echo 
echo -e "${CYAN}Your Answer:${NC}"
./a.out < debug.txt
echo
