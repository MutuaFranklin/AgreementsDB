from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect, get_object_or_404
from api.forms import agreementPublishForm, updateAgreementForm
from api.models import Agreement, Agreement_type, Digital_assets_inventory, Profile, Role, Service_provider, Receiving_UNEP_division
from django.contrib.auth.decorators import login_required
import mimetypes
import os
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin



# Create your views here.
def index(request):
    
    return render(request, 'agreements/index.html')

def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'username or password not correct')
            return redirect('login')

    return render(request, 'registration/login.html')

@login_required(login_url='login')
def home(request):
    agreements = Agreement.objects.all()    
    license_count = Agreement.filter_by_agreement_type('IT License')
    SLA_count = Agreement.filter_by_agreement_type('SLA')
    subscription_count = Agreement.filter_by_agreement_type('Subscription')
    inventory = Digital_assets_inventory.objects.all()


    context = {
        "agreements":agreements,
        "inventory":inventory,
        "license": license_count,
        "sla":SLA_count,
        "subscription": subscription_count,  

       
    }


    return render(request, 'agreements/home.html', context)

@login_required(login_url='login')
def agreements(request):
    agreements = Agreement.objects.all()
    agreement_types = Agreement_type.objects.all()
    service_providers = Service_provider.objects.all()
    receiving_divisions = Receiving_UNEP_division.objects.all()
    current_user_profile = Profile.objects.filter(user = request.user)
    focal_role = Role.objects.filter(id=4).first()
    admin_role = Role.objects.filter(id=3).first()


    if request.method == 'POST':
        aForm = agreementPublishForm(request.POST, request.FILES)
        if aForm.is_valid():
            agreement_publish = aForm.save(commit=False)
            agreement_publish.uploaded_by =request.user.profile
            agreement_publish.save()
            messages.success(request, 'Form submission successful')
            return redirect('agreements')
        else:
            messages.error(request, 'Form submission unsuccessful')
            return redirect('agreements')
    else:
        aForm = agreementPublishForm()

   
    
 
       
    context = {
        "agreements":agreements,
        "agreement_types":agreement_types,
        "service_providers":service_providers,
        "divisions":receiving_divisions,
        "focal":focal_role,
        "admin":admin_role,
        "current_user":current_user_profile,
        "aForm": aForm,

       
    }
    
    return render(request, 'agreements/agreements.html', context)

@login_required(login_url='login')
def view_agreement(request, id):
    agreement = Agreement.objects.filter(id=id).first()
    context = {
        "agreement":agreement,  
       
    }
    return render(request, 'agreements/single_agreement.html', context)


@login_required(login_url='login')
def update_agreement(request, id):
    agreement = Agreement.objects.filter(id=id).first()
    context = {
        "agreement":agreement,  
       
    }
    return render(request, 'updates/update_agreement.html', context)


class UpdateAgreementView(UpdateView, SuccessMessageMixin):
    model=Agreement
    form_class =updateAgreementForm
    template_name ='updates/update_agreement.html'
    
    def get_queryset(self): 
        return Agreement.objects.all()


    def get_success_url(self):
       
        # return HttpResponseRedirect('/agreement/{{agreement.id}})
        return reverse_lazy('agreements') 
    success_message = 'Agreement successfully updated'



# class AgreementDeleteView(DeleteView):
#     model = Agreement
#     success_url = reverse_lazy('agreements')

#     success_message = 'Agreement successfully deleted'

@login_required(login_url='login')
def delete_agreement(request, id):
    agreement = Agreement.objects.filter(id=id).first()
    agreement.delete()

    aForm = agreementPublishForm()
    context = {
        "agreement":agreement,
        "aForm": aForm,       
  
       
    }
    messages.success(request, 'Agreement record deleted successfully')

    return redirect(request.META['HTTP_REFERER'])


    

@login_required(login_url='login')
def inventory(request):
    inventory = Digital_assets_inventory.objects.all()
    focal_role = Role.objects.filter(id=4).first()
    admin_role = Role.objects.filter(id=5).first()


    context = {
        "inventory":inventory,  
        "focal":focal_role,
        "admin":admin_role,
    }
    
    return render(request, 'agreements/inventory.html', context)


@login_required(login_url='login')
def view_inventory(request, id):
    inventory = Digital_assets_inventory.objects.filter(id=id).first()

    context = {
        "inventory":inventory,  
       
    }
    return render(request, 'agreements/single_inventory.html', context)


@login_required(login_url='login')
def update_inventory(request, id):
    inventory = Digital_assets_inventory.objects.filter(id=id).first()

    context = {
        "inventory":inventory,  
       
    }
    return render(request, 'updates/update_inventory.html', context)


class InventoryDeleteView(DeleteView):
    model = Digital_assets_inventory
    success_url = reverse_lazy('agreement')


def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'test.txt'
    # Define the full file path
    filepath = BASE_DIR + '/filedownload/Files/' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response


@login_required(login_url='login')
def focal_points(request):

    context = {
       
    }
    
    return render(request, 'focal-points/focal_points.html', context)