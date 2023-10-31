from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.


def near_hundred(request: HttpRequest, n: str) -> HttpResponse:
    return HttpResponse((100 - abs(n)) <= 10 or (200 - abs(n)) <= 10)


def string_splosion(request: HttpRequest, string: str) -> HttpResponse:
    new_word = list(string)
    answer = ""
    answer2 = ""
    i = 1
    while i < len(string) + 1:
        fragment = slice(0, i)
        parts = answer.join(new_word[fragment])
        answer2 += parts
        i += 1
    return HttpResponse(answer2)


def cat_dog(request: HttpRequest, string: str) -> HttpResponse:
    return HttpResponse(f"{True if 'cat' and 'dog' in string else False}")


def lone_sum(request: HttpRequest, a: int, b: int, c: int) -> HttpResponse:
    if a != b:
        pass
    else:
        a = 0
        b = 0
    if b != c:
        pass
    else:
        b = 0
        c = 0
    if a != c:
        pass
    else:
        a = 0
        c = 0
    if a != b and b != c:
        pass
    else:
        a = 0
        b = 0
        c = 0
    answer = a + b + c
    return HttpResponse(answer)
