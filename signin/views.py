from django.views.generic import TemplateView
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm

# https://qiita.com/dai-takahashi/items/7d0187485cad4418c073
class Index(TemplateView):
    template_name = "signin/index.html"

# https://qiita.com/hayata-yamamoto/items/00072091caa5921fc819
class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "signin/signup.html" 
    success_url = reverse_lazy('about:index')

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        login(self.request, user) # 認証 test_***
        self.object = user 
        return HttpResponseRedirect(self.get_success_url()) # リダイレクト