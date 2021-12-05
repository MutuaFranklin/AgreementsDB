from . models import Agreement, Digital_assets_inventory
from django import forms
from django.forms import widgets


class agreementPublishForm(forms.ModelForm):
    class Meta:
        model =  Agreement
        fields = [ 'agreement_title', 'content_description', 'agreement_type', 'division',
        'service_provider','service_offered', 'start_date','end_date', 'focal_point',
        'project_name', 'document_attachment']
        widgets = {
            'agreement_title': forms.TextInput(attrs={'class':'form-control'},), 
            'content_description':forms.Textarea(attrs={'class': 'form-control'}),
            'agreement_type':forms.Select(attrs={'class': 'form-control'}),
            'division':forms.Select(attrs={'class': 'form-control'}),
            'service_offered':forms.TextInput(attrs={'class': 'form-control'}),
            'service_provider':forms.Select(attrs={'class': 'form-control'}),
            'project_name':forms.TextInput(attrs={'class': 'form-control'}),
            'start_date':forms.DateInput(attrs={'class': 'form-control' , 'type': 'date'}),
            'end_date':forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'focal_point':forms.Select(attrs={'class': 'form-control'}),
            'document_attachment':forms.FileInput(attrs={'class': 'form-control'}),
   
        }



class updateAgreementForm(forms.ModelForm):
    class Meta:
        model =  Agreement
        fields = [ 'agreement_title', 'content_description', 'agreement_type', 'division',
        'service_provider','service_offered', 'start_date','end_date', 'focal_point',
        'project_name', 'document_attachment']
        widgets = {
            'agreement_title': forms.TextInput(attrs={'class':'form-control'},), 
            'content_description':forms.Textarea(attrs={'class': 'form-control'}),
            'agreement_type':forms.Select(attrs={'class': 'form-control'}),
            'division':forms.Select(attrs={'class': 'form-control'}),
            'service_offered':forms.TextInput(attrs={'class': 'form-control'}),
            'service_provider':forms.Select(attrs={'class': 'form-control'}),
            'project_name':forms.TextInput(attrs={'class': 'form-control'}),
            'start_date':forms.DateInput(attrs={'class': 'form-control' , 'type': 'date'}),
            'end_date':forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'focal_point':forms.Select(attrs={'class': 'form-control'}),
            'document_attachment':forms.FileInput(attrs={'class': 'form-control'}),
   
        }

