from django.shortcuts import render

# Create your views here.
def indexview(request):
    return render(request,'main/index.html')

def aboutusview(request):
    return render(request,'main/aboutus.html')

def contactview(request):
    return render(request,'main/contactus.html')

def authview(request):
    return render(request,'main/login.html')