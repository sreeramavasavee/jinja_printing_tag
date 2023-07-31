from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'ashu','age':13}
    return render(request,'data_render.html',context=d)

def if_else(request):
    d={'a':1000,'b':500}
    return render(request,'if_else.html',context=d)

def if_elif_else(request):
    d={'a':1000,'b':500,'c':16000}
    return render(request,'if_elif_else.html',context=d)

def nestedif(request):
    d={'a':1000,'b':50000,'c':16000}
    return render(request,'nestedif.html',context=d)

def loopcdt(request):
    d={'name':'ashu','age':13 ,'hobbies':['cricket','football']}
    return render(request,'loopcdt.html',context=d)
