from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects #? Review this concept in the show jobs module on udemy
    return render(request,'jobs/home.html', {'jobs':jobs}) # grabs everything from the database
