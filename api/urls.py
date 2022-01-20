from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

urlpatterns = [
    path('', views.apiOverview, name="user"), 
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('get-conversations-list/<str:user_id>', views.get_conversations_list, name="get-conversations-list"),
    path('get-messages/<str:conversation_id>', views.get_messages, name="get-messages"),
    path('send-message', views.send_message, name="send-message"),
    path('create-conversation', views.create_conversation, name="create-conversation"),
]