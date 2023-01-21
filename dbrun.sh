#!/usr/bin/bash
cd ~/Code/Sublime/cf
g++ -std=c++17 -w -O2 -DRAHKIN solution.cpp
echo
./a.out < debug.txt     
echo
