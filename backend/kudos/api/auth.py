# kudos/views/auth.py (continued)
from ..api.decorators.jwt_required import token_required
import jwt
import datetime
from django.conf import settings
from rest_framework.decorators import api_view
from ..models.usermodel import User
from django.http import JsonResponse

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return JsonResponse({'error': 'Invalid credentials'}, status=401)

    if not user.check_password(password):
        return JsonResponse({'error': 'Invalid credentials'}, status=401)

    payload = {
        'user_id': str(user._id),
        'email': user.email,
        'organization_id': str(user.organization_id),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    return JsonResponse({'token': token, 'user': {'email': user.email, 'name': user.name}})

@api_view(['GET'])
@token_required
def me_view(request):
    user = request.user
    user_data = {
        'email': user.email,
        'name': user.name,
        '_id': str(user._id),
        'organization_id': str(user.organization_id),
    }
    return JsonResponse({'user': user_data})

@api_view(['GET'])
@token_required
def get_users_by_org(request):
    user = request.user
    users = User.objects.filter(organization_id=user.organization_id).exclude(_id=user._id)
    user_list = users.values('name', 'email', '_id')
    return JsonResponse(list(user_list), safe=False)