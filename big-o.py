#Big-O Notation

"""
“Big O notation is a mathematical notation that describes the limiting behavior 
of a function when the argument tends towards a particular value or infinity. 
It is a member of a family of notations invented by Paul Bachmann,Edmund Landau, and others,
collectively called Bachmann–Landau notation or asymptotic notation.”
1. Linear time 0(n) complexity increases linearly as input size increases
2. Log time 0(log n) complexity increases and then stops as input size increases, it is the most efficient and scalable
3. exponential 0(2n) is the opposite of linear time complexity, it increases and rapidly grows as input size increases, it is not efficient and scalable
4. Quadratic time 0(n²) complexity increases in relation to input size increases
5. Constant time 0(1) complexity does not respond to time increase as input size increases.
"""

def linear(num_list):
    """
    This function can recieve list input that can increase to infinity
    We're more concerned with how it runs at constant time because execution speed can differ from 
    computer to computer.
    For this we will use the big-0 of 1, 0(1)
    """
    return num_list[0] #runs at 0(1), 1 being a constant time of one operation

lst = [1,3,2,4,6,5,7,4]
print(linear(lst))


def linearofn(num_list):
    """
    This function can recieve list input that can increase to infinity
    Since we have a for loop operation, we're more concerned with how it runs at linear time.
    For this we will use the big-0 of n, 0(n)
    """
    for i in num_list: #runs at 0(n), n being the size of the loop
        return i



def linearofnplus(num_list):
    """
    This function can recieve list input that can increase to infinity
    Since we have a for loop operation, we're more concerned with how it runs at linear time.
    For this we will use the big-0 of n, 0(n)
    """
    #the cumulative time complexity of this algorithm is 0(1+n+1), which is 0(2+n), simplified by dropping the constants, 0(n)
    print(num_list[0]) # 0(1)
    for i in num_list: #runs at 0(n), n being the size of the loop
        return i
    print(num_list) # 0(1)




def linearofdoublen(num_list):
    """
    This function can recieve list input that can increase to infinity
    Since we have a for loop operation, we're more concerned with how it runs at linear time.
    For this we will use the big-0 of n, 0(n)
    """
    #the cumulative time complexity of this algorithm is 0(n+n), which is 0(2n), simplified by dropping the constants, 0(n)
    for i in num_list: #runs at 0(n), n being the size of the loop
        return i

    for i in num_list: #runs at 0(n), n being the size of the loop
        return i



def linearofdoublen(num_list,string_list):
    """
    This function can recieve input of two list that can increase to infinity
    Since we have a for loop operation, we're more concerned with how it runs at linear time.
    For this we will use the big-0 of n, 0(n)
    """
    #the cumulative time complexity of this algorithm is 0(n+m), simplified by dropping the constants, 0(n)
    for i in num_list: #runs at 0(n), n being the size of the loop
        return i

    for i in string_list: #runs at 0(m), m being the size of the loop, we use m to distinguish between both loops
        return i


def linearofnestedn(num_list,string_list):
    """
    This function can recieve list input that can increase to infinity
    Since we have a nested for loop operation, we're more concerned with how it runs at linear time.
    For this we will use the big-0 of n, 0(n)
    """
    #the cumulative time complexity of this algorithm is 0(n*n), simplified by dropping the constants, 0(n²)
    #0(n²) are slower
    for i in num_list: #runs at 0(n), n being the size of the loop
        for k in string_list: #runs at 0(n), m being the size of the loop, we use m to distinguish between both loops
            return k

def linearofdoublenplusn(num_list,string_list):
    """
    This function can recieve list input that can increase to infinity
    Since we have a nested for loop operation, we're more concerned with how it runs at linear time.
    For this we will use the big-0 of n, 0(n)
    """
    #the cumulative time complexity of this algorithm is 0(n+n*n),we focus on the approximation, simplified by dropping the n, 0(n²)
    #0(n²) are slower
    for i in num_list: #runs at 0(n), n being the size of the loop
        return i
    for i in num_list: #runs at 0(n), n being the size of the loop
        for k in string_list: #runs at 0(n), m being the size of the loop, we use m to distinguish between both loops
            return k

def linearoftriplen(num_list,string_list):
    """
    This function can recieve list input that can increase to infinity
    Since we have a nested for loop operation, we're more concerned with how it runs at linear time.
    For this we will use the big-0 of n, 0(n)
    """
    #the cumulative time complexity of this algorithm is 0(n*n*n),simplified by dropping the n, 0(n³)
    #0(n²) are slower
    for i in num_list: #runs at 0(n), n being the size of the loop
        for k in string_list: #runs at 0(n), m being the size of the loop, we use m to distinguish between both loops
            for j in string_list: #runs at 0(n), m being the size of the loop, we use m to distinguish between both loops
                return j




lst = [1,3,2,4,6,5,7,4]
print(linear(lst))


def print_all_codes(n,m):
    """
    cumulatively, 0(2+n²), which is 0(n²)
    """
    def print_01_codes(current,num_digits):
        if num_digits == 0:
            pass
        print_01_codes("0"+current,num_digits-1) #0(1)
        print_01_codes("1"+current,num_digits-1) #0(1)

    upper_bound=0
    #0(n²)
    while True: #0(n)
        for i in range(upper_bound): #0(n)
            print_01_codes('',n)
        if upper_bound>m:
            break
        upper_bound+=1