from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        "title": "Главная страница" ,
        "values": ["some", "Hello", "123"],
        "obj": {
            "car": "BMW",
            "age": 18,
            "hobby": "football"
        }
    }
    return render(request, "main/index.html", data)

def about(request):
    return render(request, "main/about.html")

def mypage(request):
    return HttpResponse("<h1> This is my page<h1")