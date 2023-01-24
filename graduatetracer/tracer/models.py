from django.db import models
from django.utils import timezone
from datetime import date
import os
import datetime
 
from django.contrib.auth.models import (
    AbstractBaseUser, AbstractUser, BaseUserManager
)
 
 
class UserManager(BaseUserManager):
    def create_user(self, email,
                    profile_picture=None,
                    password=None,
                    IDNum=None,
                    first_name=None,
                    middle_name=None,
                    last_name=None,
                    school=None,
                    employment_status=None,
                    user_type=None,
                    is_argaoCampus=False,
                    is_bariliCampus=False,
                    is_carmenCampus=False,
                    is_CCMECampus=False,
                    is_daanbantayanCampus=False,
                    is_dumanjugExt=False,
                    is_danaoCampus=False,
                    is_ginatilanExt=False,
                    is_malabuyocExt=False,
                    is_mainCampus=False,
                    is_moalboalCampus=False,
                    is_nagaExt=False,
                    is_oslobExt=False,
                    is_pinamungajanExt=False,
                    is_sanfernandoExt=False,
                    is_sanfranciscoCampus=False,
                    is_tuburanCampus=False,
                    is_employed=False,
                    is_unemployed=False,
                    is_staff=False, is_admin=False, is_active=True,
                    is_graduate=False, is_system_admin=False, is_admin_sao=False,is_dean=False,is_campus_director=False,is_university_pres=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
 
        user_obj = self.model(email=self.normalize_email(email),
                              profile_picture=profile_picture,
                              first_name=first_name,
                              middle_name=middle_name,
                              last_name=last_name,
                              school=school,
                              employment_status=employment_status,
                              user_type=user_type,
                              )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_active = is_active
 
        user_obj.graduate = is_graduate
        user_obj.employed = is_employed
        user_obj.unemployed = is_unemployed
 
        user_obj.system_admin = is_system_admin
        user_obj.admin_sao = is_admin_sao
        user_obj.dean = is_dean
        user_obj.campus_director = is_campus_director
        user_obj.university_pres = is_university_pres
 
        user_obj.argaoCampus = is_argaoCampus
        user_obj.bariliCampus = is_bariliCampus
        user_obj.carmenCampus = is_carmenCampus
        user_obj.CCMECampus = is_CCMECampus
        user_obj.daanbantayanCampus = is_daanbantayanCampus
        user_obj.danaoCampus = is_danaoCampus
        user_obj.dumanjugExt = is_dumanjugExt
        user_obj.ginatilanExt = is_ginatilanExt
        user_obj.malabuyocExt = is_malabuyocExt
        user_obj.mainCampus = is_mainCampus
        user_obj.moalboalCampus = is_moalboalCampus
        user_obj.nagaExt = is_nagaExt
        user_obj.oslobExt = is_oslobExt
        user_obj.pinamungajanExt = is_pinamungajanExt
        user_obj.sanfernandoExt = is_sanfernandoExt
        user_obj.sanfranciscoCampus = is_sanfranciscoCampus
        user_obj.tuburanCampus = is_tuburanCampus
 
        user_obj.save(using=self._db)
        return user_obj
 
    def create_staffuser(self, email, password=None):
        user = self.create_user(email,
                                password=password,
                                is_staff=True,
                                )
        return user
 
    def create_superuser(self, email, password=None):
        user = self.create_user(email,
                                password=password,
                                is_staff=True,
                                is_admin=True,
                                is_system_admin=True,
                                )
        return user
 
 
class JobCategory(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=1000, null=True)
 
    # Notif Counter
    job_category_notif_counter = models.BooleanField(default=False)
 
    def __str__(self):
        return self.title
 
    class Meta:
        db_table = "jobcategory"
 
 
class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255, unique=True)
   
    year_dropdown = []
    for y in range(1912, (datetime.datetime.now().year + 1)):
        year_dropdown.append((y, y))
 
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
     )
   
    # Date_Graduated =(
    #     ('2020', '2020'),
    #     ('2021', '2021'),
    #     ('2022', '2022'),
    #     ('2023', '2023'),
    #     ('2024', '2024'),
    #     ('2025', '2025'),
    #     ('2026', '2026'),
    #     ('2027', '2027'),
    #     ('2028', '2028'),
    #     ('2029', '2029'),
    #     ('2030', '2030'),
    # )
    Employment_Status = (
        ('Employed', 'Employed'),
        ('Unemployed', 'Unemployed'),
    )
    Type_of_User = (
        ('AdminSao', 'AdminSao'),
        ('SystemAdmin', 'SystemAdmin'),
        ('DEAN', 'DEAN'),
        ('Campus Director', 'Campus Director'),
        ('University President', 'University President'),
    )
    Course_Type = (
        ('Bachelor of Science in Information Technology', 'Bachelor of Science in Information Technology'),
        ('Bachelor in Industrial Technology Major in Computer Technology', 'Bachelor in Industrial Technology Major in Computer Technology'),
        ('Bachelor in Elementary Education', 'Bachelor in Elementary Education'),
        ('Bachelor in Industrial Technology - Drafting Technology', 'Bachelor in Industrial Technology - Drafting Technology'),
        ('Bachelor in Industrial Technology - Electrical Technology', 'Bachelor in Industrial Technology - Electrical Technology'),
        ('Bachelor in Industrial Technology -  Electronics Technology', 'Bachelor in Industrial Technology -  Electronics Technology'),
        ('Bachelor in Industrial Technology - Automotive Technology', 'Bachelor in Industrial Technology - Automotive Technology'),
        ('Bachelor in Industrial Technology - Food Technology', 'Bachelor in Industrial Technology - Food Technology'),
        ('Bachelor in Industrial Technology - Garments Technology', 'Bachelor in Industrial Technology - Garments Technology'),
        ('Bachelor in Industrial Technology - Machine Shop Technology', 'Bachelor in Industrial Technology - Machine Shop Technology'),
        ('Bachelor in Industrial Technology - Welding and Fabrication Technology', 'Bachelor in Industrial Technology - Welding and Fabrication Technology'),
        ('Bachelor in Secondary Education Major in Math', 'Bachelor in Secondary Education Major in Math'),
        ('Bachelor in Secondary Education Major in Science', 'Bachelor in Secondary Education Major in Science'),
        ('Bachelor in Secondary Education Major in English', 'Bachelor in Secondary Education Major in English'),
        ('Bachelor in Secondary Education Major in Social Studies', 'Bachelor in Secondary Education Major in Social Studies'),
        ('Bachelor of Technology and Livelihood Education', 'Bachelor of Technology and Livelihood Education'),
        ('Bachelor of Technology and Livelihood Education Major in Home Economics', 'Bachelor of Technology and Livelihood Education Major in Home Economics'),
        ('Bachelor of Technology and Livelihood Education Major in Information and Communications Technology', 'Bachelor of Technology and Livelihood Education Major in Information and Communications Technology'),
        ('Bachelor of Arts in English', 'Bachelor of Arts in English'),
        ('Bachelor of Arts in English Major in Language Studies', 'Bachelor of Arts in English Major in Language Studies'),
        ('Bachelor of Arts in Literature', 'Bachelor of Arts in Literature'),
        ('Bachelor of Arts in Literature Major in Literature and Cultural Studies', 'Bachelor of Arts in Literature Major in Literature and Cultural Studies'),
        ('Bachelor of Early Childhood Education', 'Bachelor of Early Childhood Education'),
        ('Bachelor in Elementary Education Major in Content Education', 'Bachelor in Elementary Education Major in Content Education'),
        ('Bachelor of Industrial Technology Major in Civil Technology', 'Bachelor of Industrial Technology Major in Civil Technology'),
        ('Bachelor of Industrial Technology Major in Cosmetology', 'Bachelor of Industrial Technology Major in Cosmetology'),
        ('Bachelor of Industrial Technology Major in Furniture and Cabinetmaking Technology', 'Bachelor of Industrial Technology Major in Furniture and Cabinetmaking Technology'),
        ('Bachelor of Industrial Technology Major in Interior Design Technology', 'Bachelor of Industrial Technology Major in Interior Design Technology'),
        ('Bachelor of Industrial Technology Major in Power Plant Technology', 'Bachelor of Industrial Technology Major in Power Plant Technology'),
        ('Bachelor of Industrial Technology Major in Refrigeration and and Air-Conditioning Technology', 'Bachelor of Industrial Technology Major in Refrigeration and and Air-Conditioning Technology'),
        ('Bachelor of Public Administration', 'Bachelor of Public Administration',),
        ('Bachelor of Science in AgriBusiness', 'Bachelor of Science in AgriBusiness'),
        ('Bachelor of Science in Agricultural and Biosystems Engineering', 'Bachelor of Science in Agricultural and Biosystems Engineering'),
        ('Bachelor of Science in Agriculture', 'Bachelor of Science in Agriculture'),
        ('Bachelor of Science in Agriculture Major in Horticulture', 'Bachelor of Science in Agriculture Major in Horticulture'),
        ('Bachelor of Science in Agriculture-Animal Production', 'Bachelor of Science in Agriculture-Animal Production'),
        ('Bachelor of Science in Business Administration - MM', 'Bachelor of Science in Business Administration - MM'),
        ('Bachelor of Science in Civil Engineering', 'Bachelor of Science in Civil Engineering'),
        ('Bachelor of Science in Computer Engineering', 'Bachelor of Science in Computer Engineering'),
        ('Bachelor of Science in Development Communication', 'Bachelor of Science in Development Communication'),
        ('Bachelor of Science in Electrical Engineering', 'Bachelor of Science in Electrical Engineering'),
        ('Bachelor of Science in Electronic Engineering', 'Bachelor of Science in Electronic Engineering'),
        ('Bachelor of Science in Fisheries', 'Bachelor of Science in Fisheries'),
        ('Bachelor of Science in Food Technology', 'Bachelor of Science in Food Technology'),
        ('Bachelor of Science in Forestry', 'Bachelor of Science in Forestry'),
        ('Bachelor of Science in Graphics and Designs', 'Bachelor of Science in Graphics and Designs'),
        ('Bachelor of Science in Hospitality Management', 'Bachelor of Science in Hospitality Management'),
        ('Bachelor of Science in Industrial Engineering', 'Bachelor of Science in Industrial Engineering'),
        ('Bachelor of Science in Marine Engineering', 'Bachelor of Science in Marine Engineering'),
        ('Bachelor of Science in Mathematics', 'Bachelor of Science in Mathematics'),
        ('Bachelor of Science in Mechanical Engineering', 'Bachelor of Science in Mechanical Engineering'),
        ('Bachelor of Science in Mechatronics Technology', 'Bachelor of Science in Mechatronics Technology'),
        ('Bachelor of Science in Nursing', 'Bachelor of Science in Nursing'),
        ('Bachelor of Science in Psychology', 'Bachelor of Science in Psychology'),
        ('Bachelor of Science in Statistics', 'Bachelor of Science in Statistics'),
        ('Bachelor of Science in Technology Management', 'Bachelor of Science in Technology Management'),
        ('Bachelor of Science in Tourism Management', 'Bachelor of Science in Tourism Management'),
        ('Bachelor of Special Needs Education Major in Generalist', 'Bachelor of Special Needs Education Major in Generalist'),
        ('Bachelor of Special Needs Education Major in Teaching and Hard of Hearing Learners', 'Bachelor of Special Needs Education Major in Teaching and Hard of Hearing Learners'),
        ('Bachelor of Technical and Vocational Teachers Education', 'Bachelor of Technical and Vocational Teachers Education'),
        ('Bachelor of Technical Vocational Teacher Education Major in Automotive Technology', 'Bachelor of Technical Vocational Teacher Education Major in Automotive Technology'),
        ('Bachelor of Technical Vocational Teacher Education Major in Drafting Technology', 'Bachelor of Technical Vocational Teacher Education Major in Drafting Technology'),
        ('Bachelor of Technical Vocational Teacher Education Major in Electrical Technology', 'Bachelor of Technical Vocational Teacher Education Major in Electrical Technology'),
        ('Bachelor of Technical Vocational Teacher Education Major in Electronics Technology', 'Bachelor of Technical Vocational Teacher Education Major in Electronics Technology'),
        ('Bachelor of Technical Vocational Teacher Education Major in Food Service Management', 'Bachelor of Technical Vocational Teacher Education Major in Food Service Management'),
        ('Bachelor of Technical Vocational Teacher Education Major in Garments Fashion and Design', 'Bachelor of Technical Vocational Teacher Education Major in Garments Fashion and Design'),
        ('Bachelor of Technical Vocational Teacher Education Major in Welding and Fabrication Technology', 'Bachelor of Technical Vocational Teacher Education Major in Welding and Fabrication Technology'),
        ('Bachelor of Technology and Livelihood Education Major in Industrial Arts', 'Bachelor of Technology and Livelihood Education Major in Industrial Arts'),
        ('Batsilyer ng Sining sa Filipino', 'Batsilyer ng Sining sa Filipino'),
        ('Certificate in Professional Education', 'Certificate in Professional Education'),
        ('Certificate of Technology Major in Computer Technology - Deaf Students', 'Certificate of Technology Major in Computer Technology - Deaf Students'),
        ('Certificate of Technology Major in Food Technology - Deaf Students', 'Certificate of Technology Major in Food Technology - Deaf Students'),
        ('DECE Practice Teaching', 'DECE Practice Teaching'),
        ('Diploma in Early Childhood Education', 'Diploma in Early Childhood Education'),
        ('Diploma in Early Childhood Education - Blended Learning', 'Diploma in Early Childhood Education - Blended Learning'),
        ('Diploma in Professional Education', 'Diploma in Professional Education'),
        ('Diploma in Professional Education - Blended Learning', 'Diploma in Professional Education - Blended Learning'),
        ('Diploma in Special Education', 'Diploma in Special Education'),
        ('Diploma in Special Education - Blended Learning', 'Diploma in Special Education - Blended Learning'),
        ('Doctor in Development Education', 'Doctor in Development Education'),
        ('Doctor in Development Education Major in Early Childhood Education', 'Doctor in Development Education Major in Early Childhood Education'),
        ('Doctor in Public Administration', 'Doctor in Public Administration'),
        ('Doctor in Development Education Major in Early Childhood Education - Blended Learning', 'Doctor in Development Education Major in Early Childhood Education - Blended Learning'),
        ('Doctor in Development Education Major in Guidance and Counseling', 'Doctor in Development Education Major in Guidance and Counseling'),
        ('Doctor in Development Education Major in Guidance and Counseling - Blended Learning', 'Doctor in Development Education Major in Guidance and Counseling - Blended Learning'),
        ('Doctor in Development Education Major in Special Education', 'Doctor in Development Education Major in Special Education'),
        ('Doctor in Development Education Major in Sped-Blended Learning', 'Doctor in Development Education Major in Sped-Blended Learning'),
        ('Doctor of Philosophy in Animal Science', 'Doctor of Philosophy in Animal Science'),
        ('Doctor of Philosophy in Horticulture', 'Doctor of Philosophy in Horticulture'),
        ('Doctor of Philosophy in Technology Management', 'Doctor of Philosophy in Technology Management'),
        ('Doctor of Veterinary Medicine', 'Doctor of Veterinary Medicine'),
        ('DPE Practice Teaching - Blended Learning', 'DPE Practice Teaching - Blended Learning'),
        ('DSPED Practice Teaching', ' DSPED Practice Teaching'),
        ('Foundation of Education-MAED ECE-Blended Learning', 'Foundation of Education-MAED ECE-Blended Learning'),
        ('Foundation of Education-MAED GC-Blended Learning', 'Foundation of Education-MAED GC-Blended Learning'),
        ('Foundation of Education-MAED Math-Blended Learning', 'Foundation of Education-MAED Math-Blended Learning'),
        ('Foundation of Education-MAED Sped-Blended Learning', 'Foundation of Education-MAED Sped-Blended Learning'),
        ('Master in Engineering Technology', 'Master in Engineering Technology'),
        ('Master in Fisheries and Aquatic Sciences', 'Master in Fisheries and Aquatic Sciences'),
        ('Master in Public Administration', 'Master in Public Administration'),
        ('Master in Technician Education Major in Automotive Technology', 'Master in Technician Education Major in Automotive Technology'),
        ('Master in Technician Education Major in Civil Technology', 'Master in Technician Education Major in Civil Technology'),
        ('Master in Technician Education Major in Drafting Technology', 'Master in Technician Education Major in Drafting Technology'),
        ('Master in Technician Education Major in Electrical Technology', 'Master in Technician Education Major in Electrical Technology'),
        ('Master in Technician Education Major in Electronics Technology', 'Master in Technician Education Major in Electronics Technology'),
        ('Master in Technician Education Major in Machine Shop Technology', 'Master in Technician Education Major in Machine Shop Technology'),
        ('Master in Vocational Education', 'Master in Vocational Education'),
        ('Master of Arts in Education Major in Administration and Supervision', 'Master of Arts in Education Major in Administration and Supervision'),
        ('Master of Arts in Education Major in Early Childhood Education', 'Master of Arts in Education Major in Early Childhood Education'),
        ('Master of Arts in Education Major in English Teaching', 'Master of Arts in Education Major in English Teaching'),
        ('Master of Arts in Education Major in Filipino Teaching', 'Master of Arts in Education Major in Filipino Teaching'),
        ('Master of Arts in Education Major in Guidance and Counseling', 'Master of Arts in Education Major in Guidance and Counseling'),
        ('Master of Arts in Education Major in Mathematics', 'Master of Arts in Education Major in Mathematics'),
        ('Master of Arts in Education Major in Teaching Biology', 'Master of Arts in Education Major in Teaching Biology'),
        ('Master of Arts in Education Major in Teaching Chemistry', 'Master of Arts in Education Major in Teaching Chemistry'),
        ('Master of Arts in Education Major in Teaching Science', 'Master of Arts in Education Major in Teaching Science'),
        ('Master of Arts in Education Major in Teaching Social Studies', 'Master of Arts in Education Major in Teaching Social Studies'),
        ('Master of Arts in Education Major in Teaching Mathematics', 'Master of Arts in Education Major in Teaching Mathematics'),
        ('Master of Arts in Education Major in Teaching Physical Education', 'Master of Arts in Education Major in Teaching Physical Education'),
        ('Master of Arts in Education Major in Teaching Physical Education and Sports', 'Master of Arts in Education Major in Teaching Physical Education and Sports'),
        ('Master of Arts in Education Major in Teaching Physics', 'Master of Arts in Education Major in Teaching Physics'),
        ('Master of Arts in Vocational Education', 'Master of Arts in Vocational Education'),
        ('Master of Science in AgriBusiness', 'Master of Science in AgriBusiness'),
 
    )
 
    School = (
            ('Argao Campus', 'Argao Campus'),
            ('Barili Campus', 'Barili Campus'),
            ('Carmen Campus', 'Carmen Campus'),
            ('Cebu City Mountain Extension Campus', 'Cebu City Mountain Extension Campus'),
            ('Daanbantayan Campus', 'Daanbantayan Campus'),
            ('Danao Campus', 'Danao Campus'),
            ('Dumanjug Extension Campus', 'Dumanjug Extension Campus'),
            ('Ginatilan Extension Campus', 'Ginatilan Extension Campus'),
            ('Malabuyoc Extension Campus', 'Malabuyoc Extension Campus'),
            ('Main Campus', 'Main Campus'),
            ('Moalboal Campus', 'Moalboal Campus'),
            ('Naga Extension Campus', 'Naga Extension Campus'),
            ('Oslob Extension Campus', 'Oslob Extension Campus'),
            ('Pinamungajan Extension Campus', 'Pinamungajan Extension Campus'),
            ('San Fernando Extension Campus', 'San Fernando Extension Campus'),
            ('San Francisco Campus', 'San Francisco Campus'),
            ('Tuburan Campus', 'Tuburan Campus'),
        )
 
    profile_picture = models.ImageField(default="default_profile_2.png", null=True, blank=True)
    IDNum = models.PositiveIntegerField(blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=200, null=True)
    middle_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    birth_date = models.DateField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, choices=GENDER, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    contact_number = models.CharField(max_length=200, null=True, blank=True)
    date_graduated = models.IntegerField(('date_graduated'),choices=year_dropdown, default=datetime.datetime.now().year)
    course_type = models.CharField(max_length=100, blank=True, null=True, choices=Course_Type)
    employment_status = models.CharField(max_length=100, blank=True, null=True, choices=Employment_Status)
    school = models.CharField(max_length=100, blank=True, null=True, choices=School)
    user_type = models.CharField(max_length=100, blank=True, null=True, choices=Type_of_User)
    job_description = models.CharField(max_length=200, null=True, blank=True)
    skill = models.ForeignKey(JobCategory, on_delete=models.CASCADE, null=True, blank=True)
 
    # employment_status = models.ForeignKey(GraduateStatus, on_delete=models.CASCADE, blank=True, null=True)
    employed = models.BooleanField(default=False)
    unemployed = models.BooleanField(default=False)
 
    graduate = models.BooleanField(default=False)
    admin_sao = models.BooleanField(default=False)
    system_admin = models.BooleanField(default=False)
    dean = models.BooleanField(default=False)
    campus_director = models.BooleanField(default=False)
    university_pres = models.BooleanField(default=False)
 
    # school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
    argaoCampus= models.BooleanField(default=False)
    bariliCampus= models.BooleanField(default=False)
    carmenCampus= models.BooleanField(default=False)
    CCMECampus= models.BooleanField(default=False)
    daanbantayanCampus= models.BooleanField(default=False)
    danaoCampus= models.BooleanField(default=False)
    dumanjugExt= models.BooleanField(default=False)
    ginatilanExt= models.BooleanField(default=False)
    malabuyocExt= models.BooleanField(default=False)
    mainCampus= models.BooleanField(default=False)
    moalboalCampus= models.BooleanField(default=False)
    nagaExt= models.BooleanField(default=False)
    oslobExt= models.BooleanField(default=False)
    pinamungajanExt= models.BooleanField(default=False)
    sanfernandoExt= models.BooleanField(default=False)
    sanfranciscoCampus= models.BooleanField(default=False)
    tuburanCampus= models.BooleanField(default=False)
 
    pending = models.BooleanField(default=True)
    approved = models.BooleanField(default=False)
 
    is_active = models.BooleanField(default=True)  # can login
    staff = models. BooleanField(default=False)  # staff user non superuser
    admin = models.BooleanField(default=False)  # superuser
    timestamp = models.DateTimeField(auto_now_add=True)
 
    job_sent_list = models.CharField(max_length=5000, null=True)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
 
    objects = UserManager()
 
    def __str__(self):
        return self.email
 
    def get_full_name(self):
        return self.email
 
    def get_short_name(self):
        return self.email
 
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
 
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
 
    @property
    def is_graduate(self):
        return self.graduate
 
    @property
    def is_argaoCampus(self):
        return self.argaoCampus
    @property
    def is_bariliCampus(self):
        return self.bariliCampus
    @property
    def is_carmenCampus(self):
        return self.carmenCampus
    @property
    def is_CCMECampus(self):
        return self.CCMECampus
    @property
    def is_daanbantayanCampus(self):
        return self.daanbantayanCampus
    @property
    def is_danaoCampus(self):
        return self.danaoCampus
    @property
    def is_dumanjugExt(self):
        return self.dumanjugExt
    @property
    def is_ginatilanExt(self):
        return self.ginatilanExt
 
    @property
    def is_malabuyocExt(self):
        return self.malabuyocExt
 
    @property
    def is_mainCampus(self):
        return self.mainCampus
    @property
    def is_moalboalCampus(self):
        return self.moalboalCampus
    @property
    def is_nagaExt(self):
        return self.nagaExt
    @property
    def is_oslobExt(self):
        return self.oslobExt
    @property
    def is_pinamungajanExt(self):
        return self.pinamungajanExt
    @property
    def is_sanfernandoExts(self):
        return self.sanfernandoExts
    @property
    def is_sanfranciscoCampus(self):
        return self.sanfranciscoCampus
    @property
    def is_tuburanCampus(self):
        return self.tuburanCampus
 
    @property
    def is_admin_sao(self):
        return self.admin_sao
 
    @property
    def is_system_admin(self):
        return self.system_admin
    @property
    def is_dean(self):
        return self.dean
 
    @property
    def is_campus_director(self):
        return self.campus_director
 
    @property
    def is_university_pres(self):
        return self.university_pres
 
    @property
    def is_staff(self):
        return self.staff
 
    @property
    def is_admin(self):
        return self.admin
 
    class Meta:
        db_table = "user"
 
