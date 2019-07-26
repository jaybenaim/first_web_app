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
        'skills': ['Management skills', 'Problem Solving', 'Work well under pressure'],
        'interests': ['Cooking', 'Guitar']
    }
    response = render(request, 'about_me.html', context) 
    return HttpResponse(response) 

def favourites(request): 
    context = { 'fave_links': ['http://hackertyper.com/', 'https://findtheinvisiblecow.com/', 'https://www.incredibox.com/demo/v1', 'http://www.flashbynight.com/', 'https://www.autodraw.com', 'http://bomomo.com/', 'http://weavesilk.com/', 'http://www.movenowthinklater.com/', 'https://www.addictivetips.com/','https://www.dafont.com/','https://mashable.com/article/websites-to-waste-time/', 'http://www.koalastothemax.com/']}
    
    response = render(request, 'favourites.html', context) 
    return HttpResponse(response) 
