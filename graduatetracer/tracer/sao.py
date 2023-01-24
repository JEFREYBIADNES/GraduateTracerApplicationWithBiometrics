from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import *
from .forms import *

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.contrib import messages

from django.conf import settings
from django.utils.encoding import force_str
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


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['is_admin_sao'])
# def DashboardAdmin(request):
#     jobs = Advertise.objects.all().order_by('-date_created')
#     job_categories = JobCategory.objects.all().order_by('-id')
#     announcements = Announcement.objects.all().order_by('-date_created')

#     top_notif_announcements = Announcement.objects.all().order_by(
#         '-date_created').filter(announcement_notif_counter=False)[:3]
#     top_notif_jobs = Advertise.objects.all().order_by(
#         '-date_created').filter(job_advertise_notif_counter=False)[:3]

#     count_users = User.objects.filter(graduate=True).count()
#     count_employed = User.objects.filter(employed=True).count()
#     count_unemployed = User.objects.filter(unemployed=True).count()
#     count_approved = User.objects.filter(approved=True).count()
#     count_pending = 0
    
#     User = User.objects.all()
#     for user in User:
#         if user.graduate and user.pending:
#             count_pending+=1
#             print(count_pending)
    
    
#     # if user 

#     count_jobs_advertised = Advertise.objects.all().count()
#     count_job_requests = JobRequest.objects.all().count()

#     user = request.user
#     user_chat_bot_notifications_counter = chat_bot_notifications_counter(user)
#     user_top_nav_notifications_counter = top_nav_notifications_counter(user)

#     user_announcement_notifications_counter = announcement_notifications_counter(
#         user)
#     user_job_advertise_notifications_counter = job_advertise_notifications_counter(
#         user)
#     user_job_request_notifications_counter = job_request_notifications_counter(
#         user)
#     user_job_category_notif_counter = job_category_notifications_counter(user)

#     vote_results = JobRequest.objects.all().order_by('job_category', '-total_vote')

#     context = {
#                 'announcements': announcements,
#                 'jobs': jobs,
#                 'job_categories': job_categories,
#                 'top_notif_announcements': top_notif_announcements,
#                 'top_notif_jobs': top_notif_jobs,

#                 'count_users': count_users,
#                 'count_employed': count_employed,
#                 'count_unemployed': count_unemployed,
#                 'count_approved': count_approved,
#                 'count_pending': count_pending,
#                 'count_jobs_advertised': count_jobs_advertised,
#                 'count_job_requests': count_job_requests,

#                 'vote_results': vote_results,
#                 'vote_results': vote_results,

#                 'user_chat_bot_notifications_counter': user_chat_bot_notifications_counter,
#                 'user_top_nav_notifications_counter': user_top_nav_notifications_counter,
#                 'user_announcement_notifications_counter': user_announcement_notifications_counter,
#                 'user_job_advertise_notifications_counter': user_job_advertise_notifications_counter,
#                 'user_job_request_notifications_counter': user_job_request_notifications_counter,
#                 'user_job_category_notif_counter': user_job_category_notif_counter,
#                 }

#     return render(request, 'admin/index.html', context)

