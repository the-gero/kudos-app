import jwt
from django.conf import settings
from django.http import JsonResponse
from functools import wraps
from datetime import datetime
from ...models.usermodel import User

def token_required(func):
    @wraps(func)
    def decorator(request, *args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return JsonResponse({'error': 'Authorization token is missing'}, status=403)

        try:
            token = token.replace('Bearer ', '')
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user_id = payload['user_id']
            user = User.objects.get(_id=user_id)
            request.user = user

        except (jwt.ExpiredSignatureError, jwt.DecodeError, User.DoesNotExist):
            return JsonResponse({'error': 'Invalid or expired token'}, status=401)

        return func(request, *args, **kwargs)

    return decorator
