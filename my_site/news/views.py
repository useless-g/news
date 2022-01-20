from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    print(request)
    return HttpResponse('Hello, world!')


def my_page(request):
    return HttpResponse("""<!doctype html>
<html>
    <head>
        <title>моя страница</title>
        <meta charset="UTF-8" />
    </head>
    <body>
        <h1>Hello world!</h1>
        <h2>Hello world!</h2>
        <h3>Hello world!</h3>
        <h4>Hello world!</h4>
        <h5>Hello world!</h5>
        <h6>Hello world!</h6>
        <p>bla bla bla</p>
    </body>
</html>""")