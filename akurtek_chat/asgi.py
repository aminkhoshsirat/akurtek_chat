import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from channels.sessions import SessionMiddlewareStack
from channels.security.websocket import OriginValidator
from .routing import websocket_urlpatterns


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "akurtek_chat.settings")

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": OriginValidator(
            SessionMiddlewareStack(
                AllowedHostsOriginValidator(
                    AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
                )
            ),
            ['*']
        ),

    }
)
