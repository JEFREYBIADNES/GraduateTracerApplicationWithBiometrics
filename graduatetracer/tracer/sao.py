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

    #countuser
    argao_count_users= 0
    barili_count_users = 0
    carmen_count_users = 0
    cebu_count_users = 0
    daan_count_users = 0
    dumanjug_count_users = 0
    danao_count_users = 0
    ginatilan_count_users = 0
    malabuyoc_count_users = 0
    main_count_users = 0
    moalboal_count_users = 0
    naga_count_users = 0
    oslob_count_users = 0
    pinamungajan_count_users = 0
    sanfernando_count_users = 0
    sanfrancisco_count_users = 0
    tuburan_count_users = 0
    # unemployed
    argao_count_unemployed= 0
    barili_count_unemployed = 0
    carmen_count_unemployed = 0
    cebu_count_unemployed = 0
    daan_count_unemployed = 0
    dumanjug_count_unemployed = 0
    danao_count_unemployed = 0
    ginatilan_count_unemployed = 0
    malabuyoc_count_unemployed = 0
    main_count_unemployed = 0
    moalboal_count_unemployed = 0
    naga_count_unemployed = 0
    oslob_count_unemployed = 0
    pinamungajan_count_unemployed = 0
    sanfernando_count_unemployed = 0
    sanfrancisco_count_unemployed = 0
    tuburan_count_unemployed = 0

    #employed
    argao_count_employed= 0
    barili_count_employed = 0
    carmen_count_employed = 0
    cebu_count_employed = 0
    daan_count_employed = 0
    dumanjug_count_employed = 0
    danao_count_employed = 0
    ginatilan_count_employed = 0
    malabuyoc_count_employed = 0
    main_count_employed = 0
    moalboal_count_employed = 0
    naga_count_employed = 0
    oslob_count_employed = 0
    pinamungajan_count_employed = 0
    sanfernando_count_employed = 0
    sanfrancisco_count_employed = 0
    tuburan_count_employed = 0

    #approved
    argao_count_approved= 0
    barili_count_approved = 0
    carmen_count_approved = 0
    cebu_count_approved = 0
    daan_count_approved = 0
    dumanjug_count_approved = 0
    danao_count_approved = 0
    ginatilan_count_approved = 0
    malabuyoc_count_approved = 0
    main_count_approved = 0
    moalboal_count_approved = 0
    naga_count_approved = 0
    oslob_count_approved = 0
    pinamungajan_count_approved = 0
    sanfernando_count_approved = 0
    sanfrancisco_count_approved = 0
    tuburan_count_approved = 0

    #pending
    argao_count_pending= 0
    barili_count_pending = 0
    carmen_count_pending = 0
    cebu_count_pending = 0
    daan_count_pending = 0
    dumanjug_count_pending = 0
    danao_count_pending = 0
    ginatilan_count_pending = 0
    malabuyoc_count_pending = 0
    main_count_pending = 0
    moalboal_count_pending = 0
    naga_count_pending = 0
    oslob_count_pending = 0
    pinamungajan_count_pending = 0
    sanfernando_count_pending = 0
    sanfrancisco_count_pending = 0
    tuburan_count_pending = 0

    users = User.objects.all()
    for user in users:
# PENDING
        if user.graduate and user.pending:
            if user.is_argaoCampus:
                argao_count_pending+=1
            elif user.is_bariliCampus:
                barili_count_pending+=1
            elif user.is_carmenCampus:
                carmen_count_pending+=1
            elif user.is_CCMECampus:
                cebu_count_pending+=1
            elif user.is_daanbantayanCampus:
                daan_count_pending+=1
            elif user.is_dumanjugExt:
                dumanjug_count_pending+=1
            elif user.is_danaoCampus:
                danao_count_pending+=1
            elif user.is_ginatilanExt:
                ginatilan_count_pending+=1
            elif user.is_malabuyocExt:
                malabuyoc_count_pending+=1
            elif user.is_mainCampus:
                main_count_pending+=1
            elif user.is_moalboalCampus:
                moalboal_count_pending+=1
            elif user.is_nagaExt:
                naga_count_pending+=1
            elif user.is_oslobExt:
                oslob_count_pending+=1
            elif user.is_pinamungajanExt:
                pinamungajan_count_pending+=1
            elif user.is_sanfernandoExt:
                sanfernando_count_pending+=1
            elif user.is_sanfranciscoCampus:
                sanfrancisco_count_pending+=1
            elif user.is_tuburanCampus:
                tuburan_count_pending+=1
