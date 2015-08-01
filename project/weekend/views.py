from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from weekend.models import Instagram
from django.http import HttpResponse
import os


class IndexView(View):
    template = 'weekend/index.html'

    def get(self, request):
        return render(request, self.template)

class InstagramView(View):

    def get(self,request):
        all_posts = Instagram.objects.all()
        all_post_info = []
        for post in all_posts:
            all_post_info.append(post.info)
        return JsonResponse({"all_post_info": all_post_info})



def flag(request):
    print('got here')
    print(os.system('pwd'))
    print(type(os.getcwd()))
    print(os.getcwd())
    image_data = open(os.getcwd()+'/weekend/templates/weekend/gay_flag.png',"rb").read()
    return HttpResponse(image_data,content_type="image/png")


class FrontView(View):
    template = 'weekend/front.html'
    def get(self,request):
        return render(request, self.template)