class SystemUser(AbstractUser):
 
    Type_of_User = (
        ('AdminSao', 'AdminSao'),
        ('SystemAdmin', 'SystemAdmin'),
        ('DEAN', 'DEAN'),
        ('Campus Director', 'Campus Director'),
        ('University President', 'University President'),
    )
    School = (
            ('Argao Campus', 'Argao Campus'),
            ('Barili Campus', 'Barili Campus'),
            ('Carmen Campus', 'Carmen Campus'),
            ('Cebu City Mountain Extension Campus', 'Cebu City Mountain Extension Campus'),
            ('Daanbantayan Campus', 'Daanbantayan Campus'),
            ('Danao Campus', 'Danao Campus'),
            ('Dumanjug Extension Campus', 'Dumanjug Extension Campus'),
            ('Ginatilan Extension Campus', 'Ginatilan Extension Campus'),
            ('Malabuyoc Extension Campus', 'Malabuyoc Extension Campus'),
            ('Main Campus', 'Main Campus'),
            ('Moalboal Campus', 'Moalboal Campus'),
            ('Naga Extension Campus', 'Naga Extension Campus'),
            ('Oslob Extension Campus', 'Oslob Extension Campus'),
            ('Pinamungajan Extension Campus', 'Pinamungajan Extension Campus'),
            ('San Fernando Extension Campus', 'San Fernando Extension Campus'),
            ('San Francisco Campus', 'San Francisco Campus'),
            ('Tuburan Campus', 'Tuburan Campus'),
        )
    userid = models.CharField(max_length=45,primary_key = True)
    username = models.CharField(primary_key=False,max_length=45, blank=True, null=True)
    email = models.EmailField(null = True)
    first_name = models.CharField(max_length=45, blank=True)
    middle_name = models.CharField(max_length=45, blank=True)
    last_name = models.CharField(max_length=45, blank=True)
 
    school = models.CharField(max_length=100, blank=True, null=True, choices=School)
    argaoCampus= models.BooleanField(default=False)
    bariliCampus= models.BooleanField(default=False)
    carmenCampus= models.BooleanField(default=False)
    CCMECampus= models.BooleanField(default=False)
    daanbantayanCampus= models.BooleanField(default=False)
    danaoCampus= models.BooleanField(default=False)
    dumanjugExt= models.BooleanField(default=False)
    ginatilanExt= models.BooleanField(default=False)
    malabuyocExt= models.BooleanField(default=False)
    mainCampus= models.BooleanField(default=False)
    moalboalCampus= models.BooleanField(default=False)
    nagaExt= models.BooleanField(default=False)
    oslobExt= models.BooleanField(default=False)
    pinamungajanExt= models.BooleanField(default=False)
    sanfernandoExt= models.BooleanField(default=False)
    sanfranciscoCampus= models.BooleanField(default=False)
    tuburanCampus= models.BooleanField(default=False)
 
    user_type = models.CharField(max_length=100, blank=True, null=True, choices=Type_of_User)
    admin_sao = models.BooleanField(default=False)
    system_admin = models.BooleanField(default=False)
    dean = models.BooleanField(default=False)
    campus_director = models.BooleanField(default=False)
    university_pres = models.BooleanField(default=False)
    profile_picture = models.ImageField(default="default_profile_2.png", null=True, blank=True)
 
 
    is_active = models.BooleanField(default=True)  # can login
    staff = models. BooleanField(default=False)  # staff user non superuser
    admin = models.BooleanField(default=False)  # superuser
    timestamp = models.DateTimeField(auto_now_add=True)
 
    job_sent_list = models.CharField(max_length=5000, null=True)
 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
 
    objects = UserManager()
 
    def __str__(self):
        return self.email
 
    def get_full_name(self):
        return self.email
 
    def get_short_name(self):
        return self.email
 
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
 
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
 
    @property
    def is_graduate(self):
        return self.graduate
 
    @property
    def is_argaoCampus(self):
        return self.argaoCampus
    @property
    def is_bariliCampus(self):
        return self.bariliCampus
    @property
    def is_carmenCampus(self):
        return self.carmenCampus
    @property
    def is_CCMECampus(self):
        return self.CCMECampus
    @property
    def is_daanbantayanCampus(self):
        return self.daanbantayanCampus
    @property
    def is_danaoCampus(self):
        return self.danaoCampus
    @property
    def is_dumanjugExt(self):
        return self.dumanjugExt
    @property
    def is_ginatilanExt(self):
        return self.ginatilanExt
   
    @property
    def is_malabuyocExt(self):
        return self.malabuyocExt
   
    @property
    def is_mainCampus(self):
        return self.mainCampus
    @property
    def is_moalboalCampus(self):
        return self.moalboalCampus
    @property
    def is_nagaExt(self):
        return self.nagaExt
    @property
    def is_oslobExt(self):
        return self.oslobExt
    @property
    def is_pinamungajanExt(self):
        return self.pinamungajanExt
    @property
    def is_sanfernandoExts(self):
        return self.sanfernandoExts
    @property
    def is_sanfranciscoCampus(self):
        return self.sanfranciscoCampus
    @property
    def is_tuburanCampus(self):
        return self.tuburanCampus
 
    @property
    def is_dean(self):
        return self.dean
 
    @property
    def is_campus_director(self):
        return self.campus_director
 
    @property
    def is_university_pres(self):
        return self.university_pres
 
    @property
    def is_staff(self):
        return self.staff
 
    @property
    def is_admin(self):
        return self.admin
 
    class Meta:
        db_table = "systemuser"
 
