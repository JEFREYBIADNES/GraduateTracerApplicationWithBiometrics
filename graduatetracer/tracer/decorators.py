from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_graduate:
                return redirect('DashboardUser')
            elif request.user.is_admin_sao:
                return redirect('saodashboard')
            elif request.user.is_system_admin:
                return redirect('admindash')
            else:
                return HttpResponse('You are not authorized to view this page')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            permissions = None
            if request.user.approved:
                permissions = 'is_graduate'
            elif request.user.is_admin_sao:
                permissions = 'is_admin_sao'
            elif request.user.is_system_admin:
                permissions = 'is_system_admin'
            elif request.user.is_admin:
                permissions = 'is_admin'

            if permissions in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        
        permissions = None
        if request.user.is_graduate:
            permissions = 'is_graduate'
        elif request.user.is_admin_sao:
            permissions = 'is_admin_sao'
        elif request.user.is_system_admin:
            permissions = 'is_system_admin'
        if permissions == 'is_graduate':
            return redirect('DashboardUser')

        if permissions == 'is_admin':
            return view_func(request, *args, **kwargs)

    return wrapper_function
