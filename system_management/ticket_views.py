from rest_framework.views import APIView
from rest_framework.response import Response
from http import HTTPStatus
from django.utils.translation import ugettext_lazy as _

from system_management.system_functions.input_functions import ProcessRequest
from system_management.system_functions.output_functions import process_response
from system_management.system_functions.permissions import JustPostForUnidentified

from system_management.serializers import TicketSerializer
from system_management.models import Ticket


class TicketView(APIView):
    permission_classes = [JustPostForUnidentified]
    validate_serializer = TicketSerializer
    read_serializer = TicketSerializer
    query_set = Ticket.objects

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
        ser = self.validate_serializer(data=inputs)
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
