from . models import Agreement, Digital_assets_inventory
from django import forms
from django.forms import widgets


class RegisterBizForm(forms.ModelForm):
    class Meta:
        model =  Agreement
        fields = [ 'agreement_title', 'content_description', 'agreement_type', 'division',
        'service_provider','service_offered', 'start_date','end_date', 'focal_point',
        'project_name', 'document_attachment']
        widgets = {
            'agreement_title': forms.TextInput(attrs={'class':'form-control'}), 
            'content_description':forms.TextInput(attrs={'class': 'form-control'}),
            'agreement_type':forms.Select(attrs={'class': 'form-control'}),
            'division':forms.Select(attrs={'class': 'form-control'}),
            'service_offered':forms.TextInput(attrs={'class': 'form-control'}),
            'service_provider':forms.Select(attrs={'class': 'form-control'}),
            'biz_image':forms.FileInput(attrs={'class': 'form-control'}),

            
            
        
        }

#  agreement_title = models.CharField(max_length=255, unique=True)
#     content_description = models.TextField()
#     agreement_type = models.ForeignKey(Agreement_type, on_delete=models.CASCADE)
#     division = models.ForeignKey(Receiving_UNEP_division, on_delete=models.CASCADE )
#     service_provider = models.ForeignKey(Service_provider, on_delete=models.CASCADE)
#     service_offered = models.TextField()
#     start_date = models.DateField()
#     end_date = models.DateField()
#     focal_point = models.ForeignKey(Profile, on_delete=models.CASCADE )
#     project_name = models.CharField(max_length=255)
#     document_attachment = models.FileField(upload_to='documents/')
#     uploaded_by = models.ForeignKey(Profile, on_delete=models.CASCADE ,related_name= 'uploader')
#     created_at = models.DateTimeField(auto_created=True)
#     updated_on = models.DateTimeField(auto_created=True, blank=True, null=True)
