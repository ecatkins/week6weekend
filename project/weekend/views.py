from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from weekend.models import Instagram


class IndexView(View):
    template = 'weekend/index.html'

    def get(self, request):
        return render(request, self.template)

class InstagramView(View):

    def get(self,request):
        print('insta view func')
        all_posts = Instagram.objects.all()
        all_post_info = []
        for post in all_posts:
            all_posts.append(post.info)
        return JsonResponse({"all_post_info": all_post_info})