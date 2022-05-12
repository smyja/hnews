from django.http import HttpResponse
from django.shortcuts import render
from news.api import HackerNewsAPI
from .models import Stories

# Create your views here.

def homepage(request):
    hn=HackerNewsAPI()
    article=hn.get_stories()
 

    # loop = asyncio.get_event_loop()
    # loop.create_task(do_long_query_in_the_background(some_data))
    comments={}
    for i in article:
        news=Stories()
        comments["list"]=i['Kids']
        news.story_id=i['ID']
        news.title=i['Title']
        news.story_type=i['Type']
        news.author=i['Author']
        news.slug=i['link']
        news.kids=i['Kids']
        news.time=i['Time']
        news.save()
    return HttpResponse("Scraping is done")
   