# from django.shortcuts import render

# def index(request):
#     return render(request, 'about/index.html')

from django.views.generic import TemplateView

# https://qiita.com/dai-takahashi/items/7d0187485cad4418c073
class Index(TemplateView):
    template_name = "about/index.html"