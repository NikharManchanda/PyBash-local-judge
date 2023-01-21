ZSH_THEME="powerlevel10k/powerlevel10k"

plugins=(
	git
zsh-autosuggestions
)

alias subl='"/mnt/c/Program Files/Sublime Text/subl.exe"'

# My custom functions for CP
dbrun(){
 cd ~/Code/Bash-local-judge-main/;
 ./dbrun.sh;
}
run(){
 cd ~/Code/Bash-local-judge-main/;
 ./run.sh solution.cpp;
}
parse(){
 cd ~/Code/Bash-local-judge-main/;
 python3 parse.py;
 cd ~/Code/Sublime/cf/;
 subl solution.cpp;
}
temp(){
 cd ~/Code/Bash-local-judge-main/;
 python3 temp.py;
 cd ~/Code/Sublime/cf/;
 subl solution.cpp;
}
