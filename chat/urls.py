
from django.urls import path, include
from .views import ChatView

app_name ='chat'

urlpatterns = [
    path('', ChatView.as_view(), name= 'index' ),
    path('<str:room>/', ChatView.as_view(), name= 'room' ),
   
]