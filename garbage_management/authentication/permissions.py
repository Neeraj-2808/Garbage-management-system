from django.shortcuts import render,redirect

def permission_roles(roles):

    def decorator(fn):

        def wrapper (request,*args,**kwargs):

            if request.user.is_authenticated and request.user.role in roles:
                return fn(request,*args,**kwargs)
            

            else:
                return render(request,'errorpages/error-403.html')
        
        return wrapper
    
    return decorator