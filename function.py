#simple program
def add(x,y):
    return x+y
b=add(10,20)
print b
#######################
def expr(x,n):
    if n==0:
        return 1
    else:
        return x *expr(x,n-1)
b=expr(2,3)
print b
#########################
def square(x):
    return x*x
input=[1,2,3,4,5,6]
output=[]
for v in input:
    output.append(square(v))
    print output
