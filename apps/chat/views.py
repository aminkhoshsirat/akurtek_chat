from django.shortcuts import render
from django.views.generic import View, ListView
from django.db.models import Q
from apps.user.models import *
from apps.panel.models import SiteDetailModel
from .models import *


class IndexView(View):
    def get(self, request):
        user = self.request.user
        rooms = ChatRoomModel.objects.filter(Q(user1=user) | Q(user2=user), ~Q(delete_user=user)).order_by('-date')
        site_detail = SiteDetailModel.objects.first()
        contacts = UserContactsModel.objects.filter(user=user).first()
        favorites = UserFavoriteContactsModel.objects.filter(user=user).first()
        context = {
            'rooms': rooms,
            'site_detail': site_detail,
            'contacts': contacts,
            'favorites': favorites,
        }
        return render(request, 'index.html', context)

