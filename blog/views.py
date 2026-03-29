from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, mundo! Esse é o blog.")
# Create your views here.
