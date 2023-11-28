ZSH_THEME="powerlevel10k/powerlevel10k"

plugins=(
	git
zsh-autosuggestions
)

# My custom functions for CP
dbrun(){
 cd ~/Code/PyBash-local-judge/;
 ./dbrun.sh;
}
run(){
 cd ~/Code/PyBash-local-judge/;
 ./run.sh solution.cpp;
}
parse(){
 cd ~/Code/PyBash-local-judge/;
 python3 parse.py;
 cd ~/Code/Sublime/;
 subl solution.cpp;
}
temp(){
 cd ~/Code/PyBash-local-judge/;
 python3 temp.py;
 cd ~/Code/Sublime/;
 subl solution.cpp;
}
