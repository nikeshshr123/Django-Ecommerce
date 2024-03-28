from django.shortcuts import redirect

#mob veri
#esrai aws garda category wala



# to check if user is logged in or not
def Unauthenticated_user(view_function):
    def wrapper_function(request, *args,**Kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_function(request,*args,**kwargs)
    return wrapper_function

#give access to admin page if user requeest comes from staff is 1 otherwise give access to normal page
def admin_only(view_function):
    def wrapper_function(request, *args,**Kwargs):
        if request.user.is_staff:
            return view_function(request, *args,**Kwargs)
        else:
            return redirect('/')
    return wrapper_function