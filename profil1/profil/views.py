from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")












def http(request):
    host = request.META["HTTP_HOST"] #получаем адрес сервера 
    user_agent = request.META["HTTP_USER_AGENT"]# получаем данные бразера
    path = request.path #получаем запрошенный путь 

    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
    """)
def set(request):
    #получаем из строки запроса имя пользователя
    username = request.GET.get("username","Undefined")
    #создаем обьект ответа
    response = HttpResponse(f"Hello {username}")
    #передаем его в куки 
    response.set_cookie("username", username)
    return response

# получение куки
#def get(request):
    # получаем куки с ключом username
    #username = request.COOKIES["username"]
    #return HttpResponse(f"Hello {username}")