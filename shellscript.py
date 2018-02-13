import os
import shutil
from os import path
#from  Zipfile import ZipFile
import urllib2
from shutil import make_archive
from datetime import date, time, timedelta, datetime
import time
print os.name       #Tell you the name of the os name
file="anup.txt"
print "items exists=====>"+str(path.exists(file))
print "Item is file======>"+str(path.isfile(file))
print "Item is a directory======>"+str(path.isdir(file))
print "item;s path=====>"+str(path.realpath(file))                  # tell you the direcotry of your file name with filename
print "item path name=====>"+str(path.split(path.realpath(file)))   #te3ll you the directory of your file
t=time.ctime(path.getmtime(file))
print t
#p=datetime.datetime.fromtimestamp(path.getmtime("anup.txt"))
#print p
if path.exists(file):
    src=path.realpath(file)    #get the path to the file in the current directory
head,tail=path.split(src)        #separate the path from file
print "path==>"+head
print "file===>"+tail
dst=src + ".bak"       #
shutil.copy(src,dst)
#shutil.make_archive(file,"Zip",root_dir)
#os.rename(file,"anup.txt")

web=urllib2.urlopen("https://www.youtube.com")
print "result code "+str(web.getcode())