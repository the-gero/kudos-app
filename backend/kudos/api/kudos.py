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
    print("USER =>>>>>",request.user)
    kudos_to = request.data.get('kudos_to')
    kudos_text = request.data.get('kudos_text')
    if not kudos_to or not kudos_text:
            return JsonResponse({'error': 'Reciever and message are required'}, status=400)
    try:
        user = request.user
        receiver = User.objects.get(_id=kudos_to,organization_id=user.organization_id)
        if user and receiver and user.kudos_left_this_week() > 0:
            kudos = Kudo( from_user=user, to_user=receiver, message=kudos_text,organization_id=user.organization_id,created_by=str(user._id))
            kudos.save()
            return JsonResponse({'message': f"Kudos was sent to {receiver.name}"})
        
            
        
    except User.DoesNotExist:
        return JsonResponse({'error': 'Sender or receiver does not exist'}, status=401)

    
    return JsonResponse({'message':"Something went wrong"})

@api_view(['GET'])
@token_required
def get_kudos(request):
    user = request.user

    # Get and serialize sent kudos
    sent_kudos = user.sent_kudos.select_related('to_user').all()
    sent_data = [
        {
            'to': kudo.to_user.name,
            'message': kudo.message,
            'date': kudo.created_at
        }
        for kudo in sent_kudos
    ]

    # Get and serialize received kudos
    received_kudos = user.received_kudos.select_related('from_user').all()
    received_data = [
        {
            'from': kudo.from_user.name,
            'message': kudo.message,
            'date': kudo.created_at
        }
        for kudo in received_kudos
    ]

    return JsonResponse({
        'sent': sent_data,
        'received': received_data
    })
