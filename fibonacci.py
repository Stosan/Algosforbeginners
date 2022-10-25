#fibonacci algorithm

"""
1. print out a number from a range
2. each number is the previous two numbers added together

"""

a,b=0,1
for i in range(0,10):
    print(a)
    a,b=b,a+b


#fibonacci with generator
def fibonacci(num):
    a,b=0,1
    for i in range(0,num):
        yield  "{}:{}".format(i+1,a)
        a,b=b,a+b

for item in fibonacci(10):
    print(item)
