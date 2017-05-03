#coding:utf-8

from PIL import Image
import os
import time
import subprocess
import random

curPath = os.path.split(os.path.realpath(__file__))[0]
path = os.path.join(curPath,'pic')
killcmd = 'taskkill /f /im "mspaint.exe"'
picList =[]
files = os.listdir(path)
for f in files:
    picList.append(f)
    #print f
indexlen = len(picList) -1

loop = 0        
while loop < 100:
    loop = loop +1 
    index = random.randint(0,indexlen)
    picName = picList[index]
    print "pic loading"
    destPath = os.path.join(path,picName)
    cmd = "mspaint {file}".format(file=destPath)
    child =subprocess.Popen(cmd) 
    time.sleep(5)
    print "pic show time end"
    os.system('taskkill /f /im "mspaint.exe"')
    child.kill()
        