def SaoDashboard(request):
    jobs = Advertise.objects.all().order_by('-date_created')
    job_categories = JobCategory.objects.all().order_by('-id')
    announcements = Announcement.objects.all().order_by('-date_created')

    top_notif_announcements = Announcement.objects.all().order_by(
        '-date_created').filter(announcement_notif_counter=False)[:3]
    top_notif_jobs = Advertise.objects.all().order_by(
        '-date_created').filter(job_advertise_notif_counter=False)[:3]

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
        

    count_jobs_advertised = Advertise.objects.all().count()
    count_job_requests = JobRequest.objects.all().count()

    user = request.user
    user_chat_bot_notifications_counter = chat_bot_notifications_counter(user)
    user_top_nav_notifications_counter = top_nav_notifications_counter(user)

    user_announcement_notifications_counter = announcement_notifications_counter(
        user)
    user_job_advertise_notifications_counter = job_advertise_notifications_counter(
        user)
    user_job_request_notifications_counter = job_request_notifications_counter(
        user)
    user_job_category_notif_counter = job_category_notifications_counter(user)

    vote_results = JobRequest.objects.all().order_by('job_category', '-total_vote')

    context = {
                'announcements': announcements,
                'jobs': jobs,
                'job_categories': job_categories,
                'top_notif_announcements': top_notif_announcements,
                'top_notif_jobs': top_notif_jobs,

                'count_users': count_users,
                'count_employed': count_employed,
                'count_unemployed': count_unemployed,
                'count_approved': count_approved,
                'count_pending': count_pending,
                'count_jobs_advertised': count_jobs_advertised,
                'count_job_requests': count_job_requests,

                'vote_results': vote_results,
                'vote_results': vote_results,

                'user_chat_bot_notifications_counter': user_chat_bot_notifications_counter,
                'user_top_nav_notifications_counter': user_top_nav_notifications_counter,
                'user_announcement_notifications_counter': user_announcement_notifications_counter,
                'user_job_advertise_notifications_counter': user_job_advertise_notifications_counter,
                'user_job_request_notifications_counter': user_job_request_notifications_counter,
                'user_job_category_notif_counter': user_job_category_notif_counter,
                }
    return render(request, 'admin/saodashboard.html', context)
#Count all Notification

def announcement_notifications_counter(user):
    announcement_notif_counter = Announcement.objects.filter(
        announcement_notif_counter=False).count()

    user.announcement_counter = announcement_notif_counter
    user_announcement_count = user.announcement_counter
    return user_announcement_count


def job_advertise_notifications_counter(user):
    job_advertise_notif_counter = Advertise.objects.filter(
        job_advertise_notif_counter=False).count()

    user.job_advertise_counter = job_advertise_notif_counter
    user_job_advertise_count = user.job_advertise_counter
    return user_job_advertise_count


def job_request_notifications_counter(user):
    job_request_notif_counter = JobRequest.objects.filter(
        job_request_notif_counter=False).count()

    user.job_request_counter = job_request_notif_counter
    user_job_request_count = user.job_request_counter
    return user_job_request_count


def job_category_notifications_counter(user):
    job_category_notif_counter = JobCategory.objects.filter(
        job_category_notif_counter=False).count()

    user.job_category_counter = job_category_notif_counter
    user_job_category_count = user.job_category_counter
    return user_job_category_count


def chat_bot_notifications_counter(user):
    user_notifications_count = job_advertise_notifications_counter(user) + job_request_notifications_counter(
        user) + job_category_notifications_counter(user) + announcement_notifications_counter(user)

    return user_notifications_count


def top_nav_job_announcement_notifications_counter(user):
    announcement_notif_counter = Announcement.objects.filter(
        announcement_notif_counter=False)[:3].count()

    user.announcement_counter = announcement_notif_counter
    user_announcement_count = user.announcement_counter
    return user_announcement_count


def top_nav_job_advertise_notifications_counter(user):
    job_advertise_notif_counter = Advertise.objects.filter(
        job_advertise_notif_counter=False)[:3].count()

    user.job_advertise_counter = job_advertise_notif_counter
    user_job_advertise_count = user.job_advertise_counter
    return user_job_advertise_count


def top_nav_notifications_counter(user):
    user_notifications_count = top_nav_job_advertise_notifications_counter(
        user) + top_nav_job_announcement_notifications_counter(user)

    return user_notifications_count

@login_required(login_url='login')
@allowed_users(allowed_roles=['is_admin_sao'])
def profile_picture(request, pk):
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
                return redirect('saodashboard')
        else:
            if user_info.is_valid():
                user_info.save()
                messages.success(
                    request, 'Your Profile Updated Successfully')
                return redirect('saodashboard')

    context = {'user': user, 'user_info': user_info, 'full_name': full_name}
    return render(request, "admin/profile.html", context)

