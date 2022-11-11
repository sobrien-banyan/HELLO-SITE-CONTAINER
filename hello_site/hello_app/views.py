from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class HomeWorldView(View):
    def get(self, request):
        return render(request, template_name='hello_world.html')

class HomeView(View):
    def get(self, request, name):
        print(name)
        return render(request, template_name='hello_name.html', context={'person': name})
