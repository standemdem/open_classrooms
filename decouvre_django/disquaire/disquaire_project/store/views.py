from django.http import HttpResponse

# Create your views here.

def index(request):
    message = "Salut tout le monde !"
    return HttpResponse(message)