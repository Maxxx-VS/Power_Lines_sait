from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анкерная опора', 'content': '''<h1>Анкерная опора</h1>
     (Это опора воздушной линии электропередачи, воспринимающая усилия от разности тяжения проводов,
      направленных вдоль ВЛ)''',
     'is_published': True},
    {'id': 2, 'title': 'Промежуточная опора', 'content': '''<h1>Промежуточная опора</h1>
     (Это опора воздушной линии электропередачи, служащая для поддержания проводов на определенной высоте от земли
      и не рассчитанная на усилия со стороны проводов в продольном направлении или под углом)''',
     'is_published': True},
    {'id': 3, 'title': 'Концевая опора', 'content': '''<h1>Концевая опора</h1>
     (Это разновидность анкерных опор, устанавливаются в конце или начале линии. При нормальных условиях работы ВЛ
      они воспринимают нагрузку от одностороннего натяжения проводов и тросов)''',
     'is_published': True},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь!!!")


def login(request):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
