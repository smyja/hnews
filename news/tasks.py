from celery import shared_task, app
from hackernews.celery import app
from news.api import HackerNewsAPI
from .models import Stories


@shared_task
def do_something(x):
    print("do something")
    return x


@app.task
def sendu():
    hn = HackerNewsAPI()
    article = hn.get_stories()

    comments = {}
    for i in article:
        Stories.objects.get_or_create(
            title=i["Title"],
            author=i["Author"],
            story_type=i["Type"],
            url=i["link"],
            time=i["Time"],
            descendants=i["descendants"],
            score=i["score"],
            story_id=i["ID"],
            kids=i["Kids"],
        )

        comments["list"] = i["Kids"]
    return "News sync complete is done"
