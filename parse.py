import click
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import threading
import shutil
from pathlib import Path 
import os
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

template='/home/rahkin/Code/Sublime/template.cpp'
solpath='/home/rahkin/Code/Sublime/cf/solution.cpp'
solDir='/home/rahkin/Code/Sublime/cf/'
url=''
timelimit=''
memorylimit=''
problemName=''
def MakeHandlerClassFromFilename(filename):
    class HandleRequests(BaseHTTPRequestHandler):
        def do_POST(self):
            global url,timelimit,memorylimit,problemName,solDir
            try:
                content_length = int(self.headers['Content-Length'])
                body = self.rfile.read(content_length)
                tests = json.loads(body.decode('utf8'))
                problemName=tests['name']
                url=tests['url']
                memorylimit=str(tests['memoryLimit'])
                timelimit=str(tests['timeLimit'])
                tests = tests["tests"]
                ntests = []
                for test in tests:
                    ntest = {
                        "test": test["input"],
                        "correct_answers": [test["output"].strip()]
                    }
                    ntests.append(ntest)
                nfilename = solDir+ filename
                with open(nfilename, "w") as f:
                    f.write(json.dumps(ntests))
            except Exception as e:
                print("Error handling POST - " + str(e))
            threading.Thread(target=self.server.shutdown, daemon=True).start()
    return HandleRequests


class CompetitiveCompanionServer:
    def startServer(filename):
        host = 'localhost'
        port = 1327
        HandlerClass = MakeHandlerClassFromFilename(filename)
        httpd = HTTPServer((host, port), HandlerClass)
        httpd.serve_forever()
        # print("Server has been shutdown")

def prepend_line(file_name, line):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.cpp'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)

def make_files():
    global solDir,solpath  
    # Deleting prev input.* files 
    filelist = [ f for f in os.listdir(solDir) if (f.find("input.")!=-1 or f.find("output.")!=-1) ]
    for f in filelist:
        os.remove(os.path.join(solDir, f))
    # Writing tests in input.# files
    f2 = open(solDir+"tests", "r")  
    lines=f2.readlines()[0]
    f2.close()
    cases=json.loads(lines)
    testCase=0
    for case in cases:
        testCase+=1
        ans=case['correct_answers']
        input=case['test']
        if isinstance(ans, list):
            ans=ans[0].strip()
        else:
            ans=ans.strip()
        if isinstance(input, list):
            input=input[0].strip()
        else:
            input=input.strip()
        infile = Path(solDir+'input.'+str(testCase)+'.txt')
        opfile = Path(solDir+'output.'+str(testCase)+'.txt')
        with open(opfile,'w') as opfile,open(infile,'w') as infile:
            opfile.writelines(ans)
            infile.writelines(input)

# @click.command()
# def cli():
click.secho("Listening to Competitive Companion",fg='bright_green') 
CompetitiveCompanionServer.startServer('tests')
make_files()
line='/**\n'+' *    author:  Rahkin\n'+f' *    created: {dt_string} \n'+'**/\n'
myfile = Path(solpath)
myfile.touch(exist_ok=True)
f = open(myfile,'w')    
shutil.copyfile(template,myfile)
prepend_line(solpath,line)
f.close()
click.secho("Test Cases Copied",fg='bright_green')
myfile1 = Path(solDir+'url.txt')
myfile1.touch(exist_ok=True)
file1 = open(myfile1,'w')    
s=url
file1.writelines(s)
file1.close()
    # click.secho("Url Copied",fg='bright_green')    
    # pass