from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Role(models.Model):
    role = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_on = models.DateTimeField(auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.role


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile')
    role = models.ForeignKey(Role, on_delete=models.CASCADE ,related_name= 'user_role', default=2)
    created_at = models.DateTimeField(auto_created=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_created=True, blank=True, null=True)


    def __str__(self):
        return self.user.username

        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 

    @classmethod
    def update_profile(cls, prof_id, updated_role):
        profile = cls.objects.filter(id = prof_id).update(role = updated_role)
        return profile

    def filter_by_user_role(cls, filter_role):
        try:
            role_user= cls.objects.filter(role__role__icontains=filter_role)
            return role_user
        except Exception:
            return  "No User found in your filter role"
    
    
    

class Agreement_type(models.Model):
    agreement_type = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_on = models.DateTimeField(auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.agreement_type



class Service_provider(models.Model):
    service_provider_name = models.CharField(max_length=255, unique=True)
    focal_point_name = models.CharField(max_length=255, unique=True)
    focal_point_email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_created=True)
    updated_on = models.DateTimeField(auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.service_provider_name

class Receiving_UNEP_division(models.Model):
    division_name = models.CharField(max_length=255, unique=True)
    division_focal_point = models.ForeignKey(Profile, on_delete=models.CASCADE )
    project_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_created=True)
    updated_on = models.DateTimeField(auto_created=True, blank=True, null=True)

    def __str__(self):
        return self.division_name

class Agreement(models.Model):
    agreement_title = models.CharField(max_length=255, unique=True)
    content_description = models.TextField()
    agreement_type = models.ForeignKey(Agreement_type, on_delete=models.CASCADE)
    division = models.ForeignKey(Receiving_UNEP_division, on_delete=models.CASCADE )
    service_provider = models.ForeignKey(Service_provider, on_delete=models.CASCADE)
    service_offered = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    focal_point = models.ForeignKey(Profile, on_delete=models.CASCADE )
    project_name = models.CharField(max_length=255)
    document_attachment = models.FileField(upload_to='documents/')
    uploaded_by = models.ForeignKey(Profile, on_delete=models.CASCADE ,related_name= 'uploader')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
            ordering = ('-created_at',)

    def __str__(self):
        return self.agreement_title

    def delete_agreement(self):
        self.delete()

    @classmethod
    def display_all_agreements(cls):
        return cls.objects.all()

    @classmethod 
    def search_agreement(cls, agreement_title):
        return Agreement.objects.filter(title__icontains = agreement_title)

    @classmethod
    def update_agreement(cls, agreement_id, updated_agreement_title):
        agreement = cls.objects.filter(id = agreement_id).update(title = updated_agreement_title)
        return agreement

    @classmethod
    def filter_by_agreement_type(cls, filter_agreement_type):
        try:
            agreement= cls.objects.filter(agreement_type__agreement_type__icontains=filter_agreement_type)
            return agreement
        except Exception:
            return  "No Agreements found in your filter agreement type"

    def filter_by_receiving_division(cls, filter_receiving_division):
        try:
            agreement= cls.objects.filter(division__receiving_unep_division__icontains=filter_receiving_division)
            return agreement
        except Exception:
            return  "No Agreements found in your filter receiving division"
    

    def filter_by_service_provider(cls, filter_service_provider):
        try:
            agreement= cls.objects.filter(service_provider__service_provider__icontains=filter_service_provider)
            return agreement
        except Exception:
            return  "No Agreements found in your filter service provider"



class Digital_assets_inventory(models.Model):
    boolean = (('Yes', 'Yes'), ('No', 'No' ))
    platform_title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    under_development = models.CharField(max_length=255,choices=boolean, blank=True, null=True)
    managing_institution = models.CharField(max_length=255 )
    manager = models.CharField(max_length=255 )
    spatial_coverage = models.CharField(max_length=255, blank=True, null=True)
    temporal_coverage = models.CharField(max_length=255, choices=boolean, blank=True, null=True)
    data_standards_compliance = models.CharField(max_length=255,choices=boolean, blank=True, null=True)
    web_services = models.CharField(max_length=255, blank=True, null=True)
    license_type = models.CharField(max_length=255, blank=True, null=True)
    backend_stack = models.CharField(max_length=255, blank=True, null=True)
    uploaded_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_created=True)
    updated_on = models.DateTimeField(auto_created=True, blank=True, null=True)


    class Meta:
            ordering = ('-created_at',)

    def __str__(self):
        return self.platform_title

    def delete_inventory(self):
        self.delete()

