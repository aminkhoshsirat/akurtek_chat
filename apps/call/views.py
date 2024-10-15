from django.shortcuts import render
from django.views import View


class VideoCallView(View):
    def get(self, request):
        return render(request, 'call/video-call.html')