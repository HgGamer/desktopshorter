import json
import os
import subprocess
import sys
from pprint import pprint

with open('folders.json') as data_file:    
    data = json.load(data_file)


folder_number=len(data["folders"]);
def nop():
    0
    
def mkdir(name):
    try:
       os.mkdir(name)
    except:
        nop
        
def move(folder,extension):
    subprocess.call("move *."+extension+" "+folder,shell=True)

def removeAllEmpty():
    i=0
    while(i<len(data["folders"])):
        removeEmpty(data["folders"][i]["foldername"])
        i=i+1

def removeEmpty(d):
    print d
    try:
        os.rmdir(d)
    except:
        nop
def readfolder(i):
    if(i<len(data["folders"])):
        print(data["folders"][i]["foldername"])
    
def sorter():
    i=0
    while (i<len(data["folders"])):
        mkdir(data["folders"][i]["foldername"])
        j=0
        while(j<len(data["folders"][i]["extensions"])):
            move(data["folders"][i]["foldername"],data["folders"][i]["extensions"][j])
            j=j+1
        i=i+1

def main(argv):
    if(len(argv)>0):
        os.chdir(argv[0])
        sorter()
        removeAllEmpty()
        print "Moving to:"+argv[0]
    else:
        print "Error! Give an argument"
        
if __name__ == "__main__":
    main(sys.argv[1:])
    sys.exit()
  
    
