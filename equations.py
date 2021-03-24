def power(x,y):
    result = 1
    for i in range(int(y)):
        result=result*x
    return result

def factorial (n):
    result2 = 1
    for i in range(1,int(n)+1):
        result2 = result2*i
    return result2

def exponent(n):
    result3 = 0
    for i in range(0,100):
        result3 = result3+(power(n,i))/(factorial(i))
    return result3

def Ln(x) :
    try:
        if(x<=0):
            return 0.0
        else:
            yn = 0
            result4 = x-1
            while((yn-result4)>0.001 or result4-yn>0.001):
                yn = result4
                result4=result4+2*((x-exponent(result4))/(x+exponent(result4)))
            return result4
    except:
        return 0.0

def XtimesY (x:float,y:float) -> float:
    try:
        if(x<=0):
            return 0.0
        else:
            a=exponent(Ln(x)*y)
            return float('%0.6f' %a)
    except:
        return 0.0

def sqrt(x:float,y:float) -> float:
    try:
        if(y>0 and x!=0):
            x=1/x
            a=XtimesY(y,x)
            return (float('%0.6f' %a))
        else:
            return 0.0
    except:
        return 0.0
def calculate(x):
    try:
        if(x<=0):
            return 0.0
        result5 = exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
        b =float('%0.6f' %result5 )
        return b
    except:
        return 0.0
# # 
# try:
#     num1=input('enter a num1: ')
#     # num2=input('enter num2: ')
#     x=float(num1)
#     # y=float(num2)
#     print(calculate(x))
#     # print(XtimesY(x,y))
#     # print(sqrt(x,y))
# except:
#     print(0)# -*- coding: utf-8 -*-
# """
# Spyder Editor

# This is a temporary script file.
# """

