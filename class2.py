#dsa

#buuble sort
#neighbour element comparision and on th right highest element get fixed

def bubble_sort(a):
    print(len(a))
    for j in range(0,len(a)-1):
        for i in range(0,len(a)-1):
            if(a[i]>a[i+1]):
                temp=a[i+1]
                a[i+1]=a[i]
                a[i]=temp
            
    return a
        
        
print(bubble_sort([2,1,7,4,3]))


# for every loop lowest element is pushed to left in a sorted aray
def select_sort(a):
    for i in range(0,len(a)):
        index=i #element to compare
        for j in range(i+1,len(a)):
            if(a[index]>a[j]):
                index=j
        print(a[index])
                
        a[i],a[index]=a[index],a[i]
    return a
                        
print(select_sort([2,1,7,4,3]))


# in insertion sort every elemnt is appended to left sorted array

def insert_sort(a):
    for i in range(1,len(a)):
        j=i-1
        key=a[i]
        for j in range(i-1,-1,-1):
            print(j)
            
            if(a[j]>key):
                a[j+1]=a[j]
            else:
                break
        a[j+1]=key
    return a
        
print(insert_sort([2,1,7,4,3]))

def binary_search(ch,a):
    element_index=False
    for i in range(0,len(a)):
        if(ch==a[i]):
            element_index=True
            #return 'Element found index {}'.format(i)
    if element_index:
        return 'Elemnet found'
    else:
        return 'Not found' 
    
print(binary_search(2,[2,1,7,4,3]))