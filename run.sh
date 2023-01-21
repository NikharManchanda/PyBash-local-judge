#!/bin/bash

cd ~/Code/Sublime/cf

IN="input.#.txt"
OUT="output.#.txt"

# Limits
TL=1 # Time limit (in seconds)

# Compiling options
CPP="g++ -std=c++17 -w -O2 -DRAHKIN" # C++


# Color Codes
red='\033[0;31m'
RED='\033[1;31m'
GREEN='\033[1;32m'
green='\033[0;32m'
blue='\033[0;34m'
BLUE='\033[1;34m'
cyan='\033[0;36m'
CYAN='\033[1;36m'
NC='\033[0m' # No Color

# Cleanup on exit
rm -f .overview .compiler_report .time_info .$1.out
trap "{ rm -f .overview .compiler_report .time_info .$1.out; }" SIGINT SIGTERM EXIT

if [ $# -ne 1 ]
then
  echo "Usage: $0 source_code"
  echo "   e.g. $0 test.cpp"g++ -std=c++17 -w -O2 -DRAHKIN
  echo "   use the above to grade file test.cpp"
  exit 2
fi

# Language detection
LANG=`echo $1 | awk -F . '{print $NF}'`
if [ "$LANG" == "cpp" ]
then
  COMPILER="$CPP $1 2> .compiler_report" # C++
elif [ "$LANG" == "c" ]
then
  COMPILER="$C $1 2> .compiler_report" # C
elif [ "$LANG" == "pas" ]
then
  COMPILER="$PAS $1 2> .compiler_report" # Pascal
fi

# Compilation
echo "$COMPILER" | sh
if [ $? -ne 0 ]
then
  echo -e " ${red}X Compilation Error${NC}";
  cat .compiler_report;
  exit 1;
fi

# echo -e " ${CYAN}* Successful compilation!${NC}";

ulimit -t $TL;

rm -rf .overview;
CORRECT=0
MAX_N=50
echo
for (( i=1; i<=$MAX_N; i++))
do
  TEST_CASE_IN=`echo $IN | sed "s/#/$i/g"`
  TEST_CASE_OUT=`echo $OUT | sed "s/#/$i/g"`

  # If i-th test case doesn't exist then stop here.
  if [ ! -e $TEST_CASE_IN ]
  then
    break
  fi
  printf "${BLUE}Test case $i:${NC}";

  time -p (./a.out < $TEST_CASE_IN > .$1.out) 2> .time_info;

  EX_CODE=$?;
  if [ $EX_CODE -eq 137 ] || [ $EX_CODE -eq 152 ]
  then
    echo -e " ${red}X TLE: Time Limit Exceeded${NC}";
    # echo -n "T" >> .overview;
  elif [ $EX_CODE -ne 0 ]
  then
    echo -e " ${red}X RE: Runtime Error${NC}";
    # echo -n "E" >> .overview;
  else
    PROG_TIME=`cat .time_info | grep real | cut -d" " -f2`;
    diff -w .$1.out $TEST_CASE_OUT > /dev/null
    if [ $? -eq 0 ]
    then
      echo -e " ${GREEN}* OK${NC} [$PROG_TIME]"
      # echo -n "*" >> .overview
      CORRECT=`expr $CORRECT + 1`
    else
      echo -e " ${red}X WA${NC} [$PROG_TIME]"
      # echo -n "X" >> .overview
      echo -e "Your answer:"
      cat .$1.out
      echo
      echo -e "Exp answer:"
      cat $TEST_CASE_OUT
      echo
    fi
  fi

  echo;
done
N=`expr $i - 1`

if [ $CORRECT -eq $N ]
then
  echo -en "${GREEN}All test cases passed!!${NC}"
else
	echo -en "${red}$CORRECT / $N test cases passed${NC}"
fi
echo
echo
