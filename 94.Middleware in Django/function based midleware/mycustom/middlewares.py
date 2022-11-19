def my_diddleware(get_response):#jub server hit ho ga to es function ka code aik bar run hoga
    print("One Time Initial")
    
    
    def my_function(request): #ye fun view fuc k run hone se phile run ho ga
        print("This is before view")
        
        
        response=get_response(request) #ye code view k execute hone k bad run ho ga
        print("This is after view")
        return response
    
    return my_function    
    