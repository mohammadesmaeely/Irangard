from rest_framework.views import APIView
from rest_framework.response import Response
from http import HTTPStatus
from django.utils.translation import ugettext_lazy as _
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from system_management.system_functions.input_functions import ProcessRequest
from system_management.system_functions.output_functions import process_response

from posts_management.serializers import PostReadSerializer, PostSerializer
from posts_management.models import Post


class PostView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    validate_serializer = PostSerializer
    read_serializer = PostReadSerializer
    query_set = Post.objects.filter(is_verify=True)

    def get(self, *args, **kwargs):
        # search filters
        if args[0].query_params.get('type', None) is not None:
            filter_values = ProcessRequest.create_filters(args[0].query_params)
            result = self.query_set.filter(**filter_values).all()[kwargs.get('first_record', 0):kwargs.get('end_record',10)]
        else:
            result = self.query_set.all()[kwargs.get('first_record', 0):kwargs.get('end_record', 10)]
        for res in result:
            res.visit += 1
            res.save()
        result = self.read_serializer(result, many=True)
        response = process_response(message=_("done!"), data=result.data)
        return Response(data=response, status=HTTPStatus.OK)

    def post(self, *args, **kwargs):
        inputs = args[0].data
        inputs['author'] = self.request.user.id
        inputs['is_verify'] = True
        ser = self.validate_serializer(data=inputs)
        if ser.is_valid():
            ser.save()
            response = process_response(message=_("done!"), data=ser.data)
            return Response(data=response, status=HTTPStatus.OK)
        else:
            response = process_response(data=_('occurred error!'), errors=ser.errors)
            return Response(data=response, status=HTTPStatus.BAD_REQUEST)

    def put(self, *args, **kwargs):
        try:
            inputs, pk = args[0].data, args[0].data['pk']
        except Exception as e:
            response = process_response(data=_('occurred error!'), errors=e.args)
            return Response(data=response, status=HTTPStatus.BAD_REQUEST)
        try:
            obj = self.query_set.get(id=pk)
        except Exception as e:
            response = process_response(data=_('there is no exist result with this request!'), errors=e.args)
            return Response(data=response, status=HTTPStatus.NOT_FOUND)
        inputs['author'] = self.request.user.id
        ser = self.validate_serializer(obj, data=inputs)
        if ser.is_valid():
            ser.save()
            response = process_response(message=_("done!"), data=ser.data)
            return Response(data=response, status=HTTPStatus.OK)
        else:
            response = process_response(data=_('occurred error!'), errors=ser.errors)
            return Response(data=response, status=HTTPStatus.BAD_REQUEST)

    def delete(self, *args, **kwargs):
        try:
            pk = args[0].data.get('pk', args[0].query_params['pk'])
        except Exception as e:
            response = process_response(data=_('occurred error!'), errors=e.args)
            return Response(data=response, status=HTTPStatus.BAD_REQUEST)
        try:
            obj = self.query_set.get(id=pk)
        except Exception as e:
            response = process_response(data=_('there is no exist result with this request!'), errors=e.args)
            return Response(data=response, status=HTTPStatus.NOT_FOUND)
        obj.delete()
        response = process_response(message=_("done!"))
        return Response(data=response, status=HTTPStatus.OK)
