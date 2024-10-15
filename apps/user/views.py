from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, login
from django.views.generic import View, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.panel.models import SiteDetailModel
from redis import Redis
from .models import *
from .forms import *
from random import randint
from django.utils.crypto import get_random_string


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


class SignUpView(View):
    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            user = UserModel.objects.filter(phone=cd['phone']).first()
            if user:
                if user.ban:
                    return HttpResponse(' user is ban')
                return HttpResponse('user is found')
            else:
                code = cd['code']
                activation_code = re.get(f'user:login:{phone}')
                if code == activation_code:
                    password = get_random_string(length=88)
                    user = UserModel.objects.create_user(phone=cd['phone'], name=cd['name'],
                                                         family_name=cd['family_name'], password=password)
                    login(request, user)
                    return HttpResponse('user sign in')
                else:
                    return HttpResponse('code incorrect')
        return HttpResponse('failed')


class ActivationView(View):
    def post(self, request):
        form = ActivationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = UserModel.objects.filter(phone=cd['phone']).first()
            if user:
                if user.ban:
                    return HttpResponse('user is baned')
                else:
                    code = cd['code']
                    activation_code = re.get(f'user:login:{phone}')
                    if code == activation_code:
                        login(request, user)
                        return HttpResponse('user login success')
                    return HttpResponse('code incorrect')
            else:
                return HttpResponse('user not found')
        return HttpResponse('failed')


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('user:login')


class StatusView(LoginRequiredMixin, ListView):
    template_name = 'user/status.html'


class SettingsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'user/settings.html')


class ContactsView(LoginRequiredMixin, ListView):
    template_name = 'user/contacts.html'
    paginate_by = 40
    context_object_name = 'contacts'

    def get_queryset(self):
        contacts = UserContactsModel.objects.filter(user=self.request.user)
        return contacts


class UserFavoriteView(LoginRequiredMixin, ListView):
    template_name = 'user/favorite.html'
    paginate_by = 40
    context_object_name = 'favorites'

    def get_queryset(self):
        favorites = UserFavoriteModel.objects.filter(user=self.request.user)
        return favorites


class UserDocumentView(ListView):
    template_name = 'user/document.html'
    paginate_by = 40
    context_object_name = 'files'

    def get_queryset(self):
        files = UserFilesModel.objects.filter(user=self.request.user)
        return files


class UserToDoView(TemplateView):
    template_name = 'user/to-do.html'


class UserNoteView(TemplateView):
    template_name = 'user/notes.html'


class UserReminderList(TemplateView):
    template_name = 'user/reminder.html'


class UserGifView(ListView):
    template_name = 'user/gifs.html'
    paginate_by = 40
    context_object_name = 'gifs'

    def get_queryset(self):
        gifs = UserGifModel.objects.filter(user=self.request.user)
        return gifs


class UserFilesView(ListView):
    template_name = 'user/files.html'
    paginate_by = 40
    context_object_name = 'files'

    def get_queryset(self):
        files = UserFilesModel.objects.filter(user=self.request.user)
        return files
