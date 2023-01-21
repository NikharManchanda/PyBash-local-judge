import click
import shutil
from pathlib import Path 
import os
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

template='/home/rahkin/Code/Sublime/template.cpp'
solpath='/home/rahkin/Code/Sublime/cf/solution.cpp'

def prepend_line(file_name, line):
    dummy_file = file_name + '.cpp'
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        write_obj.write(line + '\n')
        for line in read_obj:
            write_obj.write(line)
    os.remove(file_name)
    os.rename(dummy_file, file_name)

line='/**\n'+' *    author:  Rahkin\n'+f' *    created: {dt_string} \n'+'**/\n'
myfile = Path(solpath)
myfile.touch(exist_ok=True)
with open(myfile,'w'):
    shutil.copyfile(template,myfile)
prepend_line(solpath,line)
click.secho("Template Copied",fg='bright_green')
