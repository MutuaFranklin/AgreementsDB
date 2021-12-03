from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect, get_object_or_404
from api.models import Agreement, Agreement_type, Digital_assets_inventory, Profile, Role
from django.contrib.auth.decorators import login_required
import mimetypes
import os
from django.http.response import HttpResponse




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

    return render(request, 'registration/login.html')

@login_required(login_url='login')
def home(request):
    agreements = Agreement.objects.all()
    inventory = Digital_assets_inventory.objects.all()
    license_count = Agreement.filter_by_agreement_type('IT License')
    SLA_count = Agreement.filter_by_agreement_type('SLA')
    subscription_count = Agreement.filter_by_agreement_type('Subscription')

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
    current_user_profile = Profile.objects.filter(user = request.user)
    agreements = Agreement.objects.all()
    focal_role = Role.objects.filter(id=4).first()
    admin_role = Role.objects.filter(id=5).first()



    focal_point = Profile.objects.filter(role= focal_role)
    admin = Profile.objects.filter(role= admin_role)


    

       
    context = {
        "agreements":agreements,
        "focal_point":focal_point,
        "admin":admin,
        "current_user":current_user_profile,

       
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

@login_required(login_url='login')
def inventory(request):
    inventory = Digital_assets_inventory.objects.all()

    context = {
        "inventory":inventory,  
       
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