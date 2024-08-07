from django.shortcuts import render,redirect
from .models import Tour
from .form import *

# Create your views here.
def index(request):
    tours = Tour.objects.all()
    context = {'tours':tours}
    return render(request , 'tours/index.html',context)

def contact_view(request):
    if request.method == 'POST':
        form = Contact_Form(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-sucsess')
    
    else:
        form = Contact_Form()
        context = {'form':form}
    return render(request, 'tours/contact.html',context)

def contact_sucsess(request):
    return render(request,'tours/sucsess.html')
