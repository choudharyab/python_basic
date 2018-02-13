import math

num=int(input("Enter the 4 digit numbers"))


def perfectsquare(n):
    return not n % n** 0.5





hundred = (num // 100)
print hundred
print math.sqrt(hundred)
#print hundred
hun=(num%100)
print hun
print math.sqrt(hun)
print math.sqrt(num)
#print hun
#print hundred
#print hun


def check():
    if(hundred==True and hun==True):
          if(num==True):
              print "your 4 digit is pefect square"
          else:
              print "Perfect square"
    else:
        print " it is not perfect square"


if len(str(num))==4:
 if len(str(hundred))==2 or  len(str(hun))==2:

        try:
         perfectsquare(hun)
         perfectsquare(hundred)
        except ZeroDivisionError:
         #check1()
         hundred=True
         hun=True

        if(len(str(num))==4):



                perfectsquare(num)
                check()




else:
  print "Its insufficient digits"
