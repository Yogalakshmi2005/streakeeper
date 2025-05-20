from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logo_splash_view(request):
    return render(request, 'skapp/logo_splash.html')

def home_view(request):
    return render(request, 'skapp/home.html')

def dashboard_view(request):
    return render(request, 'skapp/dashboard.html')

def create_goal_view(request):
    return render(request, 'skapp/create_goal.html')

def check_in_view(request):
    return render(request, 'skapp/check_in.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'skapp/signup.html', {'form':form})         