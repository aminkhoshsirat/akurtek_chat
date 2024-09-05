from django.shortcuts import render, HttpResponse
from django.contrib.auth.views import LogoutView
from django.views.generic import View, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.panel.models import SiteDetailModel
from redis import Redis
from .models import *
from .forms import *
from random import randint


re = Redis(host='localhost', db=8)


class LoginView(View):
    def get(self, request):
        site_detail = SiteDetailModel.objects.first()
        context = {
            'site_detail': site_detail,
        }
        return render(request, 'user/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            user = UserModel.objects.filter(phone=phone).first()
            if user:
                if user.ban:
                    return HttpResponse('user is baned')
                time = re.ttl(f'user:login:{phone}')
                if time < 120:
                    code = randint(100000, 999999)
                    # send code with ghasedak
                    re.set(f'user:login:{phone}', code, ex=300)
                    return HttpResponse('code send')
                else:
                    return HttpResponse('code send before')

            else:
                return HttpResponse('use not found')


class LogOutView(LogoutView):
    pass


class ContactsView(LoginRequiredMixin, ListView):
    template_name = ''
    paginate_by = 40
    context_object_name = 'contacts'

    def get_queryset(self):
        contacts = UserContactsModel.objects.filter(user=self.request.user)
        return contacts


class UserFavoriteView(LoginRequiredMixin, ListView):
    template_name = ''
    paginate_by = 40
    context_object_name = 'favorites'

    def get_queryset(self):
        favorites = UserFavoriteModel.objects.filter(user=self.request.user)
        return favorites


class UserGifView(ListView):
    template_name = ''
    paginate_by = 40
    context_object_name = 'gifs'

    def get_queryset(self):
        gifs = UserGifModel.objects.filter(user=self.request.user)
        return gifs


class UserFilesView(ListView):
    template_name = ''
    paginate_by = 40
    context_object_name = 'files'

    def get_queryset(self):
        files = UserFilesModel.objects.filter(user=self.request.user)
        return files
