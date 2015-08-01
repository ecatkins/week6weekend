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
    day = "2015-06-26 {}:00:00+00:00"

    def get(self, request, search, interval):
        if search == "none" and interval == "all":
            all_posts = Instagram.objects.all()
        elif search == "none" and interval != "all": 
            all_posts = Instagram.objects.filter(created_time__range=[self.day.format(interval), self.day.format(int(interval)+1)])
        elif search != "none" and interval == "all":
            all_posts = Instagram.objects.filter(caption__icontains=search)
        else:
            all_posts = Instagram.objects.filter(caption__icontains=search, created_time__range=[self.day.format(interval), self.day.format(int(interval)+1)])
        all_post_info = []
        for post in all_posts:
            all_post_info.append(post.info)
        return JsonResponse({"all_post_info": all_post_info})



def flag(request):
    image_data = open(os.getcwd()+'/weekend/templates/weekend/gay_flag.png',"rb").read()
    return HttpResponse(image_data,content_type="image/png")


class FrontView(View):
    template = 'weekend/front.html'
    def get(self,request):
        return render(request, self.template)

