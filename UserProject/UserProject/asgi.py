"""
ASGI config for UserProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""
import os
import django
from django.core.asgi import get_asgi_application
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from UserOpeartion.user_consumer import UserConsumer
# from Authenticate.user_consumer import UserConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UserProject.settings')

# application = get_asgi_application()
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r'^ws/', UserConsumer.as_asgi()),
            url(r'^ws/<int:id>/', UserConsumer.as_asgi()),

        ])
    ),
})



#ws://127.0.0.1:8000/user/?opr=update
