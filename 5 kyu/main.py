# Valid Parentheses
def valid_parentheses(string):
    qwa=[i for i in string if i=='(' or i==')']
    while qwa and '(' in qwa:
        if qwa[0]==')' or qwa[-1]=='(':return False
        qwa.remove('(')
        try:
            qwa.remove(')')
        except ValueError:
            return False
    return True if len(qwa)==0 else False
  

# Not very secure
def alphanumeric(password:str):
    if password=='': return False
    for i in password:
        if i.isdigit() or i.isalpha():continue
        else:return False
    return True

# The Hashtag Generator
def generate_hashtag(s):
    if s=='': return False
    s, tag=s.split(' '),'#'
    while '' in s: s.remove('')
    for i in s:
        tag+=i.title() 
    return False if len(tag)>140 else tag

# Human Readable Time
def make_readable(seconds):
    hh = seconds//3600
    seconds=seconds-(hh*3600)
    mm=seconds//60
    seconds=seconds-(mm*60)
    ss=seconds
    hh,mm,ss=str(hh),str(mm),str(ss)
    if len(hh)==1: hh='0'+hh
    if len(mm)==1: mm='0'+mm
    if len(ss)==1: ss='0'+ss

    return f'{hh}:{mm}:{ss}'

# Product of consecutive Fib numbers
def productFib(prod):
    num1, num2 = 0, 1
    while num1*num2 != prod:
        num1, num2 = num2, num1+num2
        if num1*num2>prod:return [num1,num2,False]
    return[num1,num2,True]

#RGB To Hex Conversion
def rgb(*pack):
    pack2=[]
    for i in pack:
        if i<0:
            i=0
        if i>255:
            i=255
        if len(hex(i))==4:
            i=hex(i)[2:]
        else:
            i='0'+hex(i)[2:]
        pack2.append(i)
    return f'{pack2[0].upper()}{pack2[1].upper()}{pack2[2].upper()}'

#  
# 
# 
# 
# 
# 
