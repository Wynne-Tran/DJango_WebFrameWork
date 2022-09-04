from django.http import HttpResponse
from django.shortcuts import render

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return HttpResponse("<h1>Hello World </h1>")


def contacts(request, *args, **kwargs):
    #return HttpResponse("<h1>Contacts </h1>")
    return render(request, "home.html", {})

def about(request, *args, **kwargs):
    return render(request, "About.html", {})


def page1(request, *args, **kwargs):
    my_context = {
        "my_text": "This is page 1",
        "condition": True,
        "my_num": 123,
        "my_list": ["Wynne", "Tran", "Thi", "Hoang", 12, 87],
        "html_tag": "<p>render html tag</p>"
    }
    return render(request, "Page.html", my_context)