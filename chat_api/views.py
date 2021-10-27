from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Messages
from .serializers import MessagesSerializer


class MessagesListView(APIView):

    def get(self, request, page):
        """
        GET method for getting all messages with pagination by 10 messages per request.
        Sorting by message creation date: recent messages at the top.
        Using DRF Pagination out of the task.
        """
        start_message = page * 10
        end_message = (page + 1) * 10
        messages = Messages.objects.order_by("-created").all()[start_message:end_message]
        serializer = MessagesSerializer(messages, many=True)
        return Response(serializer.data)


class MessageSingleView(APIView):

    def get(self, request, pk):
        """GET method for getting single message by unique identifier"""
        try:
            message = Messages.objects.get(pk=pk)
        except Messages.DoesNotExist:
            message = None
        if not message:
            return Response({"Error": f"Message with id = {pk} does not exist!"}, status=status.HTTP_404_NOT_FOUND)
        serializer = MessagesSerializer(message)
        return Response(serializer.data)


class MessageAddView(APIView):

    @swagger_auto_schema(
        operation_description="""
        POST method for creating a new message. Body accepts email and text.
        Message validation (fields:
        "author_username" field is optional (according to task) but must be unique
        "author_email" are required and must be unique, email address must be valid
        "text" is required and length must be < 100)
        """,
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['author_email', "text"],
            properties={
                'author_username': openapi.Schema(type=openapi.TYPE_STRING),
                'author_email': openapi.Schema(type=openapi.TYPE_STRING),
                'text': openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        tags=['add message']
    )
    def post(self, request):
        serializer = MessagesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
