#coding:utf-8

from PIL import Image
import os
import time
import subprocess



if __name__ == '__main__':
    while (1):
        child =subprocess.Popen("python showpicsignle.py") 
        print child.pid
        time.sleep(8)
        child.kill()
        os.system('taskkill /f /im "mspaint.exe"')
        print "pic killed"
         
        
