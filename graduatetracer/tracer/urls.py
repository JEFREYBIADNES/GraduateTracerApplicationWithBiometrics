from django.urls import path
from .import views
from .import systemadmin
from .import sao
from django.contrib.auth import views as auth_views
from .views import AddLike, AddDislike
urlpatterns = [

    # All
    path('', views.home, name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUSer, name="logout"),
    path('welcomemessage/', views.welcomeMsg, name="welcomeMsg"),



    # User Password Reset
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="firstInterface/password/password_reset.html"),
         name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="firstInterface/password/password_reset_sent.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="firstInterface/password/password_reset_form.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="firstInterface/password/password_reset_done.html"),
         name="password_reset_complete"),




    # graduate User  URLs ...

    path('userdashboard/', views.DashboardUser, name="DashboardUser"),
    path('graduate/display-info/',
         views.DisplayGradInfo, name="DisplayGradInfo"),
    path('graduate/update-information/<str:pk>/',
         views.UpdateGradInfo, name='UpdateGradInfo'),
    path('graduates/profile/', views.GradProfilePicture, name="GradProfilePicture"),

    path('view_ads/<int:pk>/', views.view_ads, name="view_ads"),
    path('graduate/index/job/experiences/',
         views.HomeJobExperience, name="HomeJobExperience"),
    path('categorized-job/<int:category>',
         views.categorized_job, name="categorized_job"),
    path('graduates/AddJobExperience/',
         views.AddJobExperience, name="AddJobExperience"),
    path('graduates/EDITJobExperience/<int:id>',
         views.edit_experience, name="edit_experience"),
    path('graduates/DELETEJobExperience/<int:id>',
         views.delete_experience, name="delete_experience"),
    path('friendlist/', views.FriendsList, name="friendlist"),
    path('About/', views.AboutView, name="about"),



    # URLs for posting updates

    path('newsfeed/post/', views.PostTimeline, name='post-list'),
    path('newsfeed/edit-post/<int:pk>/', views.EditPostTimeline, name='post-edit'),
    path('delete_post/<int:pk>/', views.DeletePostTimeline, name="delete_post"),
    path('post_comment/<str:id>/', views.CommentPostTimeline, name="post-comment"),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),

    path('notification-job-announcement/<int:pk>/',
         views.display_announcement_notification, name="display_announcement_notification"),
    path('notification-job-advertised/<int:pk>/', views.display_job_advertised_notification,
         name="display_job_advertised_notification"),
    path('notification-job-request/<int:pk>/', views.display_job_request_notification,
         name="display_job_request_notification"),
    path('notification-job-category/<int:pk>/', views.display_job_category_notification,
         name="display_job_category_notification"),


    # Sao URLs ...
    
    path('saodashboard/', sao.SaoDashboard, name="saodashboard"),
#     path('admindashboard/', sao.DashboardAdmin, name="DashboardAdmin"),
    path('profile-picture/<int:pk>/', sao.profile_picture, name="profile_picture"),
    path('announcement/', sao.add_announcements, name="add_announcements"),
    path('update_announcement/<int:pk>/', sao.update_announcement, name="update_announcement"),
    path('delete_announcement/<int:pk>/', sao.delete_announcement, name="delete_announcement"),
    path('browse-announcements/', sao.display_announcement,
         name="display_announcements"),
    path('users/', sao.users, name="users"),
    path('user-infos/<int:pk>/', sao.user_informations, name="user_informations"),

    #create accounts
    path('approvedaccounts/', sao.approvedaccounts, name='approvedaccounts'),
    path('pendingaccounts/', sao.pendingaccounts, name='pendingaccounts'),
    path('approved/user/<int:pk>/', sao.ApprovedUser, name='approvedUser'),
    path('disapproved/user/<int:pk>/', sao.DisapprovedUser, name='disapprovedUser'),
    path('userinformation/<int:pk>', sao.userinformation, name='userinformation'),



    path('advertise-jobs/', views.advertise, name="advertise"),
    path('advertise-sent-history/<int:pk>/', views.advertise_sent_history, name="advertise_sent_history"),
    path('view-job/<int:pk>/', views.view_ad, name="view_ad"),
    path('update-advertisement/<int:pk>/', views.update_ad, name="update_ad"),
    path('delete-advertisement/<int:pk>/', views.delete_ad, name="delete_ad"),

    path('browse-jobs/', views.browser, name="browser"),
    path('categorized-jobs/<int:category>',
         views.categorized_jobs, name="categorized_jobs"),

    path('job-requests/', views.job_requests, name="job_requests"),
    path('delete-job-request/<int:pk>/',
         views.delete_job_request, name='delete_job_request'),







    # Graduate Tracer - Adminz
    #Jobs
    path('browse-available-jobs/', views.available_jobs, name="available_jobs"),
    path('add-jobs/', views.add_job_categories, name='add_jobs'),
    path('display-jobs/', views.display_job_categories, name='display_jobs'),
    path('update-jobs/<int:pk>/', views.update_job_category,
         name='update_job_category'),
    path('delete-jobs/<int:pk>/', views.delete_job_category,
         name='delete_job_category'),
    #Job Types
    path('add-job-types/', views.add_category_types, name='add_job_types'),
    path('display-types-of-job/', views.display_category_types,
         name='display_job_types'),
    path('update-job-types/<int:pk>/',
         views.update_category_type, name='update_job_type'),
    path('delete-job-types/<int:pk>/',
         views.delete_category_type, name='delete_job_type'),





    #admindashboard
     path('admindash/', systemadmin.admindash, name='admindash'),
     path('create-user-management', systemadmin.create_user_management, name="create_user_management"),

     path('display-user-management', systemadmin.display_user_management, name="display_user_management"),

     #School Reports
     path('school-report/', systemadmin.school_report, name='school_report'),
     path('school-record/', systemadmin.school_record, name='school_record'),
     #users
     path('user-graduates/', systemadmin.user_graduates, name='user_graduates'),
     path('usergrad-info/<int:pk>/', systemadmin.usergrad_informations, name="usergrad_informations"),

     path('adprof/<int:pk>', systemadmin.adprof, name='adprof'),

    ]
