"""Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. 
In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 
1666 uses each Roman symbol in descending order: MDCLXVI.

Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
1000 -> "M"
 400 -> "CD"
  90 -> "XC"
  40 -> "XL"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"M"       -> 1000
"CD"      -> 400
"XC"      -> 90
"XL"      -> 40
"I"       -> 1"""

#https://www.codewars.com/kata/51b66044bce5799a7f000003

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