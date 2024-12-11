from django.shortcuts import render , HttpResponse

# Create your views here. 
def hello(request) : 
    return  render(request,'myapp/index.html') 

def cond1(request) : 
    return  render(request,'myapp/index1.html') 

def cond2(request) : 
    return  render(request,'myapp/index2.html') 

def cond3(request) : 
    return  render(request,'myapp/index3.html')
