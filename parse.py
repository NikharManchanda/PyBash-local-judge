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

# template='~/Code/Sublime/template.cpp'
# solpath='~/Code/Sublime/solution.cpp'
template=os.path.expanduser('~/Code/PyBash-local-judge/template.cpp')
solpath=os.path.expanduser('~/Code/Sublime/solution.cpp')
solDir=os.path.expanduser('~/Code/Sublime/')
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
        
def prepend_line(file_name):
    line='/**\n'+' *    author:  Rahkin\n'+f' *    created: {dt_string} \n'+'**/\n'
    dummy_file = file_name + '.cpp'
    with open(file_name, 'r') as read_obj, open(dummy_file, 'w') as write_obj:
        write_obj.write(line + '\n')
        for line in read_obj:
            write_obj.write(line)
    os.remove(file_name)
    os.rename(dummy_file, file_name)

def make_files():
    global solDir,solpath  
    filelist = [ f for f in os.listdir(solDir) if (f.find("input.")!=-1 or f.find("output.")!=-1) ]
    for f in filelist:
        os.remove(os.path.join(solDir, f))
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

click.secho("Listening to Competitive Companion",fg='bright_green') 
CompetitiveCompanionServer.startServer('tests')
make_files()

def touch_file(file_path):   
    # Convert the provided path to a Path object
    path_object = Path(file_path)
    # Touch the file (create if it doesn't exist and update access/modification times)
    path_object.touch()

touch_file(solpath)
shutil.copyfile(template,solpath)
prepend_line(solpath)
click.secho("Test Cases Copied",fg='bright_green')

    