from django.http import HttpResponse
from django.shortcuts import render
from news.api import HackerNewsAPI
from .models import Stories
from django.views import generic

# Create your views here.

def apidata(request):
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
        news.url=i['link']
        news.kids=i['Kids']
        news.time=i['Time']
        news.save()
    return HttpResponse("Scraping is done")


class StoryListView(generic.ListView):
    template_name = 'homepage.html'
    paginate_by = 10


    def get_queryset(self):
        story = Stories.objects.filter(story_type='story')

        title = self.request.GET.get('title', None)
        val = self.request.GET.get('dropdown',None)
        print(val)
        if title:
            qs = Stories.objects.all()
            qs = qs.filter(title__icontains=title)
            return qs.order_by("-synced")
        elif val:
            qs = Stories.objects.all()
            qs = qs.filter(story_type=val)
            return qs.order_by("-synced")
        

        return story.order_by("-synced")

    def get_context_data(self, **kwargs):
        context = super(StoryListView, self).get_context_data(**kwargs)
        count = Stories.objects.all().count()
        
        context.update({
            "total_count": count
        })
        return context
    

