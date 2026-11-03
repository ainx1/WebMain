# views.py — это пример классического подхода 
# Django (SSR — Server-Side Rendering), 
# когда сам бэкенд берет данные из базы, вставляет 
# их в HTML-шаблон и отдает в браузер уже готовую веб-страницу. 

# пример как работает базовый контроллер в Django, прежде чем перейти 
# к современному подходу — REST API (api.py),
# где бэкенд отдает не HTML-страницы, а чистые данные
# в формате JSON для отдельного фронтенда на Vue.js

# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
# from PCShop.models import Component

# class ShowComponentsView(View):
#     def get(request, *args, **kwargs):
#         components = Component.objects.all()

#         result = ""
#         for s in components:
#             result += s.name + "<br>"

#         return HttpResponse(result)