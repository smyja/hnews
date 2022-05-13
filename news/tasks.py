from celery import shared_task, app
from hackernews.celery import app
from news.api import HackerNewsAPI
from .models import Stories


@shared_task
def do_something(x):
    print('do something')
    return x

@app.task
def sendu():
    hn=HackerNewsAPI()
    article=hn.get_stories()
 

    # loop = asyncio.get_event_loop()
    # loop.create_task(do_long_query_in_the_background(some_data))
    comments={}
    for i in article:
        #Check if the story is already in the database
        news,created = Stories.objects.get_or_create(title=i['Title'])
        if not created:
            comments["list"]=i['Kids']
            news.story_id=i['ID']
            news.title=i['Title']
            news.story_type=i['Type']
            news.author=i['Author']
            news.url=i['link']
            news.kids=i['Kids']
            news.time=i['Time']
            news.score=i['score']
            news.descendants=i['descendants']
            news.save()
    return 'First scraping is done'
    
    