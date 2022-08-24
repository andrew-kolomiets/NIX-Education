#! /usr/bin/python

#**********************************************

import sys
import math

#**********************************************

class shape:
    
    def __init__(self, name, a=0, b=0, c=0):
       pass

         
class squar(shape):
    
    def __init__(self, name, a):
        self.name=name
        self.a=a
        
    def area(self):
        return 'The area of'+self.name+'equal: '+ str(self.a*self.a)
        
         
class rectangular(shape):
    
    def __init__(self, name, a, b):
        self.name=name
        self.a=a
        self.b=b
        
        
    def area(self):
        return 'The area of'+self.name+'equal: '+ str(self.a*self.b)
        
         
class triangle(shape):
    
    def __init__(self, name, a, b, c):
        self.name=name
        self.a=a
        self.b=b
        self.c=c

    def area(self):
        p=(self.a+self.b+self.c)/2
        return 'The area of' +self.name+'equal: '+str(math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c)))


#**********************************************

if(sys.argv[1]=='rectangular' and int(sys.argv[2])!=0 and int(sys.argv[3])!=0 and sys.argv[4] not in sys.argv):
    
    obj=rectangular(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]))
    print(obj.area())
    
elif(sys.argv[1]=='triangle' and int(sys.argv[2])!=0 and int(sys.argv[3])!=0 and int(sys.argv[4])!=0 and sys.argv[5] not in sys.argv):
    
    obj=triangle(sys.argv[1],int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
    print(obj.area())

elif(sys.argv[1]=='squar' and int(sys.argv[2])!=0 and sys.argv[3] not in sys.argv):
    
    obj=squar(sys.argv[1],int(sys.argv[2]))
    print(obj.area())
    
else:
    
    print('You incorect input date.')



sys.exit("End program.")   

#**********************************************  
