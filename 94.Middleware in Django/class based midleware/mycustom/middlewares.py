class My_Mdiddleware:
    def __init__(self, get_response):  #jub server hit ho ga to es function ka code aik bar run hoga
        self.get_response = get_response 
        print("One Time Initial")   
        
    def __call__(self,requset):  #ye fun view fuc k run hone se phile run ho ga
        print("This is before View")
        response = self.get_response(requset) #ye code view k execute hone k bad run ho ga
        print("This is after view")
        return response