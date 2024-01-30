from django.shortcuts import render

# Create your views here.
def not_found(request):
    template_name = '404.html'
    context = {}
    return render(request, template_name, context)

def forbidden(request):
    template_name = '403.html'
    context = {}
    return render(request, template_name, context)

def server_error(request):
    template_name = '500.html'
    context = {}
    return render(request, template_name, context)