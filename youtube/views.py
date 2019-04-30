from django.shortcuts import render

# Create your views here.

def index(request):
    context={
        "insert":"hello dhaka",
        "insert_num":100,
    }
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')

def other(request):
    return render(request,'other.html')