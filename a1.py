import os
import shutil
import os.path
print os.getcwd()
print __file__

#fileDir = os.path.dirname(os.path.realpath('__file__'))
#print fileDir
'''
filename="aa.txt"
if filename in fileDir:
     print "exists"
else:
    print " not Exists"

'''
#fname="aa.txt.txt"
path = os.getcwd()
dirList = os.listdir(path)
for fname in dirList:
      print fname
fname="aa.txt.txt"
if fname  in dirList:
   print "exists"
else:
    print "not exists"
