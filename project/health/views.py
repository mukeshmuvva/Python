from django.shortcuts import render
from .models import Testimonial
from django.http import JsonResponse
from .models import Feedback
from django.http import HttpResponse
import json


def fbsubmit(request):

   
    mail = request.POST.get('email')
    rate = request.POST.get('rating')
    rev = request.POST.get('review')
    if request.method == 'POST':
        Feedback.objects.create(Email = mail, rating = rate, review = rev)

    return render(request,"health/base.html")



def index(request):
    return render(request,'health/base.html')

def home(request):
    return render(request,'health/home.html')

def testimonials(request):
    Testimonial_list=Testimonial.objects.all()
    context={
        "Testimonials_list":Testimonial_list
    }  
    return render(request,'health/testimonials.html',context)
    
# Create your views here.
def beneficts(request):
    return render(request,'health/advantage.html')

def contact(request):
    return render(request,'health/contact.html')


def feedback(request):
    return render(request,'health/feedback.html')