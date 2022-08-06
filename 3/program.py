import math

def number_float_point(_number):
    x=str(round(float(_number),2))
    size=len(x)
    if(x[size-1]=='0' and x[size-2]=='0' and x[size-3]=='.' ):
        x=float(x)
        return round(x)
    elif(x[size-1]=='0' and x[size-2]=='.'):
       
        return round(float(x))
    else:
        return round(float(_number),2)


print('************************************')

number=input('Input number: ')

print('************************************')

text='Output: {_number}'.format(_number=number_float_point(number))

print(text)

print('************************************')

