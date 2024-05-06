from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Home<h2>")
def about(request):
    return HttpResponse("Site")
def contact(request):
    return HttpResponse("Conctact")