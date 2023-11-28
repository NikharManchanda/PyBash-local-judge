import click
import shutil
from pathlib import Path
import os
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

template=os.path.expanduser('~/Code/PyBash-local-judge/template.cpp')
solpath=os.path.expanduser('~/Code/Sublime/solution.cpp')

def prepend_line(file_name):
    line='/**\n'+' *    author:  Rahkin\n'+f' *    created: {dt_string} \n'+'**/\n'
    dummy_file = file_name + '.cpp'
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        write_obj.write(line + '\n')
        for line in read_obj:
            write_obj.write(line)
    os.remove(file_name)
    os.rename(dummy_file, file_name)

def touch_file(file_path):   
    # Convert the provided path to a Path object
    path_object = Path(file_path)
    # Touch the file (create if it doesn't exist and update access/modification times)
    path_object.touch()

touch_file(solpath)
shutil.copyfile(template,solpath)
prepend_line(solpath)
click.secho("Template Copied",fg='bright_green')
