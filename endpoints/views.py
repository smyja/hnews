from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from news.models import Stories
from .serializers import StoriesSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method="get",
    manual_parameters=[
        openapi.Parameter(
            "story_type",
            openapi.IN_QUERY,
            description="Search by type",
            type=openapi.TYPE_STRING,
        )
    ],
    responses={status.HTTP_200_OK: StoriesSerializer(many=True)},
)
@api_view(
    [
        "GET",
    ]
)
def story_list(request):
    """
    List all stories
    """
    story_type = request.GET.get("story_type")
    if story_type in ["job", "comment", "poll", "pollopt", "story"]:
        news = Stories.objects.filter(story_type=story_type)[:100]
    else:
        return Response(
            status=status.HTTP_400_BAD_REQUEST,
            data={
                "error": "Please provide a correct news type,type can be story,job,comment,poll,pollopt"
            },
        )

    if request.method == "GET":
        serializer = StoriesSerializer(news, many=True)
        return Response(serializer.data)


@swagger_auto_schema(
    method="post",
    request_body=StoriesSerializer,
    responses={
        201: StoriesSerializer,
        400: "Bad Request",
    },
)
@api_view(["POST"])
def create_story(request):
    """
    Create a new story
    """
    serializer = StoriesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
