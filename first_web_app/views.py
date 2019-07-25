from random import randint 
from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render

def root(request): 
    return HttpResponseRedirect('home')

def home_page(request): 
    context = {'name': 'Betty Maker'}
    response = render(request, 'index.html', context) 
    return HttpResponse(response) 

def gallery(request): 
    image_urls = [] 
    for i in range(5): 
        random_number = randint(0, 100) 
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number)) 
    
    context = {'gallery_images': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response) 

def portfolio(request): 
    return HttpResponseRedirect('/portfolio')

def about_me(request): 
    context = {
        'skills': ['Management skills', 'Problem Solving', 'work well under pressure'],
        'interests': ['cooking', 'guitar']
    }
    response = render(request, 'about_me.html', context) 
    return HttpResponse(response) 

def favourites(request): 
    context = { 'fave_links': ['link1', 'link2', 'link3']}
    response = render(request, 'favourites.html', context) 
    return HttpResponse(response) 
