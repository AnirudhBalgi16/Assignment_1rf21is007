from django.shortcuts import render
import math

def home(request):
    res=fact(3,8)
    return render(request,'app3/index.html',{'para':res})


def fact(n1,n2):
    number=[]
    facto=[]
    for i in range(n1,n2+1):
        f=math.factorial(i)
        facto.append(f)
        number.append(i)
    return zip(number,facto)    

           
     
