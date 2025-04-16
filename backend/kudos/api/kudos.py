# kudos/views/auth.py (continued)
from ..api.decorators.jwt_required import token_required
import jwt
import datetime
from django.conf import settings
from rest_framework.decorators import api_view
from ..models.usermodel import User
from ..models.kudomodel import Kudo
from django.http import JsonResponse

@api_view(['POST'])
@token_required
def send_kudos_view(request):
    user_email= request.user.email
    kudos_to = request.data.get('kudos_to')
    kudos_text = request.data.get('kudos_text')
    if not kudos_to or not kudos_text:
            return JsonResponse({'error': 'Reciever and message are required'}, status=400)
    try:
        user = User.objects.get(email=user_email,organization_id=str(user._id))
        receiver = User.objects.get(_id=kudos_to,organization_id=str(user._id))
        if user.kudos_left_this_week() > 0:
            kudos = Kudo( from_user=str(user._id), to_user=kudos_to, message=kudos_text,organization_id=user.organization_id,created_by=str(user._id))
            kudos.save()
            return JsonResponse({'message': f"Kudos was sent to {receiver.name}"})
        
            
        
    except User.DoesNotExist:
        return JsonResponse({'error': 'Sender or receiver does not exist'}, status=401)

    
    return JsonResponse({'message':"Something went wrong"})

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
