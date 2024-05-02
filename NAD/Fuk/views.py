from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    header = "Данные пользователя" #обычные переменая
    langs = ["Python"]
    user = {"name": "David", "age": 22}
    #site = ()

    data = {"header": header, "langs": langs, "name": user}
    return render(request,"index.html", context=data)
def mainthing(request):
    return render(request, "mainthing.html")
def about(request):
    return render(request, "about.html")
def concact(request):
    return render(request, "contact.html")





#Установка  кукикс
def set(request):
     # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefind")
    #создаем обьект ответа
    response = HttpResponse("username", username)
    #передаем его в куки 
    response.set_cookie("username", username)
    return response
#Получения куки: 
def get(request):
    #получаем куки с ключом username
    username =request.COOKIES["username"]
    return HttpResponse(f"Hello{username}")