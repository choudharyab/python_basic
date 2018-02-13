from math import pi
from string import maketrans
from string import Template
import math as foobar
import math
import cmath
from math import sqrt
#power
print "2**3 =",2**3
print "2 to power of 3 is",pow(2,3)

#round
print "1/2 is",1/2
print "1//2 is",1//2
print "round(1/2) is",round(1/2)
print "round(1//2) is",round(1//2)
print"round (1.0/2.0) is",round(1.0/2.0)

#module
print math.floor(32.9)
print math.ceil(32.9)
print int(math.floor(32.9))
print int(math.ceil(32.9))

#square
print sqrt(25)
print cmath.sqrt(-4)

#printing hello world program
print "Hello world!"

#Taking input from user defined
Name=raw_input("Enter your name:")
print (Name)

#string
print "Hello world!..."   #single quoted
print 'Hello world!...'     #escaping quotes
x="Good morning!"
y="How are you!!"
print x+y       #concatenating the string
temp=42
print "The temperature is  "+'temp'
print 'Hello,\nworld!...'        #Raw String
print 'C:\\anup'

#variable
a=2
print a
print long(a)    #convert string to long integer
print str(a)     #converting string to value

#Expression
y=(2**3)-(5+4)/10
print y

#indexing
greeting= "Hello"
print greeting[0]
print greeting[-1]   #taking from last digits
print greeting[1:5]    #slicing

url=raw_input("Enter your url")
print url
print url[5:9]

x=[1,2,3,4,]
y=[1,7,8]
z=["hello","world"]
print x+z


sentence=raw_input("Sentence")
Screen_width=80
text_width=len(sentence)
box_width=text_width +6
left_margin=(Screen_width-box_width)//2
print
print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'
print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
print ' ' * left_margin + '| ' + sentence + ' |'
print ' ' * left_margin + '| ' + ' ' * text_width + ' |'
print ' ' * left_margin + '+' + '-' * (box_width-2) + '+'
print

#memebership operator
database=[['alber','123'],['anup','234'],['mayur','111']]
username=raw_input('username')
pincode=raw_input('pincode')
if [username,pincode] in database:
    print 'Access Granted'

 #user_defined function
numbers=[1,89,69,34,56,45,67,45,32,234,53,2344,89]
print len(numbers)
print max(numbers)
print min(numbers)
#print del numbers[2]

#print 'anup'.join('choudhary')
#lists
list=[1,2,3]
print list
mylst= list.append(4)    #append used when we are using single element
print mylst
c=list.count(1)          #counting occurrence of events
print c
x=[3,5,6,7,4]
x.extend(list)
print x#works same as append but for many elements
list.index(2)
print list#used to find index
list.pop()
print list#used to pop the element
list.remove(2)
print list#to remove the element
list.reverse()
print list#to reverse the element
x.sort()
print x
num=[3,1,5,2,7,6]
num.sort(cmp)
print num

#string
format= "Hello %s. %s enough to do work"
value=('world','hot')
print format % value         #%s is conversion specifier
format= "The value of pi is %.3f"
print format % pi
#s=Template('$x ,very happy $x')
#s.substitute(x='well')
#print s

#Demo
width=int(input("Enter the width"))
#print width
price_width = 10
item_width = width - price_width

header_format = '%-*s%*'
format = '%-*s%*.2f'
print '='*width
print header_format %(item_width,"item",price_width,'price')
print '-'* width
print header_format %(item_width,"Apples",price_width,'0.40')
print header_format %(item_width,"Pears",price_width,'0.50')
print header_format %(item_width,"Cantaloups",price_width,'1.92')
print header_format %(item_width,"Dried Apricots(16.02",price_width,'8.00')
print header_format %(item_width,"Prunes(4lbs)",price_width,'12.00')
print '-'* width

#Translate
#transs=["hello world"]
#transs=maketrans('wo','cs')
#print transs

#Dictionary
items=[('name','anup'),('age','32')]
t=dict(items)
print t
print t.get('name')
x={'name':'arjun'}
print t.update(x)
print t.has_key('name')
print t.pop('name')
print t.popitem()
d=t.clear()   #clearing the data that is present
print d
y=t.copy()   #copying the value into next time
print y

#using module
print foobar.sqrt(16)

x,y,z=1,2,3       #unpacking squence
print x,y,z

#conditional statement
name=raw_input("Enter your name")
if(name.endswith("Anup")):
    print "Hello mrs.Anup"
else:
    print "Hello mrs.strange"

#nested if statment
number=input("Enter the number :")
if(number==0):
    print "Your number is Zero"
elif(number>0):
    print "Your number is postive"
else:
    print "your number is negative"

  #assertion
Age=int(input("Enter your age"))
assert (Age>0)            #crash your program which stop your program
print Age

#while loop
x=1
while x<=10:
    print x
    x+=1

