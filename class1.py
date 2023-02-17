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

        
    