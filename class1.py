def reverse_number(x):
    xstring=str(x)
    y=""
    for i in xstring:
        y=i+y
    
    return int(y)

print(reverse_number(123))


def temp_convertor(celsius):
    f=celsius*1.8+32
    return f


print(temp_convertor(37))
      
def leap_year(y):
    if (y % 4 == 0):
        return ("it is a leap year")
    else:
        return("Not leap year")
        
print(leap_year(1992))

def factorial(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)
        
print(factorial(4))


def freq_string(ch,s):
    occ=0
    for i in s:
        if(i==ch):
            occ+=1
    return occ

print(freq_string('a','aabcg'))

def comm_element(a,b):
    commelem_arr=[]
    for i in a:
        if i in b:
            commelem_arr.append(i)
    
    return commelem_arr

print(comm_element([1,2,3],[2,4,6]))

def fib_num(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib_num(n-1)+fib_num(n-2)

print(fib_num(4))

def prime_numbers(n):
    primen=[1]
    for i in range(1,n-1):
        occ=0
        for j in range(2,i):
            if(i%j==0):
                occ+=1
        if(occ>0):
            primen.append(i)
    return primen

print(prime_numbers(6))

def palin(s):
    rev_s=''
    for i in s:
        rev_s=i+rev_s
    if rev_s==s:
        return 'String is palindrome'
 
    
print(palin('eee'))

        
    