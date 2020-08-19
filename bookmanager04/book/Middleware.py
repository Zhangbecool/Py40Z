from django.utils.deprecation import MiddlewareMixin


class TestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print('中间件request')

    def process_response(self, request, response):

        print('中间件response')

        return response


class TestMiddleware2(MiddlewareMixin):
    def process_request(self, request):
        print('test2request')

    def process_response(self, request, response):
        print('test2response')
        return response