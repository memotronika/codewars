# Find the unique number
from collections import Counter

def find_uniq(arr):
    counts = Counter(arr)
    for num in arr:
        if counts[num] == 1:
            return num
    return -1

# Lowest product of 4 consecutive numbers
def lowest_product(input: str):
    if len(input)<4: return "Number is too small"
    qq=6561
    for i in range(len(input)-3):
        a=list(input[i:i+4])
        print(a)
        b=1
        for j in a:
            b*=int(j)
        if b<qq:qq=b
    return qq

# PhoneWords
def phone_words(string_of_nums: str):
    string_of_nums=string_of_nums.replace('222','c').replace('22','b').replace('2','a')
    string_of_nums=string_of_nums.replace('333','f').replace('33','e').replace('3','d')
    string_of_nums=string_of_nums.replace('444','i').replace('44','h').replace('4','g')
    string_of_nums=string_of_nums.replace('555','l').replace('55','k').replace('5','j')
    string_of_nums=string_of_nums.replace('666','o').replace('66','n').replace('6','m')
    string_of_nums=string_of_nums.replace('7777','s').replace('777','r').replace('77','q').replace('7','p')
    string_of_nums=string_of_nums.replace('888','v').replace('88','u').replace('8','t')
    string_of_nums=string_of_nums.replace('9999','z').replace('999','y').replace('99','x').replace('9','w')
    string_of_nums=string_of_nums.replace('0',' ').replace('1','')
    return string_of_nums

# Even Fibonacci Sum
def even_fib(m):
    if m<2: return 0
    nums=[0,1]
    n=nums[-1]+nums[-2]
    suu=[]
    while n<m:
        n=nums[-1]+nums[-2]
        nums.append(n)
        if n%2==0:
            suu.append(n)
    return sum(suu) if suu[-1] < m else sum(suu[:-1])

# Happy numbers
def is_happy(n):
    was=[]
    while n!=1:
        n=sum(int(i)*int(i) for i in str(n))
        if n in was: return False
        was.append(n)
    return True

# Pyramid Array
def pyramid(n):
    
    qwerty=[]
    for i in range(n+1):
        yo=[]
        for b in range(1,i+1):
            yo.append(1)
        qwerty.append(yo)
    return qwerty[1::]

# Delete occurrences of an element if it occurs more than n times
def delete_nth(order,max_e):
    uniques=set(order)
    final=[]
    for number in uniques:
        counter=0
        for i in range(len(order)):
            if number==order[i] and counter!=max_e:
                counter+=1

            elif number==order[i] and counter==max_e:
                order[i]=None
    while None in order:
        order.remove(None)
    return order

# Write Number in Expanded Form - Part 2
def expanded_form(num):
    aa=str(num).split('.')
    num=int(aa[0])
    num1=(aa[1]) if len(aa)==2 else ''

    nums=[i for i in str(num)[-1::-1]]
    for i in range(len(nums)):
        nums[i]=int(nums[i])*(10**i)
    while 0 in nums:
        nums.remove(0)
    nums.sort(reverse=True)
    q=''.join([str(i)+' + ' for i in nums])

    nums1=[i for i in (num1)]
    for i in range(len(nums1)):
        nums1[i]=str(int(nums1[i])/(10**(i+1)))
    while '0.0' in nums1:
        nums1.remove('0.0')
    
    f=''
    for i in nums1:
        if 'e' not in i:
            f+=(i[-1]+'/'+str(10**(len(i)-2)) + ' + ')
        else:
            f+=(i[0]+'/'+str(10**(int(i[-1])))+' + ')
    return q+f[:-3]

# Write Number in Expanded Form
def expanded_form(num):
    nums=[i for i in str(num)[-1::-1]]
    for i in range(len(nums)):
        nums[i]=int(nums[i])*(10**i)
    while 0 in nums:
        nums.remove(0)
    nums.sort(reverse=True)
    return (''.join([str(i)+' + ' for i in nums]))[:-3]

# Convert string to camel case
def to_camel_case(text: str):
    words=[i for i in text]
    while '-' in words or '_' in words:
        for i in range(len(words)):
            if words[i]=='-' or words[i]=='_':
                words[i+1]=words[i+1].upper()
                words.remove(words[i])
                break
    result=''
    for i in words:
        result+=i
    return result

# Create Phone Number
def create_phone_number(n):
    p1,p2,p3='','',''
    for i in range(len(n)):
        if len(p1)<3:
            p1+=str(n[i])
        elif len(p2)<3:
            p2+=str(n[i])
        else:
            p3+=str(n[i])
    return f'({p1}) {p2}-{p3}'

# Does my number look big in this?
def narcissistic( value ):
    return sum([(int(i)**len(str(value))) for i in str(value)])==value

# Persistent Bugger.
def persistence(n):
    result=0
    while n>9:
        n=str(n)
        a=[]
        for i in n:
            a.append(i)
        b=1
        for i in a :
            b*=int(i)
        n=int(b)
        result+=1
    return result

# Validate Credit Card Number
def validate(n):
    nums=[]
    while n:
        nums.append(n%10)
        n//=10
    for i in range(len(nums)):
        if i%2:
            nums[i]*=2
            if nums[i]>9:
                nums[i]-=9
    return(sum(nums)%10==0)

#Multiples of 3 or 5
def solution(number):
    return sum(i for i in range(number) if i%3==0 or i%5==0)

# Make the Deadfish Swim
def parse(data):
    a=[]
    b=0
    for i in data:
        if i == 'i':
            b+=1
        if i == 'd':
            b-=1
        if i == 's':
            b**=2
        if i == 'o':
            a.append(b)
    return a

#  Calculate the area of a regular n sides polygon inside a circle of radius r
import math
def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    side=2*circle_radius*math.sin(math.radians(180/number_of_sides))
    r=circle_radius*math.cos(math.radians(180/number_of_sides))
    P=number_of_sides*side
    return round((P*r)/2,3)

# Break camelCase
def solution(s):
    new_line=''
    for i in s:
        if i == i.upper():
            new_line+=' '
        new_line+=i
    return new_line

# Unique In Order
def unique_in_order(iterable):
    new_list=[]
    for every in iterable:
        if len(new_list)==0:
            new_list.append(every)
        else:
            if new_list[-1]!=every:
                new_list.append(every)
    return new_list

#Length of missing array
def get_length_of_missing_array(array_of_arrays):
    if array_of_arrays == [] or None in array_of_arrays or [] in array_of_arrays:return 0     
    newarr=[]
    for i in array_of_arrays:
        newarr.append(len(i))
    newarr.sort()
    for i in range(len(newarr)):
        if i == 0:pass
        elif newarr[i]-newarr[i-1] != 1: return newarr[i]-1
