import re
'''
a="hello i am your good friend"
pattern=re.findall(r'^\w+',a)
r1=re.findall(r'\W+',a)
print r1
print (re.split(r'\s',a))
print (re.split(r's',a))
print (re.split(r'\S',a))
print pattern


list = ["guru99 get", "guru99 give", "guru Selenium"]
print list
for element in list:
    #print element
    z=re.match("(g\w+)\W(g\w+)", element)
   # print z.group()
    if z:
     print z.group()

patterns = [ 'software testing', 'guru99' ]
text = 'software testing is fun?'
for pattern in patterns:
 print 'Looking for "%s" in "%s" ->' % (pattern, text)
if re.search(pattern,  text):
	 print 'found a match'
else:
	 print 'no match'

email=raw_input("Enter your email address")
abc=re.findall(r'[\w\.-]+@[\w\.-]+',email)
if abc:
    print abc
'''
############################################
f=open("anup.txt","r")
if f.mode=='r':
    contents=f.read()
    print contents

#for i in range(2):
 #   f.write("This is appended line %d\r\n" %(i+1))
f.close()