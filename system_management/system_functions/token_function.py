# import jwt
#
# from datetime import datetime
# from django.utils import timezone
# from rest_framework.response import Response
# from rest_framework import status
# from datetime import timedelta
#
# from user_management.models import User
# from irangard.settings import jwt_key
#
#
# def encode_token(user: 'User'):
#     now = timezone.now()
#     expiration_time = now + timedelta(60 * 60 * 24 * 3)  # insert time in seconds
#     token_data = {
#         'id': user.id,
#         'time': now.timestamp(),
#         'exp': expiration_time
#     }
#     return jwt.encode(token_data, jwt_key, algorithm='HS256')
#
#
# def decode_token(request):
#     try:
#         result = jwt.decode(request, jwt_key, algorithms='HS256')
#         user = User.objects.get(id=result['id'])
#         return user
#     except jwt.exceptions.ExpiredSignatureError:
#         return Response("شما پس از هر هشت ساعت باید دوباره وارد سیستم شوید", status=status.HTTP_401_UNAUTHORIZED)
#     except:
#         return Response({"error": "لطفا وارد سیستم شوید"}, status=status.HTTP_401_UNAUTHORIZED)
#
