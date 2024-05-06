from django.http import HttpResponse

def index(request):
    return HttpResponse("<h2>Home<h2>")
def about(request):
    return HttpResponse("Site")
def contact(request, name, age):
    return HttpResponse(f"""
            <h2>Contact<h2>
            <p>Name: {name}</p>
            <p>Age:{age}</p>
     """)
def https(request):
    host = request.META["HTTP_HOST"]#получаем адрес сервера
    user_agent= request.META["HTTP_USER_AGENT"] #получаем данные браузера
    path = request.path #поулчаем запрошенный путь 
    
    return HttpResponse(f"""
                <p>Host:{host}</p>
                <p>Path:{path}</p>
                <p>User-agent:{user_agent}</p>
                """)
#Set cookis
def set(request):
    #получаем из строки запрос имя пользователя
    username = request.GET.get("username", "Undefined")
    #создаем обьект ответ
    response = HttpResponse(f"Hello {username}")
    #передаем его куки
    response.set_cookie("username", username)
    return response