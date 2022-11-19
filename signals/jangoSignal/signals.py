from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_save,pre_delete,post_init,post_save,post_delete
from django.core.signals import request_started,request_finished,got_request_exception

@receiver(user_logged_out,sender=User)  #use decorater
def logged_out(sender,request,user, **kwargs):
    print("logout signal ######################")
    print("-----------------------------")
    print("Logged-out Signal... Run Outro..")
    print("Sender:",sender)
    print("Request:",request)
    print("User:",user)
    print(f'Kwargs: {kwargs}')
    
# user_logged_out.connect(log_out,sender=User) #user connect 

@receiver(user_logged_in,sender=User)   #use decorater
def logged_in(sender,request,user, **kwargs):
    print("login signal ######################")
    print("-----------------------------")
    print("Logged-in Signal... Run-login ")
    print("Sender:",sender)
    print("Request:",request)
    print("User:",user)
    print(f'Kwargs: {kwargs}')
    
# user_logged_in.connect(login,sender=User)  #user connect 

@receiver(user_login_failed)   #use decorater
def login_failed(sender,credentials,request, **kwargs):
    print("login failed ######################")
    print("-----------------------------")
    print("Login failed Signal... ")
    print("Sender:",sender)
    print("Request:",request)
    print("Request:",request)
    print(f'Kwargs: {kwargs}')
    
# user_login_failed.connect(login_failed)  #user connect 


@receiver(pre_save,sender=User)   #use decorater
def At_beggining_save(sender,instance, **kwargs):
    
    print("-----------------------------")
    print("Pre save Signal... ")
    print("Sender:",sender)
    print("Instance:",instance)
    print(f'Kwargs: {kwargs}')
    
@receiver(post_save,sender=User)   #use decorater
def At_ending_save(sender,instance,created, **kwargs):
    if created:
        print("-----------------------------")
        print("Post save Signal... ")
        print("New Record")
        print("Sender:",sender)
        print("Instance:",instance)
        print("Created:",created)
        print(f'Kwargs: {kwargs}')     
    else:
        print("-----------------------------")
        print("Post save Signal... ")
        print("Sender:",sender)
        print("Updated")
        print("Instance:",instance)
        print("Created:",created)
        print(f'Kwargs: {kwargs}')
        

@receiver(pre_delete,sender=User)   #use decorater
def at_begning_delete(sender,instance, **kwargs):
    
    print("-----------------------------")
    print("pre Delete Signal... ")
    print("Sender:",sender)
    print("Instance:",instance)
    print(f'Kwargs: {kwargs}') 
    
@receiver(post_delete,sender=User)   #use decorater
def at_ending_delete(sender,instance, **kwargs):  
    print("-----------------------------")
    print("post ending Delete Signal... ")
    print("Sender:",sender)
    print("Instance:",instance)
    print(f'Kwargs: {kwargs}')
    
@receiver(pre_init,sender=User)   #use decorater
def at_beginning_init(sender,*args, **kwargs):  
    print("-----------------------------")
    print("pre init Signal... ")
    print("Sender:",sender)
    print(f'Args':{args})
    print(f'Kwargs: {kwargs}') 
    

@receiver(post_init,sender=User)   #use decorater
def at_ending_init(sender,*args, **kwargs):  
    print("-----------------------------")
    print("Post init Signal... ")
    print("Sender:",sender)
    print(f'Args':{args})
    print(f'Kwargs: {kwargs}') 
    
@receiver(request_started)   #use decorater
def at_beginning_request(sender,environ, **kwargs):  
    print("-----------------------------")
    print("At beginning request... ")
    print("Sender:",sender)
    print(f'Environ':{environ}')
    print(f'Kwargs: {kwargs}')        
    
@receiver(got_request_exception)   #use decorater
def at_req_exception(sender,environ, **kwargs):  
    print("-----------------------------")
    print("At request  Exception... ")
    print("Sender:",sender)
    print(f'Environ':{environ}')
    print(f'Kwargs: {kwargs}')        
            
    
     
        
    
           
               

 
