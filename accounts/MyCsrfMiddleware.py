# from django.utils.deprecation import MiddlewareMixin
#
#
# # class MyCsrfMiddleware(MiddlewareMixin):
# #
# #     def process_response(self, request, response):
# #         response["Access-Control-Allow-Origin"] = "*"
# #         if request.method == "OPTIONS":
# #             response["Access-Control-Allow-Headers"] = "Content-Type"
# #             response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST, GET"
# #         return response
#
#
# # 继承 MiddlewareMixin
# class MyCsrfMiddleware(MiddlewareMixin): # 继承 MiddlewareMixin
#     def process_reponse(self, request, response):
#         if request.method == "OPTIONS":   # 如果操作的是删除指令这里在这里判断下面 return 返回
#             response["Access-Control-Allow-methods"] = "DELETE, PUT, POST, GET"
#             # 处理跨域的中间件，将所有的响应都能实现跨域
#             response["Access-Control-Allow-Origin"] = "http://localhost:8083"
#             response["Access-Control-Allow-Headers"] = "Content-Type"
#         return response


class MiddlewareMixin(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()

    def __call__(self, request):
        response = None
        if hasattr(self, 'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self, 'process_response'):
            response = self.process_response(request, response)
        return response


class CORSMiddleware(MiddlewareMixin):

    def process_response(self,request,response):
        # 添加响应头

        # 允许你的域名来获取我的数据
        response['Access-Control-Allow-Origin'] = "*"

        # 允许你携带Content-Type请求头
        response['Access-Control-Allow-Headers'] = "Content-Type"

        # 允许你发送DELETE,PUT
        response['Access-Control-Allow-Methods'] = "DELETE,PUT, GET, POST"

        return response


    """
    CORS策略已阻止从来源“ http：// localhost：8083”访问“ 
    http://127.0.0.1:8000/test/?text=uni.request”
    处的XMLHttpRequest：请求标头字段custom-header未被接受
     在飞行前响应中由Access-Control-Allow-Headers允许。
    """