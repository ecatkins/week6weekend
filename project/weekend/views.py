from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import JsonResponse
from weekend.models import Instagram
from django.http import HttpResponse
import os


class GayPrideView(View):
    
    def get(self,request):
        return JsonResponse({
            "event":"gay_pride",
            "date":"2015-06-26 {}:00:00+00:00",
            "icon":"flag",
            "latitude":"40.733661",
            "longitude":"-74.011023",
            "zoom":"13",
            "suggested_search": "pride, gay, SCOTUS"
            })


class WWCView(View):

    def get(self, request):
        return JsonResponse({
            "event":"wwc",
            "date":"2015-07-10 {}:00:00+00:00",
            "icon":"soccer",
            "latitude":"40.713669",
            "longitude":"-74.006016",
            "zoom":"13",
            "suggested_search": "USWNT, WWC, Alex Morgan"
            })


class IndexView(View):
    template = 'weekend/index.html'

    def get(self, request):
        return render(request, self.template)


class InstagramView(View):
    def get(self, request, event_name, search, interval):
        #filter by event name
        if event_name == "gay_pride":
            day = "2015-06-26 {}:00:00+00:00"
        elif event_name == "wwc":
            day = "2015-07-10 {}:00:00+00:00"
        #filter by search fields
        print(search,interval)
        if search == "none" and interval == "all":
            all_posts = Instagram.objects.filter(event=event_name)
        elif search == "none" and interval != "all": 
            all_posts = Instagram.objects.filter(event=event_name, created_time__range=[day.format(interval), day.format(int(interval)+1)])
        elif search != "none" and interval == "all":
            all_posts = Instagram.objects.filter(event=event_name, caption__icontains=search)
        else:
            all_posts = Instagram.objects.filter(event=event_name, caption__icontains=search, created_time__range=[day.format(interval), day.format(int(interval)+1)])
        print(all_posts)
        all_post_info = []
        for post in all_posts:

            all_post_info.append(post.info)
        return JsonResponse({"all_post_info": all_post_info})


class FrontView(View):
    template = 'weekend/front.html'
    def get(self,request):
        return render(request, self.template)


def flag(request):
    image_data = open(os.getcwd()+'/weekend/templates/weekend/gay_flag.png',"rb").read()
    return HttpResponse(image_data,content_type="image/png")

def soccer(request):
    image_data = open(os.getcwd()+'/weekend/templates/weekend/soccer.png',"rb").read()
    return HttpResponse(image_data,content_type="image/png")
