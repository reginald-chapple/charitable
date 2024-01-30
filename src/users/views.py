from django.contrib.auth import logout, login
from django.shortcuts import redirect, render

from users.forms import UserSignUpForm
from users.models import User

def register_user(request):
    template_name = 'registration/signup.html'
    context = {}
    
    form = UserSignUpForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("home")
    
    context["form"] = form
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('home')