def display_announcement(request):
    announcements = Announcement.objects.all().order_by('-date_created')
    context = {'announcements': announcements, }
    return render(request, 'admin/display_announcements.html', context)


def add_announcements(request):
    announcements = AnnouncementForm()

    if request.method == 'POST':
        image = request.FILES.get('image')
        announcements = AnnouncementForm(request.POST, request.FILES)
        if announcements.is_valid():
            announcements.save()
            messages.success(
                request, 'You have successfully added a new Announcement')
            return redirect('display_announcements')

    context = {'announcements': announcements, }
    return render(request, 'admin/announcement.html', context)

def update_announcement(request, pk):
    announce = Announcement.objects.get(id=pk)
    announcements = AnnouncementForm(instance=announce)

    if request.method == 'POST':
        announcements = AnnouncementForm(request.POST, request.FILES, instance=announce)
        if announcements.is_valid():
            announcements.save()
            messages.success(
                request, 'You have successfully updated the Announcement')
            return redirect('display_announcements')
    else:
        an = AnnouncementForm()

    context = {'announcements': announcements, }
    return render(request, 'admin/update_announcements.html', context)

def delete_announcement(request, pk):
    delete_announcement = Announcement.objects.get(id=pk)
    delete_announcement.delete()
    messages.success(request, 'Successfully Deleted')
    return redirect('display_announcements')

@login_required(login_url='login')
@allowed_users(allowed_roles=['is_admin_sao'])
def pendingaccounts(request):
    gradAccts = User.objects.all()

    context = {
                'gradAccts': gradAccts
                }
    return render(request, 'admin/pending.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['is_admin_sao'])
def approvedaccounts(request):
    gradAccts = User.objects.all()

    context = {'gradAccts': gradAccts}
    return render(request, 'admin/approved.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['is_admin_sao'])
def ApprovedUser(request, pk):

    if request.method == 'POST':
        user = User.objects.get(id=pk)
        user.pending = False
        user.approved = True
        user.save()
        messages.success(
            request, 'Graduate Successfully Approved')

        template = render_to_string(
                'firstInterface/emailConfirm_template.html',
                {'name': user.first_name})

        email = EmailMessage(
                             'Confirm To Log In',
                             template,
                             settings.EMAIL_HOST_USER,
                             [user.email],
        )

        email.fail_silently = False
        email.send()

    return redirect('approvedaccounts')


def DisapprovedUser(request, pk):
    user_delete = User.objects.get(id=pk)

    if request.method == 'POST':
        user_delete = User.objects.get(id=pk)
        user_delete.delete()
        messages.success(
            request, 'Graduate Successfully DisApproved')
        return redirect('pendingaccounts')

def users(request):

    if 'query' in request.GET:
        query = request.GET['query']
        multiple_query = Q(Q(first_name__icontains=query) | Q(middle_name__icontains=query)
                           | Q(last_name__icontains=query) | Q(job_description__icontains=query) | Q(skill__icontains=query)
                           | Q(date_graduated__icontains=query) | Q(employed__icontains=query) | Q(unemployed__icontains=query))

        if query:
            user_infos = User.objects.filter(multiple_query)
        elif query == None:
            user_infos = User.objects.all()
        elif query == 'Employed' or query == 'employed':
            user_infos = User.objects.filter(employed=True)
        elif query == 'Unemployed' or query == 'unemployed':
            user_infos = User.objects.filter(unemployed=True)
        else:
            user_infos = User.objects.all()
    else:
        user_infos = User.objects.all()
    context = {'user_infos': user_infos}

    return render(request, 'admin/users.html', context)

def userinformation(request, pk):
    user_info = User.objects.get(id=pk)

    context = {'user_info': user_info}
    return render(request, 'admin/userinformation.html', context)

def user_informations(request, pk):
    user_info = User.objects.get(id=pk)
    JobExperience = WorkExperiences.objects.filter(graduateUser=pk)

    context = {
               'JobExperience': JobExperience,
               'user_info': user_info
               }
    return render(request, 'admin/user_infos.html', context)
