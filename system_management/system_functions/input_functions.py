class ProcessRequest(object):
    @staticmethod
    def create_filters(query_params):
        filter_values = {}
        for key, value in query_params.items():
            try:
                value = eval(value)
            except Exception as e:
                pass

            if key == 'type':
                continue
            if type(value) is str and not value.isdigit():
                filter_values.update({'%s__contains' % key: '%s' % value})
            elif type(value) is int:
                filter_values.update({'%s__exact' % key: value})
            elif type(value) is list:
                filter_values.update({'%s__in' % key: value})
            else:
                filter_values.update({'%s__contains' % key: '%s' % value})
        return filter_values

