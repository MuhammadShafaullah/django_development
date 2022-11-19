from django.shortcuts import HttpResponse,render
class underConstructionMiddleware:
    def __init__(self,get_response):
        self.get_response =get_response
    
    def __call__(self,request):
        print("Call From Middleware")
        # response =self.get_response(request)
        # response=HttpResponse("This is Under Construction")
        response= render(request,'mysite/underconstruction.html')
        print("Call From Middleware After view")
        return response    