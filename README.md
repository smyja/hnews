# Hackernews webapp.

### Requirements
- Redis
- Django
- Celery and Celery Beat
- Linux/Ubuntu

### To get started.
- create a virtual environment and install the packages using  ```python install -r requirements.txt``` 
- Make migrations
Open 4 terminals,
Start Django server in terminal 1.
Start Redis server in terminal 2. 

Start the worker in terminal 3 with ```celery -A hackernews worker -l info```
and the beat in terminal 4 with ```celery -A hackernews beat -l info```
#### Monitoring, 
For Monitoring, flower is used. 
Open another terminal and run 
```celery -A hackernews flower --port=5555```

#### Endpoints
- ```api/v1/docs``` - Swagger documentation
- ```api/v1/create``` - Endpoint for creating story
- ```api/v1/stories``` - Endpoint for getting stories. 