class Post(models.Model):
    body = models.TextField()
    image = models.ImageField(upload_to='upload_photos', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(
        User, blank=True, related_name='dislikes')
 
    class Meta:
        db_table = "post"
 
 
class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
 
    class Meta:
        db_table = "comment"
 
 
class WorkExperiences(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    graduateUser = models.ForeignKey(User, on_delete=models.CASCADE)
    experienceStartDate = models.DateField(blank=True, null=True)
    experienceEndDate = models.DateField(blank=True, null=True)
 
    def __str__(self):
        return self.graduateUser
 
    class Meta:
        db_table = "workexperiences"
 
# Recommender System
 
 
class Announcement(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=1000, null=True)
    image = models.ImageField(
        upload_to='announcements/img', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
 
    # Notif Counter
    announcement_notif_counter = models.BooleanField(default=False)
 
    def __str__(self):
        return self.title
 
    class Meta:
        db_table = "announcement"
 
 
 
class CategoryType(models.Model):
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True)
    total_vote = models.IntegerField(default=0, editable=False)
 
    def __str__(self):
        return "{} - {}".format(self.job_category, self.job_category.title)
 
    class Meta:
        db_table = "categorytype"
 
 
class ControlVote(models.Model):
    user = models.ForeignKey(User,  null=True, on_delete=models.SET_NULL)
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
 
    def __str__(self):
        return "{} - {} - {}".format(self.user, self.job_category, self.status)
 
 
    class Meta:
        db_table = "controlvote"
 
 
class JobRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    job_category = models.ForeignKey(
        JobCategory, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True)
    total_vote = models.IntegerField(default=0, editable=False)
    # Notif Counter
    job_request_notif_counter = models.BooleanField(default=False)
 
    def __str__(self):
        return "{} - {}".format(self.job_category, self.job_category.title)
 
    class Meta:
        db_table = "jobrequest"
 
 
class Advertise(models.Model):
    job_category = models.ForeignKey(
        JobCategory, on_delete=models.CASCADE, null=True, blank=True)
 
    # About the Company
    name = models.CharField(max_length=50, null=True)
    address_1 = models.CharField(max_length=50, null=True)
    address_2 = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    email_address = models.CharField(max_length=50, null=True)
    personal_website = models.CharField(max_length=50, null=True, blank=True)
 
    # About the job
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=1000, null=True)
    image = models.ImageField(
        upload_to='advertisement/img', null=True, blank=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
 
    # Recommender System conditions
    job_sent = models.IntegerField(default=0, null=True, blank=True)
 
    # Notif Counter
    job_advertise_notif_counter = models.BooleanField(default=False)
    
    # Users sent
    user_advertise_list = models.CharField(max_length=5000, null=True)
 
    def __str__(self):
        return self.title
 
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)
 
    class Meta:
        db_table = "advertise"
 

