import requests
from datetime import datetime
import pytz

class HackerNewsAPI:
    """Serves as a layer of abstraction for communication with the Hacker News API.


    Attributes:
        write_api str): Zc_core API endpoint for writing (POST) and updating (PUT) data.
       

    """
    def __init__(self):

        """Initializes the data storage instance with zc_messaging plugin id.

        A request is sent to Hackernews API endpoint to get the Top 100 stories.

        Args:
            item_id: The story id

        Raises:
            HTTPException: {"detail": "Request Timeout"}
        """        
        self.stories_api = "https://hacker-news.firebaseio.com/v0/topstories.json"
        self.story_api = "https://hacker-news.firebaseio.com/v0/item/{}.json"
        
    def get_stories(self):
        """Gets the top 100 stories from the Hacker News API. 
        """
        # to obtain list of top story ids
        r = requests.get(self.stories_api)
        article_ids = r.json() # author used submission as variable name, but articles made more sense to me
        five_articles_dicts = [] # this dict will contain all of our articles
        for article_id in article_ids[:10]:
            url = 'https://hacker-news.firebaseio.com/v0/item/' + str(article_id) + '.json' # plug in looped id
            article_r = requests.get(url) # get response for each individual article

            #author prints out article status code to ensure no failures with requests
            one_article= article_r.json()
            print(one_article)
      

            five_articles_dict = {
            'Title': one_article.get('title'),
            'link': one_article.get('url', ""),
            'descendants': one_article.get('descendants', 0),
            'score': one_article.get('score'),
            'Author': one_article.get('by'),
            'Time': datetime.fromtimestamp(one_article['time']).strftime("%d %B, %Y %H:%M"),
            'Type': one_article.get('type'),
            'ID': one_article.get('id'),
            'Kids': one_article.get('kids', None)  
            }

            five_articles_dicts.append(five_articles_dict)
            
         
        return five_articles_dicts
    def get_comments(self, item_id):
        """Gets the comments for a given story id.
        """

        # try :
        #     response = requests.get(self.stories_api)

        #     return response.json()

        # except Exception as e:
        #     raise Exception("Request Timeout")

