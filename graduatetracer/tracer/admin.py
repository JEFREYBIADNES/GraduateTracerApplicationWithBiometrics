from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
 
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import Post, Comment, WorkExperiences
User = get_user_model()
 
 
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
 
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'admin')
    list_filter = ('admin', 'staff', 'employed', 'unemployed',
                    'argaoCampus',
                    'bariliCampus',
                    'carmenCampus',
                    'CCMECampus',
                    'daanbantayanCampus',
                    'danaoCampus',
                    'dumanjugExt',
                    'ginatilanExt',
                    'malabuyocExt',
                    'mainCampus',
                    'moalboalCampus',
                    'nagaExt',
                    'oslobExt',
                    'pinamungajanExt',
                    'sanfernandoExt',
                    'sanfranciscoCampus',
                    'tuburanCampus','is_active')
 
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('profile_picture',
                                      'IDNum',
                                      'first_name',
                                      'middle_name',
                                      'last_name',
                                      'pending',
                                      'approved')}),
        ('School', {'fields': ('school',
                                 'argaoCampus',
                                 'bariliCampus',
                                 'carmenCampus',
                                 'CCMECampus',
                                 'daanbantayanCampus',
                                 'danaoCampus',
                                 'dumanjugExt',
                                 'ginatilanExt',
                                 'malabuyocExt',
                                 'mainCampus',
                                 'moalboalCampus',
                                 'nagaExt',
                                 'oslobExt',
                                 'pinamungajanExt',
                                 'sanfernandoExt',
                                 'sanfranciscoCampus',
                                 'tuburanCampus',)}),
        ('Permissions', {'fields': ('admin', 'staff', 'is_active')}),
        ('Types of User', {'fields': ('user_type','graduate', 'admin_sao','system_admin','dean','campus_director','university_pres')}),
        ('Graduate Status', {'fields': ('employment_status','employed', 'unemployed')}),
 
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ['email', 'first_name', 'last_name', ]
    ordering = ['email']
    filter_horizontal = ()
 
 
admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(WorkExperiences)
 
 
admin.site.unregister(Group)
 
 

