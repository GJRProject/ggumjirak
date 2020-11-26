from django.shortcuts import render
from .models import Post
# Create your views here.

# 메인화면 
def home(request):
	return render(request, 'home.html')

# 스케쥴
def schedule(request):
    return render(request, 'schedule.html')

    
def alpha(request):
    return render(request, 'alpha.html')

def beta(request):
    return render(request, 'beta.html')

def gamma(request):
    return render(request, 'gamma.html')   