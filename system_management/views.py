from rest_framework.views import APIView
from django.utils.translation import ugettext_lazy as _
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny

from system_management.system_functions.input_functions import ProcessRequest
from system_management.system_functions.output_functions import process_response

from user_management.models import User
from user_management.serializers import UserReadSerializer, RegisterSerializer
from . import serializers
from system_management.models import State
from .system_functions.output_functions import process_response
# from .system_functions.token_function import encode_token


class Login(APIView):
    queryset = User.objects.filter(is_active=True)
    serializer = serializers.LoginSerializer

    def post(self, *args, **kwargs):
        inputs = args[0].data
        validate = self.serializer(data=inputs)
        if not validate.is_valid():
            response = process_response(message=_("bad request!"), errors=validate.errors)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username=inputs['username'])
            if not check_password(inputs['password'], user.password):
                raise Exception("login error")
            else:
                token = Token.objects.get_or_create(user=user)
                ser = UserReadSerializer(user)
                response = ser.data
                response['token'] = token[0].key
                response = process_response(message=_("done!"), data=response)
                return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response = process_response(message=_("login failed!"), errors=e.args)
            return Response(response, status=status.HTTP_401_UNAUTHORIZED)


class Register(APIView):
    queryset = User.objects.all()
    serializer = RegisterSerializer

    def post(self, *args, **kwargs):
        inputs = args[0].data
        validate = self.serializer(data=inputs)
        if not validate.is_valid():
            response = process_response(message=_("bad request!"), errors=validate.errors)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            user = validate.save()
        token = Token.objects.get_or_create(user=user)
        ser = UserReadSerializer(user)
        response = ser.data
        response['token'] = token[0].key
        response = process_response(message=_("done!"), data=response)
        return Response(response, status=status.HTTP_200_OK)


class StateView(APIView):
    permission_classes = [AllowAny]
    read_serializer = serializers.StateReadSerializer
    query_set = State.objects

    def get(self, *args, **kwargs):
        # search filters
        if args[0].query_params.get('type', None) is not None:
            filter_values = ProcessRequest.create_filters(args[0].query_params)
            result = self.query_set.filter(**filter_values).all()[kwargs.get('first_record', 0):kwargs.get('end_record',10)]
        else:
            result = self.query_set.all()[kwargs.get('first_record', 0):kwargs.get('end_record', 10)]
        result = self.read_serializer(result, many=True)
        response = process_response(message=_("done!"), data=result.data)
        return Response(data=response, status=status.HTTP_200_OK)
