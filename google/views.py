from django.shortcuts import render
from .models import *
from .forms import FirstForm
# Create your views here.

def home(request):
    context={

    }
    return render(request,'home.html',context)


def url_info(request):
    webpg=AccessRecord.objects.order_by('date')

    context={
        "a_r":webpg
    }

    return render(request,'url_info.html',context)


def user_info(request):
    info=user.objects.all()
    context={
        "user":info
    }
    return render(request,'user_info.html',context)









def formtest(request):
    form=FirstForm()
    if request.method=='POST':
        form=FirstForm(request.POST)
        if form.is_valid():

            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            body=form.cleaned_data['body']

            context={
                "c_name":name,
                "c_email":email,
                "c_body":body,
            }

            return render(request,'success.html',context)

    context={
        "form":form,
    }
    return render(request,'from.html',context)