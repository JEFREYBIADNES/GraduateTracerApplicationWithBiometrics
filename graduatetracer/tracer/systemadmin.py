from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import *
from .forms import *

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.contrib import messages

from django.conf import settings

from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from .decorators import unauthenticated_user, allowed_users
from .forms import RegisterForm, RegisterAdminForm, Profile, GraduateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.mail import EmailMessage



# ADMIN
@login_required(login_url='login')
def admindash(request):
    count_users = User.objects.filter(approved=True).count()
    count_employed = 0
    count_unemployed = 0
    count_approved = User.objects.filter(approved=True).count()
    count_pending = 0
    users = User.objects.all()
    for user in users: 
        if user.graduate and user.pending:
            count_pending+=1
        elif user.graduate and user.approved and user.employed:
            count_employed+=1
        elif user.graduate and user.approved and user.unemployed:
            count_unemployed+=1
        
    context = {
                'count_users': count_users,
                'count_employed': count_employed,
                'count_unemployed': count_unemployed,
                'count_approved': count_approved,
                'count_pending': count_pending,
                }
    return render(request, 'systemadmin/admindash.html', context)

@login_required(login_url='login')
def create_user_management(request):
    adform = RegisterAdminForm()
    if request.method == 'POST':
        adform = RegisterAdminForm(request.POST)
        if adform.is_valid():
            adform.save()
            messages.success(
                request, 'New Account Created Successfully!')
            return redirect('display_user_management')
        else:
            messages.info(
                request, 'The email you used is taken already.')

    context = {'adform': adform}
    return render(request, 'systemadmin/create_user_management.html', context)

@login_required(login_url='login')
def display_user_management(request):
    ad_info = User.objects.all
    context = {
               'ad_info': ad_info
               }
    return render(request, 'systemadmin/display_user_management.html', context)

@login_required(login_url='login')
def user_graduates(request):
    user_info = User.objects.all().order_by('-id')
    query_IDNum = []
    query_school = []
    query_employment_status = []

    for user_info in user_info:
        if user_info.IDNum not in query_IDNum:
            query_IDNum.append(user_info.IDNum)
        if user_info.school not in query_school:
            query_school.append(user_info.school)
        if user_info.employment_status not in query_employment_status:
            query_employment_status.append(user_info.employment_status)

    if 'query' in request.GET:
        query = request.GET['query']
        multiple_query = Q(Q(first_name__icontains=query) | Q(middle_name__icontains=query)| Q(last_name__icontains=query)
                           | Q(email__icontains=query))
        if query:
            user_info = User.objects.filter(multiple_query)

        else:
            user_info = User.objects.all().order_by('-id')
    else:
        user_info = User.objects.all().order_by('-id')

    context = {
                'user_info': user_info,
                'query_IDNum': query_IDNum,
                'query_school': query_school,
                'query_employment_status': query_employment_status,
                }
    return render(request, 'systemadmin/user_graduates.html', context)

@login_required(login_url='login')
def usergrad_informations(request, pk):
    user_info = User.objects.get(id=pk)
    JobExperience = WorkExperiences.objects.filter(graduateUser=pk)

    context = {
               'JobExperience': JobExperience,
               'user_info': user_info
               }
    return render(request, 'systemadmin/usergrad_info.html', context)

@login_required(login_url='login')
def adprof(request, pk):
    user = User.objects.get(id=pk)
    user_info = ProfileForm(instance=user)
    full_name = None
    if request.method == 'POST':
        profile_picture = request.FILES.get('profile')
        user_info = ProfileForm(request.POST, instance=user)
        if profile_picture:
            if user_info.is_valid():
                fs = FileSystemStorage()
                user.profile_picture = fs.save(
                    profile_picture.name, profile_picture)
                user_info.save()
                messages.success(
                    request, 'Your Profile Updated Successfully')
                return redirect('admindash')
        else:
            if user_info.is_valid():
                user_info.save()
                messages.success(
                    request, 'Your Profile Updated Successfully')
                return redirect('admindash')

    context = {'user': user, 'user_info': user_info, 'full_name': full_name}
    return render(request, 'systemadmin/adprof.html', context)


@login_required(login_url='login')
def school_report(request):
    table = []
    class sr:
        def __init__(self, school_list, graduate, employed, unemployed):
            self.school_list = school_list
            self.graduate = graduate
            self.employed = employed
            self.unemployed = unemployed
    users = User.objects.all()
    graduate_counter = []
    employed_counter = []
    unemployed_counter = []
    school_list = ["Argao Campus", "Barili Campus", "Carmen Campus", "Cebu City Mountain Extension Campus", "Daanbantayan Campus", "Danao Campus", "Dumanjug Extension Campus", "Ginatilan Extension Campus", "Malabuyoc Extension Campus", "Main Campus", "Moalboal Campus", "Naga Extension Campus", "Oslob Extension Campus", "Pinamungajan Extension Campus", "San Fernando Extension Campus", "San Francisco Campus", "Tuburan Campus"]
 
    i = 0
    j = 0
    while i != len(school_list):
        graduate_counter+=[0]
        employed_counter+=[0]
        unemployed_counter+=[0]
        i+=1
    for user in users:
        if user.graduate and user.approved:
            while j != len(school_list):
                if user.school == school_list[j]:
                    graduate_counter[j]+=1
                    if user.employed:
                        employed_counter[j]+=1
                    else:
                        unemployed_counter[j]+=1
                    j=0
                    break
                j+=1
 
    print(graduate_counter)
    print(employed_counter)
    print(unemployed_counter)
    for k in range(len(school_list)):
        schools = school_list[k]
        graduate = graduate_counter[k]
        employed = employed_counter[k]
        unemployed = unemployed_counter[k]
        s = sr(schools, graduate, employed, unemployed)
        table.append(s)
 
    context = {'table':table}
    return render(request, 'systemadmin/school_report.html', context)


def school_record(request):
    context = {}
    return render(request, 'systemadmin/school_record.html', context)
