from django.shortcuts import render, redirect


def home(request):
    # if request.user.is_authenticated and request.user.is_member:
    #     return redirect('users:profile', request.user.slug)
    template_name='pages/home.html'
    return render(request, template_name)

