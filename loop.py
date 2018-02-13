############################
numbers=[1,3,4,5,6,2,3,4,5]
sum=0
for i in  numbers:
    sum+=i
    print sum
print "Total sum is ",sum

#############################
digit=[1,3,4,2,5]
for i in digit:
    print i
else:
    print "no data item left"

#############################
num=int(input("Enter your favourite number"))
if num>1:
    for i in range(2,num):
        if(num%i)==0:
            print "it not prime number"
            break
    else:
     print "it is prime number"
else:
 print "it is not prime number"

 #############################################
 num=int(input("Enter the number"))