#cOUNT USER
        elif user.graduate and user.approved:
            if user.is_argaoCampus:
                argao_count_users+=1
                argao_count_approved+=1
                if user.employed:
                    argao_count_employed+=1
                elif user.unemployed:
                    argao_count_unemployed+=1
                
            elif user.is_bariliCampus:
                barili_count_users+=1
                barili_count_approved+=1
                if user.employed:
                    barili_count_employed+=1
                elif user.unemployed:
                    barili_count_unemployed+=1

            elif user.is_carmenCampus:
                carmen_count_users+=1
                carmen_count_approved+=1
                if user.employed:
                    carmen_count_employed+=1
                elif user.unemployed:
                    carmen_count_unemployed+=1

            elif user.is_CCMECampus:
                cebu_count_users+=1
                cebu_count_approved+=1
                if user.employed:
                    cebu_count_employed+=1
                elif user.unemployed:
                    cebu_count_unemployed+=1

            elif user.is_daanbantayanCampus:
                daan_count_users+=1
                daan_count_approved+=1
                if user.employed:
                    daan_count_employed+=1
                elif user.unemployed:
                    daan_count_unemployed+=1

            elif user.is_dumanjugExt:
                dumanjug_count_users+=1
                dumanjug_count_approved+=1
                if user.employed:
                    dumanjug_count_employed+=1
                elif user.unemployed:
                    dumanjug_count_unemployed+=1

            elif user.is_danaoCampus:
                danao_count_users+=1
                danao_count_approved+=1
                if user.employed:
                    danao_count_employed+=1
                elif user.unemployed:
                    danao_count_unemployed+=1
                    
            elif user.is_ginatilanExt:
                ginatilan_count_users+=1
                ginatilan_count_approved+=1
                if user.employed:
                    ginatilan_count_employed+=1
                elif user.unemployed:
                    ginatilan_count_unemployed+=1

            elif user.is_malabuyocExt:
                malabuyoc_count_users+=1
                malabuyoc_count_approved+=1
                if user.employed:
                    malabuyoc_count_employed+=1
                elif user.unemployed:
                    malabuyoc_count_unemployed+=1

            elif user.is_mainCampus:
                main_count_users+=1
                main_count_approved+=1
                if user.employed:
                    main_count_employed+=1
                elif user.unemployed:
                    main_count_unemployed+=1

            elif user.is_moalboalCampus:
                moalboal_count_users+=1
                moalboal_count_approved+=1
                if user.employed:
                    moalboal_count_employed+=1
                elif user.unemployed:
                    moalboal_count_unemployed+=1

            elif user.is_nagaExt:
                naga_count_users+=1
                naga_count_approved+=1
                if user.employed:
                    naga_count_employed+=1
                elif user.unemployed:
                    naga_count_unemployed+=1

            elif user.is_oslobExt:
                oslob_count_users+=1
                oslob_count_approved+=1
                if user.employed:
                    oslob_count_employed+=1
                elif user.unemployed:
                    oslob_count_unemployed+=1

            elif user.is_pinamungajanExt:
                pinamungajan_count_users+=1
                pinamungajan_count_approved+=1
                if user.employed:
                    pinamungajan_count_employed+=1
                elif user.unemployed:
                    pinamungajan_count_unemployed+=1

            elif user.is_sanfernandoExt:
                sanfernando_count_users+=1
                sanfernando_count_approved+=1
                if user.employed:
                    sanfernando_count_employed+=1
                elif user.unemployed:
                    sanfernando_count_unemployed+=1

            elif user.is_sanfranciscoCampus:
                sanfrancisco_count_users+=1
                sanfrancisco_count_approved+=1
                if user.employed:
                     sanfrancisco_count_employed+=1
                elif user.unemployed:
                     sanfrancisco_count_unemployed+=1

            elif user.is_tuburanCampus:
                tuburan_count_users+=1
                tuburan_count_approved+=1
                if user.employed:
                    tuburan_count_employed+=1
                elif user.unemployed:
                    tuburan_count_unemployed+=1
        

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

                'argao_count_users':argao_count_users,
                'barili_count_users':barili_count_users,
                'carmen_count_users':carmen_count_users,
                'cebu_count_users':cebu_count_users,
                'daan_count_users':daan_count_users,
                'dumanjug_count_users':dumanjug_count_users,
                'danao_count_users':danao_count_users,
                'ginatilan_count_users':ginatilan_count_users,
                'malabuyoc_count_users':malabuyoc_count_users,
                'main_count_users':main_count_users,
                'moalboal_count_users':moalboal_count_users,
                'naga_count_users':naga_count_users,
                'oslob_count_users':oslob_count_users,
                'pinamungajan_count_users':pinamungajan_count_users,
                'sanfernando_count_users':sanfernando_count_users,
                'sanfrancisco_count_users':sanfrancisco_count_users,
                'tuburan_count_users':tuburan_count_users,

                'argao_count_employed':argao_count_employed,
                'barili_count_employed':barili_count_employed,
                'carmen_count_employed':carmen_count_employed,
                'cebu_count_employed':cebu_count_employed,
                'daan_count_employed':daan_count_employed,
                'dumanjug_count_employed':dumanjug_count_employed,
                'danao_count_employed':danao_count_employed,
                'ginatilan_count_employed':ginatilan_count_employed,
                'malabuyoc_count_employed':malabuyoc_count_employed,
                'main_count_employed':main_count_employed,
                'moalboal_count_employed':moalboal_count_employed,
                'naga_count_employed':naga_count_employed,
                'oslob_count_employed':oslob_count_employed,
                'pinamungajan_count_employed':pinamungajan_count_employed,
                'sanfernando_count_employed':sanfernando_count_employed,
                'sanfrancisco_count_employed':sanfrancisco_count_employed,
                'tuburan_count_employed':tuburan_count_employed,

                'argao_count_approved':argao_count_approved,
                'barili_count_approved':barili_count_approved,
                'carmen_count_approved':carmen_count_approved,
                'cebu_count_approved':cebu_count_approved,
                'daan_count_approved':daan_count_approved,
                'dumanjug_count_approved':dumanjug_count_approved,
                'danao_count_approved':danao_count_approved,
                'ginatilan_count_approved':ginatilan_count_approved,
                'malabuyoc_count_approved':malabuyoc_count_approved,
                'main_count_approved':main_count_approved,
                'moalboal_count_approved':moalboal_count_approved,
                'naga_count_approved':naga_count_approved,
                'oslob_count_approved':oslob_count_approved,
                'pinamungajan_count_approved':pinamungajan_count_approved,
                'sanfernando_count_approved':sanfernando_count_approved,
                'sanfrancisco_count_approved':sanfrancisco_count_approved,
                'tuburan_count_approved':tuburan_count_approved,

                'argao_count_pending':argao_count_pending,
                'barili_count_pending':barili_count_pending,
                'carmen_count_pending':carmen_count_pending,
                'cebu_count_pending':cebu_count_pending,
                'daan_count_pending':daan_count_pending,
                'dumanjug_count_pending':dumanjug_count_pending,
                'danao_count_pending':danao_count_pending,
                'ginatilan_count_pending':ginatilan_count_pending,
                'malabuyoc_count_pending':malabuyoc_count_pending,
                'main_count_pending':main_count_pending,
                'moalboal_count_pending':moalboal_count_pending,
                'naga_count_pending':naga_count_pending,
                'oslob_count_pending':oslob_count_pending,
                'pinamungajan_count_pending':pinamungajan_count_pending,
                'sanfernando_count_pending':sanfernando_count_pending,
                'sanfrancisco_count_pending':sanfrancisco_count_pending,
                'tuburan_count_pending':tuburan_count_pending,
                
                'argao_count_unemployed':argao_count_unemployed,
                'barili_count_unemployed':barili_count_unemployed,
                'carmen_count_unemployed':carmen_count_unemployed,
                'cebu_count_unemployed':cebu_count_unemployed,
                'daan_count_unemployed':daan_count_unemployed,
                'dumanjug_count_unemployed':dumanjug_count_unemployed,
                'danao_count_unemployed':danao_count_unemployed,
                'ginatilan_count_unemployed':ginatilan_count_unemployed,
                'malabuyoc_count_unemployed':malabuyoc_count_unemployed,
                'main_count_unemployed':main_count_unemployed,
                'moalboal_count_unemployed':moalboal_count_unemployed,
                'naga_count_unemployed':naga_count_unemployed,
                'oslob_count_unemployed':oslob_count_unemployed,
                'pinamungajan_count_unemployed':pinamungajan_count_unemployed,
                'sanfernando_count_unemployed':sanfernando_count_unemployed,
                'sanfrancisco_count_unemployed':sanfrancisco_count_unemployed,
                'tuburan_count_unemployed':tuburan_count_unemployed,

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
        
        # Send a password reset email to the user
        reset_url = f"{request.scheme}://{request.get_host()}/login/"
        subject = 'Approved Email'
        message = render_to_string('firstInterface/approved_email.html', {'reset_url': reset_url})
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]
        send_mail(subject, message, from_email,
                  recipient_list, html_message=message)

        # template = render_to_string(
        #         'firstInterface/emailConfirm_template.html',
        #         {'name': user.first_name})

        # email = EmailMessage(
        #                      'Confirm To Log In',
        #                      template,
        #                      settings.EMAIL_HOST_USER,
        #                      [user.email],
        # )

        # email.fail_silently = False
        # email.send()

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
