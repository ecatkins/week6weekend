from django.shortcuts import render, redirect
from django.views.generic import View

class IndexView(View):
    template = 'weekend/index.html'

    def get(self, request):
        return render(request, self.template)