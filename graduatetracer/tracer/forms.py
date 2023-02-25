from .models import *
from django import forms
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
 
User = get_user_model()
 
 
class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ('profile_picture',
                  'email',
                  'IDNum',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'birth_date',
                  'age',
                  'gender',
                  'address',
                  'contact_number',
                  'date_graduated',
                  'course_type',
                  'school',
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
                  'tuburanCampus',
                  'user_type',
                  'admin_sao', 'graduate',
                  'system_admin','dean','campus_director','university_pres',
                  'job_description',
                  'skill',
                  'employment_status',
                  'employed',
                  'unemployed'
        )
 
    def clean_password2(self):
        '''
        Verify both passwords match.
        '''
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
 
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_active = True
 
        if commit:
            user.is_active = True
            user.save()
        return user
 
 
class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()
 
    class Meta:
        model = User
        fields = ('profile_picture',
                  'IDNum',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'birth_date',
                  'age',
                  'gender',
                  'address',
                  'contact_number',
                  'date_graduated',
                  'course_type',
                  'school',
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
                  'tuburanCampus',
                  'user_type', 'graduate', 'admin_sao', 'system_admin','dean','campus_director','university_pres',
                  'job_description',
                  'skill',
                  'employment_status',
                  'employed',
                  'unemployed',
                  'is_active',
                  'staff',
                  'admin')
 
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
 
 
class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)
 
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)
 
    def clean(self):
        request = self.request
        data = self.cleaned_data
        email = data.get("email")
        password = data.get("password")
        user = authenticate(request, username=email, password=password)
        if user is None:
            raise forms.ValidationError("Invalid credentials")
        login(request, user)
        self.user = user
        return data
 
class RegisterForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
 
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ('email', 'IDNum', 'first_name', 'middle_name', 'last_name',
                  'course_type', 'school', 'date_graduated',
                   'employment_status', 'employed', 'unemployed',
                  'password1', 'password2',
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
                  'tuburanCampus')
 
        widgets = {
                   'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'true'}),
                   'IDNum': forms.NumberInput(attrs={'class': 'form-control', 'required': 'true'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
                   'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
                   'course_type': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
                   'school': forms.Select(attrs={'class': 'form-control','required': 'true'}),
                   'date_graduated': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
                   'employment_status': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
                   'password1': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'true'}),
                   'password2': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'true'}),
        }
 
    def clean_password2(self):
        '''
        Verify both passwords match.
        '''
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
 
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = True
 
        if commit:
            user.save()
        return user
 
class RegisterAdminForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ('email', 'first_name', 'middle_name', 'last_name',
                   'school', 'password1', 'password2','user_type',
                   'admin_sao', 'system_admin','dean','campus_director','university_pres',
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
                   'tuburanCampus',)
 
        widgets = {
                   'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'true'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
                   'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
                   'school': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
                   'user_type': forms.Select(attrs={'class': 'form-control', 'required': 'true'}),
                   'password1': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'true'}),
                   'password2': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'true'}),
                    }
 
    def clean_password2(self):
        '''
        Verify both passwords match.
        '''
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
 
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(RegisterAdminForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.active = True
 
        if commit:
            user.save()
        return user
 
 
class Profile(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
 
    class Meta:
        model = User
        fields = ('email', 'password', 'profile_picture')
 
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
 
# For updating their personal info
 
 
class GraduateForm(forms.ModelForm):
    GENDER = [
            ('Male', 'Male'),
            ('Female', 'Female'),
        ]
    gender = forms.CharField(max_length=6, widget=forms.Select(choices=GENDER)),
 
    class Meta:
        model = User
        fields = ('IDNum',
                  'profile_picture',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'birth_date',
                  'age',
                  'gender',
                  'address',
                  'contact_number',
                  'date_graduated',
                  'course_type',
                  'school',
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
                  'tuburanCampus',
                  'employment_status',
                  'job_description',
                  'skill',)
        widgets = {
         'IDNum': forms.NumberInput(attrs={'class': 'form-control'}),
         'profile_picture': forms.FileInput(attrs={'class': 'form-control'}),
         'first_name': forms.TextInput(attrs={'class': 'form-control'}),
         'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
         'last_name': forms.TextInput(attrs={'class': 'form-control'}),
         'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
         'age': forms.NumberInput(attrs={'class': 'form-control'}),
         'gender': forms.Select(attrs={'class': 'form-control'}),
         'address': forms.TextInput(attrs={'class': 'form-control'}),
         'contact_number': forms.NumberInput(attrs={'class': 'form-control'}),
         'date_graduated': forms.Select(attrs={'class': 'form-control'}),
         'course_type': forms.Select(attrs={'class': 'form-control'}),
         'school': forms.Select(attrs={'class': 'form-control'}),
         'employment_status': forms.Select(attrs={'class': 'form-control'}),
         'job_description': forms.TextInput(attrs={'class': 'form-control'}),
        #  'skill': forms.TextInput(attrs={'class': 'form-control', 'required': 'true'}),
            }
 
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
 
class PostFeedForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('body','image',)
 
        image = forms.ImageField(required=False)
 
 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
 
# Recommender System
 
 
class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('image', 'title', 'description')
 
        image = forms.ImageField(required=False)
 
 
class AdvertiseForm(forms.ModelForm):
    class Meta:
        model = Advertise
        fields = ('job_category',
                  'name',
                  'address_1',
                  'address_2',
                  'city',
                  'phone_number',
                  'email_address',
                  'personal_website',
                  'title',
                  'salary',
                  'description',
                  'image',
                  'job_sent')
 
        image = forms.ImageField(required=False)
 
 
class JobRequestForm(forms.ModelForm):
    class Meta:
        model = JobRequest
        fields = ('job_category', 'title', 'description')
 
 
class JobCategoryForm(forms.ModelForm):
    class Meta:
        model = JobCategory
        fields = ("__all__")
 
 
class CategoryTypeForm(forms.ModelForm):
    class Meta:
        model = CategoryType
        fields = ('job_category', 'title', 'description')
 
 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'middle_name',
                  'last_name', 'email', 'profile_picture')
 
 