# Strip Comments
def strip_comments(strng: str, markers):
    strng=strng.split('\n')
    for j in markers:
        for i in range(len(strng)):
            strng[i]=strng[i].split(j)
            strng[i]=strng[i][0].rstrip()
    formated=''
    for i in strng:
        formated=formated+i+'\n'
    return  formated[:-1:]

# Human readable duration format
def format_duration(seconds):
    if seconds==0: return 'now'
    years=seconds//31_536_000
    seconds-=years*31_536_000
    days=seconds//86_400
    seconds-=days*86_400
    hours=seconds//3600
    seconds-=hours*3600
    minutes=seconds//60
    seconds-=minutes*60
    times=[]
    if years: years=f'{years} year'+'s'if years>1 else'1 year'
    if days: days=f'{days} day'+'s'if days>1 else'1 day'
    if hours: hours=f'{hours} hour'+'s'if hours>1 else'1 hour'
    if minutes: minutes=f'{minutes} minute'+'s'if minutes>1 else'1 minute'
    if seconds: seconds=f'{seconds} secon'+'ds'if seconds>1 else '1 second'
    times.append(years)
    times.append(days)
    times.append(hours)
    times.append(minutes)
    times.append(seconds)
    while 0 in times:
        times.remove(0)
    signs=[]
    for i in range(len(times)):
        signs.append(', ')
    if len(signs)>=2: signs[-2]=' and '
    almost_result=''
    for i in range(len(times)):
        almost_result+=times[i]
        almost_result+=signs[i]
    return almost_result[:-2]

# Codewars style ranking system
class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
    def calc_progress(self, r):
        if r == 0 or r < -8 or r > 8 or self.rank < -8 or self.rank > 8 or self.rank == 0 or self.progress > 100 or self.progress < 0:
            raise ValueError
        if r == self.rank: 
            return 3
        if r < 0:
            if self.rank < 0:
                if abs(self.rank - r) == 1 and self.rank > r:
                    return 1
                if abs(self.rank - r) >= 2 and self.rank > r:
                    return 0
                else:
                    return 10 * abs(self.rank - r) * abs(self.rank - r)
            else:
                if abs(self.rank - r - 1) == 1 and self.rank > r:
                    return 1
                if abs(self.rank - r - 1) >= 2 and self.rank > r:
                    return 0
        else:
            if self.rank < 0:
                if abs(self.rank - r + 1) == 1 and self.rank > r:
                    return 1
                if abs(self.rank - r + 1) >= 2 and self.rank > r:
                    return 0
                else:
                    return 10 * abs(self.rank - r + 1) * abs(self.rank - r + 1)
            else:
                if abs(self.rank - r) == 1 and self.rank > r:
                    return 1
                if abs(self.rank - r) >= 2 and self.rank > r:
                    return 0
                else:
                    return 10 * abs(self.rank - r) * abs(self.rank - r)

    def inc_progress(self, r):
        print(r, self.rank, self.progress)
        prog = self.calc_progress(r)
        up = 0
        self.progress += prog
        if self.progress >= 100:
            while self.progress >= 100:
                self.progress -= 100
                up += 1
        if up != 0:
            if self.rank + up >= 8:
                self.rank, self.progress = 8, 0
            else:
                if self.rank < 0 and self.rank + up >= 0:
                    up += 1
                self.rank += up
        else:
            if self.rank >= 8:
                self.rank, self.progress = 8, 0

# Roman Numerals Helper
class RomanNumerals:

    def to_roman(val):
        roman_nums=''
        while val>=1000:
            roman_nums+='M'
            val-=1000
        if val>=900:
            val-=900
            roman_nums+='CM'
        while val>=500:
            roman_nums+='D'
            val-=500
        if val>=400:
            val-=400
            roman_nums+='CD'
        while val>=100:
            roman_nums+='C'
            val-=100
        if val>=90:
            val-=90
            roman_nums+='XC'
        while val>=50:
            roman_nums+='L'
            val-=50
        if val>=40:
            val-=40
            roman_nums+='XL'
        while val>=10:
            roman_nums+='X'
            val-=10
        if val>=9:
            val-=9
            roman_nums+='IX'
        while val>=5:
            roman_nums+='V'
            val-=5
        while val>=1:
            roman_nums+='I'
            val-=1
            roman_nums
        roman_nums=roman_nums.replace('IIII','IV')
        return roman_nums


    def from_roman(roman_num):
        val=0
        while roman_num:
            if len(roman_num)==1:
                if roman_num[0]=='I':
                    val+=1
                    break
                if roman_num[0]=='X':
                    val+=10
                    break
                if roman_num[0]=='C':
                    val+=100
                    break
            if roman_num[0]=='M':
                val+=1000
                roman_num=roman_num[1:]
                continue
            elif roman_num[0]=='C':
                if roman_num[1]=='M':
                    val+=900
                    roman_num=roman_num[2:]
                    continue
                elif roman_num[1]=='D':
                    val+=400
                    roman_num=roman_num[2:]
                    continue
                else:
                    val+=100
                    roman_num=roman_num[1:]
                    continue
            elif roman_num[0]=='D':
                val+=500
                roman_num=roman_num[1:]
                continue
            elif roman_num[0]=='X':
                if roman_num[1]=='C':
                    val+=90
                    roman_num=roman_num[2:]
                    continue
                elif roman_num[1]=='L':
                    val+=40
                    roman_num=roman_num[2:]
                    continue
                else:
                    val+=10
                    roman_num=roman_num[1:]
                    continue
            elif roman_num[0]=='L':
                val+=50
                roman_num=roman_num[1:]
                continue
            elif roman_num[0]=='I':
                if roman_num[1]=='X':
                    val+=9
                    roman_num=roman_num[2:]
                    continue
                elif roman_num[1]=='V':
                    val+=4
                    roman_num=roman_num[2:]
                    continue
                else:
                    val+=1
                    roman_num=roman_num[1:]
                    continue
            elif roman_num[0]=='V':
                val+=5
                roman_num=roman_num[1:]
                continue
        return val

# )))
# 
# 
# 
# 
# 
# 
# 
# 
# 
