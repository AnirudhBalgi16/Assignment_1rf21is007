from django.shortcuts import render
from app2.forms import inputform
import math
def home(request):
    result=None
    n1=0
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1")
            result=math.factorial(n1)
            return render(request,"app2/index.html",{'param1':result, 'num':n1,'form':form1})
    else:
        form1 = inputform()

    return render(request, 'app2/index.html', {'form': form1,'num':n1, 'param1':result})