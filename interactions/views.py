from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import Anime, Manga
from .models import Like

# Create your views here.


class ToggleLikeView(LoginRequiredMixin, View):
    def post(self, request, content_type, obj_id):
        like_filter = {'user': request.user}

        if content_type == 'anime':
            obj = get_object_or_404(Anime, id=obj_id)
            like_filter['anime'] = obj
        elif content_type == 'manga':
            obj = get_object_or_404(Manga, id=obj_id)
            like_filter['manga'] = obj
        else:
            raise Http404('Not allowed content type.')
            
        like, created = Like.objects.get_or_create(**like_filter)

        if not created:
            like.delete()

        return redirect(request.META.get('HTTP_REFERER', '/'))