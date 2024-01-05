# Especially Joyful Numbers
def number_joy(n):
    return n==sum([int(i) for i in str(n)])*int(str(sum([int(i) for i in str(n)]))[::-1])

# Vowel one
def vowel_one(s):
    vovels=['a','o','u','e','i']
    result=''
    for i in s:
        if i.lower() in vovels: result+="1"
        else:result+='0'
    return result
# Squares sequence
def squares(x, n):
    if n<=0:
        return []
    nums=[]
    for i in range(n):
        nums.append(x)
        x**=2
    return nums


# Is this a valid Chess960 position?
def is_valid(positions):
    if positions[0]=="K" or positions[7]=="K":
        return False
    a, b = None, None
    for i in range(len(positions)):
        if positions[i]=='B' and a==None :
            a=i
        elif positions[i]=='B':
            b=i
    if (a+b)%2==0:
        return False
    r1,r2,k=None,None,None
    for i in range(len(positions)):
        if positions[i]=='K':
            k=i
        if positions[i]=='R' and r1==None :
            r1=i
        elif positions[i]=='R':
            r2=i

    return k > r1 and k < r2

# Unique string characters
def solve(a,b):
    c=''
    for i in a :
        if i not in b:
            c+=i
    for i in b :
        if i not in a:
            c+=i
    return c

#Disemvowel Trolls 
def disemvowel(string_):
    vovels=['a','o','u','e','i','A','E','I','U','O']
    for vov in vovels:
        string_=string_.replace(vov,'')
    return string_

# Are the numbers in order?
def in_asc_order(arr):
    if sorted(arr)==arr:
        return True
    else:
        return False
    
# Interlocking Binary Pairs
def interlockable(a, b):
    check=True
    a,b=bin(a)[::-1][:-2],bin(b)[::-1][:-2]
    for x,y in zip(a,b):
        if x=='1' and y=='1':
            check=False
    return check

# Descending Order
def descending_order(num):
    a=[]
    for i in str(num):
        a.append(i)
    a.sort()
    b=''
    while a:
        b+=a.pop()
    return int(b)

# Count the divisors of a number
def divisors(n):
    a=0
    for i in range(1,n+1):
        if n%i==0:
            a+=1
    return a

# [Geometry A-2]: Length of a vector
from math import sqrt
def vector_length(vector):
    a=vector[0]
    b=vector[1]
    lenght=sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    return lenght

# Highest and Lowest

def high_and_low(numbers):
   
    new_nums_list=[]
    pos_nums=[]
    neg_nums=[]
    raw_list_of_numbers=[]

    for num in numbers:
        raw_list_of_numbers.append(num)
    raw_list_of_numbers.append(' ')
    container=[]
    for el in raw_list_of_numbers:
        if el!=' ':
            container.append(el)
        else:
            new_nums_list.append(container)
            container=[]
    for num in new_nums_list:
        if num[0]=='-':
            neg_nums.append(num)
        else:
            pos_nums.append(num)

    nu=''
    neg_nums2=[]
    for i in neg_nums:
        for j in i:
            nu+=j
        neg_nums2.append(nu)
        nu=''
    pos_nums2=[]
    for i in pos_nums:
        for j in i:
            nu+=j
        pos_nums2.append(nu)
        nu=''

    pos_nums,neg_nums=[],[]
    for a in pos_nums2:
        a=int(a)
        pos_nums.append(a)
    for b in neg_nums2:
        b=int(b)
        neg_nums.append(b)

    pos_nums.sort()
    neg_nums.sort()
    if pos_nums and neg_nums:
        numbers=f'{pos_nums[-1]} {neg_nums[0]}'
        return numbers
    if pos_nums:
        numbers=f'{pos_nums[-1]} {pos_nums[0]}'
        return numbers
    if neg_nums:
        numbers=f'{neg_nums[-1]} {neg_nums[0]}'
        return numbers
    
# List Filtering
def filter_list(l):
    'return a new list with the strings filtered out'
    list=[]
    for i in l:
        if type(i)==int:
            list.append(i)
    return list        

# If you can't beat 'em, join 'em!
def cant_beat_so_join(numbers):
    for _ in range(len(numbers)):
        for i in range(len(numbers)):
            if i==len(numbers)-1:pass
            else:
                if sum(numbers[i]) < sum(numbers[i+1]):
                    numbers[i],numbers[i+1] = numbers[i+1], numbers[i]
    numbers = [i for sub in numbers for i in sub]
    return numbers
# Is this a triangle?
def is_triangle(a, b, c):
    return a>0 and b>0 and c>0 and a+b>c and a+c>b and c+b>a
