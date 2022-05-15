# Hackernews webapp.

### Requirements
- Redis
- Django
- Celery and Celery Beat
### To get started.
- create a virtual environment and install the packages using  ```python install -r requirements.txt``` 
- Make migrations
Open 4 terminals,
Start Django server in terminal 1.
Start Redis server in terminal 2. 

Start the worker in terminal 3 with ```celery -A hackernews worker -l info```
and the beat in terminal 4 with ```celery -A hackernews beat -l info```
#### For Monitoring, flower is used. 
Open another terminal and run 
```celery -A hackernews flower --port=5555```
