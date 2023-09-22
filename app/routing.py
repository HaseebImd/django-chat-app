from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/sc/<str:groupkaname>/", consumers.SyncConsumer.as_asgi()),
]
