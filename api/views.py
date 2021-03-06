from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_conversations_list(request, user_id):
    user = User.objects.get(id=user_id)
    conversations_list = user.conversations.all()
    serializer = ConversationSerializer(conversations_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
#@renderer_classes([JSONRenderer])
def get_messages(request, conversation_id):
    conversation = Conversation.objects.get(id=conversation_id)
    messages = conversation.messages.all()
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_message(request):
    serializer = MessageSerializer(data=request.data)
    print(request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_conversation(request):
    serializer = ConversationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)