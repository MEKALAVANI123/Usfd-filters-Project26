from django.shortcuts import render

# Create your views here.

def usdf(request):
    d={'data':'Hai VaNi'}
    return render(request,'usdf.html',d)