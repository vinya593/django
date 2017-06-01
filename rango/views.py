from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from rango.models import Category
#def index(request):
    #return HttpResponse("Rango says hey there partner!")
def about(request):
        #return HttpResponse("Rango says about us to partner!"+ "<a href='/rango'> back </a>"
        return render(request, 'rango/about.html')
def index(request):
    #context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    #return render(request, 'rango/index.html', context=context_dict)
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
# Render the response and send it back!
    return render(request, 'rango/index.html', context_dict)


# Create your views here.
